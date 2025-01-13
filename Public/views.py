from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from Specialist.models import *
from .form import *
from django.urls import reverse
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
            print("kajl;sdj",login_id)
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
        specialists = Specialist_Details.objects.all()
        return render(request, 'user/specialist_list.html', {'specialists': specialists})
