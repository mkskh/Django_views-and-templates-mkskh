from django.urls import reverse 
from django import template


register = template.Library()

@register.filter
def linkable_section(section_name):
    if section_name:
        
        section_url = reverse('notes:by_section', args=[section_name])
        return f"<a href='{section_url}'>{section_name}</a>"
    else:
        return ""