from django.shortcuts import render,redirect
from django.views import View
from Public .models import*

# Create your views here.
class UserView(View):
    def get(self, request):
        user_data = user_details.objects.all()
        return render(request, 'specialist/user_details.html', {'user_data': user_data})
