from django.shortcuts import render
from django.views.generic import TemplateView

# def home_page(request):
#     return render(request, 'home_page/home.html')     


class HomePage(TemplateView):
    template_name = 'home_page/home.html' #DON'T forget in settings - TEMPLATES - set: 'DIRS': [BASE_DIR / 'templates'],
