from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('signup/', views.signup, name='signup'),
]
