from django.core.management.base import BaseCommand
from App.models import Page

class Command(BaseCommand):
    help = 'Create default objects'

    HOME_CONTENT = """
        <p class="reveal">We are a solution provider for any of your technological needs.&nbsp; We provide a wide range of services.</p>

        <div class="row reveal" style="padding-top:50px;padding-bottom:50px;">
        <div class="col-lg-4">
        <div class="card" style="width: 100%;"><a href="/faq"><img alt="Finger touching tablet with question marks." class="card-img-top" src="/static/media/huh.png" /></a>

        <div class="card-body">
        <h3 class="card-text text-center">FAQ</h3>

        <p class="card-text text-center">No worries, we&#39;re here to help.</p>

        <p class="card-text"><a href="/faq">Learn More</a></p>
        </div>
        </div>
        </div>

        <div class="col-lg-4">
        <div class="card" style="width: 100%;"><a href="/contact"><img alt="3D map pin." class="card-img-top" src="/static/media/Maplocation.png" /></a>

        <div class="card-body">
        <h3 class="card-text text-center">Location</h3>

        <p class="card-text text-center">We are located in Eureka, California.</p>

        <p class="card-text"><a href="/contact">Learn More</a></p>
        </div>
        </div>
        </div>

        <div class="col-lg-4">
        <div class="card" style="width: 100%;"><a href="/contact"><img alt="Nylex.net's open sign." class="card-img-top" src="/static/media/NylexOpen.png" /></a>

        <div class="card-body">
        <h3 class="card-text text-center">Business Hours</h3>

        <p class="card-text text-center">Monday - Friday, 8PM - 5PM</p>

        <p class="card-text"><a href="/contact">Learn More</a></p>
        </div>
        </div>
        </div>
        </div>

        <h2 class="text-center">What We Do?</h2>

        <div class="row reveal" style="padding-top:50px;padding-bottom:50px;">
        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Cabling</h5>

        <p class="card-text text-center">Connecting you to the world.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Tech Support</h5>

        <p class="card-text text-center">Help with your tech needs.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Network Management</h5>

        <p class="card-text text-center">Configure networks to connect properly.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Device Setups</h5>

        <p class="card-text text-center">Getting your workspace all setup.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Desktops</h5>

        <p class="card-text text-center">Creating workspaces for your needs.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Security</h5>

        <p class="card-text text-center">Keeping you on the safe side.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Software Development</h5>

        <p class="card-text text-center">Custom applications just for you.</p>
        </div>
        </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">NVR</h5>

        <p class="card-text text-center">I don&#39;t know what this means...</p>
        </div>
        </div>
        </div>
        </div>

        <h2 class="text-center">Partners and Resellers</h2>

        <div class="row reveal" style="padding-top:50px;padding-bottom:50px;">
        <div class="col-md-6 col-lg-3">
        <div class="card" style="width: 100%; height: 100%; align-items: center; justify-content: space-around; padding-top:20px; padding-bottom:20px;"><a href="https://www.microsoft.com/"><img alt="Microsoft Partner Logo" class="card-img-top" src="/static/media/Microsoft-Partner.jpg" /></a></div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card" style="width: 100%; height: 100%; align-items: center; justify-content: space-around; padding-top:20px; padding-bottom:20px;"><a href="https://www.lenovo.com/"><img alt="Lenovo Business Partner Logo" class="card-img-top" src="/static/media/lenovo-business-partner-logo.png" /></a></div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card" style="width: 100%; height: 100%; align-items: center; justify-content: space-around; padding-top:20px; padding-bottom:20px;"><a href="https://www.grandstream.com/"><img alt="Grandstream Certified Reseller Logo" class="card-img-top" src="/static/media/Grandstream_certified_reseller_logo_new.png" /></a></div>
        </div>

        <div class="col-md-6 col-lg-3">
        <div class="card" style="width: 100%; height: 100%; align-items: center; justify-content: space-around; padding-top:20px; padding-bottom:20px;"><a href="https://www.ibm.com/"><img alt="IBM Business Partner Logo" class="card-img-top" src="/static/media/IBM-Business-Partner-Mark.webp" /></a></div>
        </div>
        </div>
        """
    
    def handle(self, *args, **kwargs):
        # Check if the default objects exist, create them if they do not
        if not Page.objects.filter(slug='home').exists():
            Page.objects.create(tile='Home',
                                description='Nylex.net is a technology solution provider based in Eureka, California.',
                                slug='home',
                                header='Outsource from Humboldt',
                                banner='media/TransLex.png',
                                content=self.HOME_CONTENT)
            self.stdout.write(self.style.SUCCESS('Successfully created default objects'))
        else:
            self.stdout.write(self.style.SUCCESS('Default objects already exist'))