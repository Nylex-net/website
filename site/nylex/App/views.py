from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.template import loader
from django.db.models import Q
from .models import Page
import re
from rest_framework import viewsets
from .serializers import WebsiteSerializer
from django.shortcuts import render
from django.contrib.admin import site
from django.contrib.auth.views import LoginView
# from webauthn.helpers import register_webauthn_credential
# from webauthn.models import WebAuthnUser
from django_webauthn.helpers import generate_challenge, create_credential_options, verify_credential, generate_authentication_options, verify_assertion

class page_view_set(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = WebsiteSerializer

    # Header dropdowns
    about_dropdown = Page.objects.filter(show_in_header=True, header_dropdown='about').order_by('title')
    services_dropdown = Page.objects.filter(show_in_header=True, header_dropdown='services').order_by('title')
    more_dropdown = Page.objects.filter(show_in_header=True, header_dropdown='more').order_by('title')

    # Footer sections
    company_info = Page.objects.filter(show_in_footer=True, footer_section='company').order_by('title')
    resources = Page.objects.filter(show_in_footer=True, footer_section='resources').order_by('title')
    other = Page.objects.filter(show_in_footer=True, footer_section='other').order_by('title')

    def home(request):
        content = Page.objects.filter(slug='home')
        if len(content) <= 0:
            print("No home menu")
            # home(request)
            raise Http404("Page not found")
        else:
            content = content.all().values()[0]
            context = {
                'content': content
            }
            try:
                return HttpResponse(loader.get_template('home.html').render(context, request))
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return HttpResponse(loader.get_template('home.html').render(context, request))

    def template(request, slug):
        if slug == '500':
            return custom500()
        elif slug == '404':
            raise Http404("Page not found")
        content = Page.objects.filter(slug=slug)
        if len(content) <= 0:
            # home(request)
            raise Http404("Page not found")
        else:
            content = content.all().values()[0]
            context = {
                'content': content
            }
            return HttpResponse(loader.get_template('template.html').render(context, request))
        
    def search(request):
        if request.method == 'POST':
            # Retrieve the search query entered by the user
            search_query = request.POST['search_query']
            # Filter your model by the search query
            posts = Page.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query) | Q(header__icontains=search_query))
            for post in posts:
                post.content = re.sub(r'<.*?>', '', post.content)
            context = {'query':search_query, 'posts':posts}
            return HttpResponse(loader.get_template('search.html').render(context, request))
        else:
            return HttpResponse(loader.get_template('search.html').render({}, request))
        
    def site_map(request):
        posts = Page.objects.exclude(slug='404').exclude(slug='500').order_by('title')
        for post in posts:
            post.content = re.sub(r'<.*?>', '', post.content)
        context = {'posts':posts}
        return HttpResponse(loader.get_template('site-map.html').render(context, request))
    
def custom404(request, exception):
    content = Page.objects.filter(slug='404')
    content = content.all().values()[0]
    context = {
        'content': content
    }
    print(exception)
    return HttpResponseNotFound(loader.get_template('404.html').render(context, request))

def custom500(request):
    content = Page.objects.filter(slug='500')
    content = content.all().values()[0]
    context = {
        'content': content
    }
    # print(exception)
    return HttpResponseServerError(loader.get_template('404.html').render(context, request))

# 2FA Stuff that don't work yet...

class AdminLoginWebAuthnView(LoginView):
    template_name = 'admin/login.html'

def register_webauthn(request):
    if request.method == 'POST':
        credential_options = create_credential_options(
            rp_name='My Django App',
            rp_id='myapp.com',
            user_id=str(request.user.id),
            user_name=request.user.username,
            user_display_name=request.user.get_full_name(),
        )
        request.session['webauthn_challenge'] = credential_options['challenge']
        return render(request, 'register_webauthn.html', {'credential_options': credential_options})

def verify_registration(request):
    if request.method == 'POST':
        # Verify the challenge and create the WebAuthnCredential
        credential = verify_credential(
            request.POST['credential'],
            challenge=request.session.pop('webauthn_challenge'),
            rp_id='myapp.com',
        )
        if credential:
            UserWebAuthnCredential.objects.create(
                user=request.user,
                credential_id=credential.credential_id,
                public_key=credential.public_key,
                sign_count=credential.sign_count,
            )
            return redirect('success_url')
    return redirect('failure_url')

def login_webauthn(request):
    if request.method == 'POST':
        # Create the authentication options to pass to the browser
        auth_options = generate_authentication_options(
            rp_id='myapp.com',
            allowed_credentials=[{
                'id': cred.credential_id,
                'transports': ['usb', 'nfc', 'ble', 'internal'],
            } for cred in request.user.webauthn_credentials.all()],
        )
        request.session['webauthn_challenge'] = auth_options['challenge']
        return render(request, 'login_webauthn.html', {'auth_options': auth_options})

def verify_login(request):
    if request.method == 'POST':
        # Verify the WebAuthn credential assertion
        credential = verify_assertion(
            request.POST['assertion'],
            challenge=request.session.pop('webauthn_challenge'),
            rp_id='myapp.com',
        )
        if credential:
            # Log in the user (depends on your auth system)
            # You can use Django's built-in login function
            login(request, request.user)
            return redirect('success_url')
    return redirect('failure_url')

from django.urls import path
urlpatterns = [
    path('admin/login_webauthn/', AdminLoginWebAuthnView.as_view(), name='admin_login_webauthn'),
]