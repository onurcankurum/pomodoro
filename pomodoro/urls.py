
from django.contrib import admin
from django.urls import path,include
from .views import home,Hometest,Statistics
from accounts.views import login_view ,register
from allauth.account.views import login

urlpatterns = [
    path('register/', register,name='register'),
    path('accounts/login/',login,name="account_login"),
     path('hometest/',Hometest.as_view()),
    path('home/', home,name='ev'),
    path('statistics/',Statistics.as_view(),name='statistics'),
   
    path('admin/', admin.site.urls),
    
    path('accounts/', include('allauth.urls')),

]

