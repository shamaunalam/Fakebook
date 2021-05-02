from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('update/',views.update,name='update')
]


