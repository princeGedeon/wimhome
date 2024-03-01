from django.urls import path

from startup import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('application/', views.application, name="application"),
    path('demarche-rse/', views.demarche, name="demarche"),
    path('nouveautes/', views.nouveaute, name="nouveaute"),
    path('media/', views.media, name="media"),
path('contact-us/', views.contact, name="contact"),
    path('newsletter_save', views.newsletter_signup, name="new")


]
