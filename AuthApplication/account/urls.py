from django.urls import path
from account.views import *


urlpatterns=[
    path('signup',SignUpView.as_view(),name='signup'),
    path('otpverify',OtpVerificationView.as_view(),name='otpverify'),
    path('login',LoginView.as_view(),name='login'),
    path('home',HomeView.as_view(),name='home'),
    path('profile',ProfileView.as_view(),name='profile'),
    path('logout',LogoutView.as_view(),name='logout')
]