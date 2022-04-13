from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('citizen/', views.citizen, name = 'citizen'),
    path('otp/', views.otp, name = 'otp'),
    path('home/',views.home,name = 'home'),
    path('logout/',views.logout,name = 'logout'),
    path('password/',views.password,name = 'password'),
    path('edit-profile/',views.edit_profile,name = 'edit-profile'),
    path('view-profile/',views.view_profile,name = 'view-profile'),
    path('add-FIR/',views.add_FIR,name='add-FIR'),
    path('view-FIR/',views.view_FIR,name='view-FIR'),
    path('view-one-FIR/',views.view_one_FIR,name='view-one-FIR'),
    path('search-station/',views.search_station,name='search-station'),
    path('add-com/',views.add_com,name='add-com'),

]
