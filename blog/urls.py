from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog,name = 'blog-home'),
    path('blogpost/<str:slug>',views.blogpost,name='blog-blogpost'),
    path('contact/',views.contact,name = 'blog-contact'),
    path('search/',views.search,name = 'blog-search'),
    path('about/',views.about,name='blog-about'),
   
   
    

]
