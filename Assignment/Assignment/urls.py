
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

from RestAPIs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('user/register/', views.addUser),
    path('admin2/advisor/', views.addAdvisor),
    path("user/<str:uID>/advisor", views.getAdvisors),
    path('user/<str:usid>/advisor/<str:advid>/', views.bookAdvisor, name='book-advisor'),
    path('users/<str:uId>/advisor/booking/', views.getBookings),
    path('user/login', views.login),
]

