from django.urls import path
from django.conf.urls import url
from example import views
from .views import Index, AboutPageView, DataPageView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),    
    path('home/', Index.as_view(), name='homepage'),    
    path('about/', AboutPageView.as_view(), name='about'),
    url('data/', DataPageView.as_view(), name='data'),
]
