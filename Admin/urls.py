from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-index/', views.admin_index,name='admin-index'),
    path('admin-login/',views.admin_login,name='admin-login'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
]