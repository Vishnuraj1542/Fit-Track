from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages
from .models import *
from django.views import View
# Create your views here.

class HomePage(View):
    def get(self,request):
        return render(request,'user/home.html')
    
class ShopPage(View):
    def get(self,request):
        return render(request,'shop/homepage.html')

class Trainer_Page(View):
    def get(self,request):
        return render(request,'trainer/homepage.html')
    
class Specialist_Page(View):
    def get(self,request):
        return render(request,'specialist/homepage.html')


class login_page(View):
    def get(self,request):
        return render(request,'manager/login.html')
    def post(self,request):
        user_type=""
        response_dict={'sucess':False}
        landing_page_url={
            "USER":"Manager:homepage",
            "SHOPKEEPER":"Manager:shoppage",
            "TRAINER":"Manager:trainerpage",
            "SPECIALIST":"Manager:Specialist_Page",
        }
        username=request.POST.get('username')
        password=request.POST.get('password')
        authenticated = authenticate(username=username,password=password)
        try:
            user = LoginDetails.objects.get(username=username)

        except LoginDetails.DoesNotExist:
            response_dict[
                            "reason"
                        ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "user:login")

        else:

            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                        user=user, defaults={"session_dict": json.dumps(session_dict)}
                        )

            user_type = authenticated.user_type

            request.session["data"] = {
                            "user_id": user.id,
                            "user_type": user.user_type,
                            "token": token.key,
                            "username": user.username,
                            "status": user.is_active,
                        }
            request.session["user"] = authenticated.username
            request.session["token"] = token.key
            request.session["status"] = user.is_active
            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or loadlogin)