from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-index/', views.admin_index,name='admin-index'),
    path('admin-login/',views.admin_login,name='admin-login'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
    path('admin-view-FIR/',views.admin_view_FIR,name='admin-view-FIR'),
    path('admin-view-one-FIR/<int:pk>',views.admin_view_one_FIR,name='admin-view-one-FIR'),
    path('admin-station/',views.admin_station,name='admin-station'),
    path('admin-one-station/<int:pk>',views.admin_one_station,name='admin-one-station'),
    path('admin-user/',views.admin_user,name='admin-user'),
    path('admin-one-user/<int:pk>',views.admin_one_user,name='admin-one-user'),
    path('admin-inspector/',views.admin_inspector,name='admin-inspector'),
    path('admin-one-ins/<int:pk>',views.admin_one_ins,name='admin-one-ins'),
    path('admin-subins/',views.admin_subins,name='admin-subins'),




]