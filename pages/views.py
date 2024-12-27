from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = "pages/home.html"

class AboutPageVeiw(TemplateView):
  template_name = "pages/about.html"
