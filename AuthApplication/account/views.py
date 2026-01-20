from django.shortcuts import render,redirect
from django.views import View
from account.forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def send_otp(user_instance):
    user_instance.generate_otp()
    # send email
    send_mail(
        subject="Django App Authentication OTP",
        message=f"Your Generated OTP is : {user_instance.otp}",
        from_email="vishnuprasadm666@gmail.com",
        recipient_list=[user_instance.email],
        fail_silently=True
    )
    # send phone

class LandingPageView(View):
    def get(self,request):
        return render(request,'landingpage.html')

class SignUpView(View):
    def get(self,request):
        form=UserForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request,**kwargs):
        form_data=UserForm(data=request.POST)
        if form_data.is_valid():
            user=form_data.save(commit=False)
            user.is_active=False
            user.save()
            send_otp(user)
            return redirect('otpverify')
        messages.warning(request,"invalid input recieved")
        return render(request,'signup.html',{'form':form_data})

class OtpVerificationView(View):
    def get(self,request):
        return render(request,'otp_verify.html')
    def post(self,request):
        otpval=request.POST.get('otpnum')
        try:
            user_instance=User.objects.get(otp=otpval)
            user_instance.is_verified=True
            user_instance.is_active=True
            user_instance.otp=None
            user_instance.save()
            messages.success(request,'SignUp Succcessfull')
            return redirect('login')
        except:
            messages.warning(request,'wrong OTP entered')
            return redirect('otpverify')
    
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{'form':form})

    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('home')
            else:
                messages.warning(request,"Invalid Username or Password")
                return redirect('login')
        messages.error(request,"Invalid Input Recieved!!")
        return render(request,"login.html",{"form":form_data})
    
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class ProfileView(View):
    def get(self,request,**kwargs):
        form=ProfileForm(instance=request.user.userprofile)
        return render(request,'profile.html',{'form':form}) 
    
    def post(self,request,*kwargs):
        form_data=ProfileForm(data=request.POST,files=request.FILES,instance=request.user.userprofile)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Profile Updated")
            return redirect('home')
        return render(request,'profile.html',{'form':form_data})
    
class LogoutView(View):
    def get(self,request,**kwargs):
        logout(request)
        messages.success(request,"User Logged Out!")
        return redirect('login')
