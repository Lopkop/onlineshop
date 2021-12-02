from django.urls import path

from .views import HomePageView, FeedbackPageView, ThanksPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('feedback/', FeedbackPageView.as_view(), name='feedback'),
    path('thanks-for-your-feedback/', ThanksPageView.as_view(), name='thanks_for_feedback'),
]
