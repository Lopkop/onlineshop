from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class FeedbackPageView(FormView):
    form_class = ContactForm
    template_name = 'pages/feedback.html'
    success_url = reverse_lazy('thanks_for_feedback')


class ThanksPageView(TemplateView):
    template_name = 'pages/thanks.html'
