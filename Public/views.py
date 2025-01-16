from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from Shop .models import *
from Specialist.models import *
from .form import *
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
#                   <-----user interaction page------------->
class UserPage(View):
    def get(self,request):
        return render(request,'user/home.html')



 #                   <-----------user registration ----------->
class UserRegistration(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        details = user_form(request.POST)
        if details.is_valid():
            user = LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='USER'
            )
            public = details.save(commit=False)
            public.USER = user
            public.save()
            return HttpResponse('<script>alert("Registration successful!"); window.location.href="/public/home/";</script>')
        return render(request, 'user/register.html', {'form': details})

                           #<----------complaints------------->
class SubmitComplaintView(View):
    def get(self, request, *args, **kwargs):
        form = ComplaintForm()
        return render(request, 'user/submit_complaint.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if 'login_id' not in request.session:
            return redirect('Manager:login')
        user_id = request.session['login_id']
        user = get_object_or_404(LoginDetails, id=user_id)

        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.sender = user
            complaint.save()
            return HttpResponse(
                '<script>alert("Complaint submitted successfully!"); window.location.href="/homepage/";</script>')
        return render(request, 'user/submit_complaint.html', )

   #         <----------reply from admin------------------->
class ReplyView(View):
    def get(self,request):
        id=request.session.get('login_id')
        if not id:
            return redirect('Manager:login')
        content=Complaint.objects.filter(sender_id=id)
        for complaint in content:
            if not complaint.reply:
                complaint.reply="not replied yet"
        return render(request,'user/complaint_reply.html',{'replies':content})

          #<------------rating and feedback-------------->
class SubmitFeedback(View):
    def get(self, request):
        return render(request, 'user/submit_feedback.html')

    def post(self, request):
        user_id = request.session.get('login_id')
        if not user_id:
            return redirect('Manager:login')

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating:
            Feedback.objects.create(
                user_id=user_id,rating=int(rating),comment=comment
            )
            return HttpResponse(f"<script>alert('Thank you for the feedback and rating'); window.location.href='/public/userpage/';</script>")
        return render(request, 'user/submit_feedback.html', {'error': 'Please select a rating.'})

#        <---------------for viewing  all specialists---------------------->

class SpecialistList(View):
    def get(self, request):
        specialists = Specialist_Details.objects.select_related('key').all()
        return render(request, 'user/specialist_list.html', {'specials': specialists})


class ChatWithSpecialist(View):
    def get(self, request, specialist_id):
        user_id = request.session.get('login_id')
        if not user_id:
            return redirect('login')
        specialist = get_object_or_404(LoginDetails, id=specialist_id)
        print('ljsldjajdoaljdoajkl',specialist)
        messages = Message.objects.filter(
            Q(sender_id=user_id, receiver_id=specialist_id) |
            Q(sender_id=specialist_id, receiver_id=user_id)
        ).order_by('timestamp')
        return render(request, 'user/specialist_chat.html', {
            'messages': messages,
            'specialist_id': specialist_id,
            'user_id': user_id,
        })
    def post(self, request, specialist_id):
        user_id = request.session.get('login_id')
        if not user_id:
            return redirect('login')

        message_text = request.POST.get('message')
        if message_text:
            Message.objects.create(sender_id=user_id, receiver_id=specialist_id, message=message_text)

        return redirect('specialistchat', specialist_id=specialist_id)
    #               <------------shop view \product view----------->
class ViewShop(View):
    def get(self, request):
        data = Products.objects.all()
        return render(request, 'User/shop_page.html', {'datas': data})
    
class ProductView(View):
    def get(self,request,id):
        data=Products.objects.get(pk=id)
        return render(request,'user/product_view.html',{'log':data})


