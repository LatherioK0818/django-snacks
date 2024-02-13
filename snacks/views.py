from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'snacks/home.html'

class AboutPageView(TemplateView):
    template_name = 'snacks/about.html'
