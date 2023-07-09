from django.urls import  path
from . import views

urlpatterns = [
    path('',views.register,name='reg'),
    path('log/',views.sign,name='login'),
    path('logout/',views.logout,name='logout'),
    path('booking/',views.book,name='booking')
]
