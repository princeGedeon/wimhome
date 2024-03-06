from django.urls import path

from startup import views

urlpatterns = [
    path('',views.home,name="home"),
    path('qui-sommes-nous/', views.about, name="about"),
    path('application/', views.application, name="application"),
    path('demarche-rse/', views.demarche, name="demarche"),
    path('nouveautes/', views.nouveaute, name="nouveaute"),
    path('media/', views.media, name="media"),
    path('contact-us/', views.contact, name="contact"),
    path('newsletter_save', views.newsletter_signup, name="new"),
    path('contacts_send', views.contact_send, name="sent"),
    path('mentions-legales/',views.mention,name="mention"),
    path('politique-de-confidentialités', views.politique, name="politique")


]
