from django.urls import path
from . import views
urlpatterns = [
    path('ins-login/', views.ins_login,name='ins-login'),
    path('ins-index/',views.ins_index,name='ins-index'),
    path('ins-view-FIR/',views.ins_view_FIR,name='ins-view-FIR'),
    path('ins-view-one-FIR/<int:pk>',views.ins_view_one_FIR,name='ins-view-one-FIR'),

    
]