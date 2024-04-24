from django.urls import path

from . import views
from . views import HomeView
from . views import AboutView
from . views import ProductView
from . views import ContactView
from . views import ServiceView
# your urls 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('product', ProductView.as_view(), name='product'),
    path('contact', ContactView.as_view(), name='contact'),
    path('service', ServiceView.as_view(), name='service'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]