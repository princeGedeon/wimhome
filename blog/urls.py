from django.urls import path

from blog import views

urlpatterns = [
    path("",views.blog_view,name="blog_list"),
    path("<str:slug>",views.blog_view_unique,name="blog_unique"),


]
