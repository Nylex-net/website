from dataclasses import fields
from rest_framework import serializers
from .models import Page
 
# create a serializer
class WebsiteSerializer(serializers.Serializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Page
        fields = ('title', 'description', 'slug', 'header', 'banner', 'content', 'show_in_header', 'header_dropdown', 'show_in_footer', 'footer_section')