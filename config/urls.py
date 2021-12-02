from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
