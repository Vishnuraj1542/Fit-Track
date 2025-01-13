from django.shortcuts import render,redirect,get_object_or_404
from Trainer.models import*
from Public.models import*
from Specialist.models import *
from Shop.models import *
from Trainer.forms import *
from Specialist.forms import *
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib import messages



# Create your views here.

                         # Trainer registration view
class TrainersRegistration(View):
    def get(self, request):
        return render(request, 'admin/trainer_register.html')

    def post(self, request):
        data = Trainer_Form(request.POST, request.FILES)
        if data.is_valid():
            details = LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='TRAINER',
                status='verified'
            )
            trainer = data.save(commit=False)
            trainer.key = details
            trainer.save()
            return HttpResponse('<script>alert("Trainer added successfully!"); window.location.href="/admin/home/";</script>')
        return render(request, 'admin/trainer_register.html', {'form': data})

                #Specialist Registration
class Specialist_Registration(View):
    def get(self, request):
        return render(request, 'admin/specialist_register.html')

    def post(self, request):
        details = Specialist_Form(request.POST, request.FILES)
        if details.is_valid():
            data = LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='NUTRI_SPECIALIST',
                status='verified'
            )
            specialist = details.save(commit=False)
            specialist.key = data
            specialist.save()
            return redirect('managespecialist')
        return render(request, 'admin/specialist_register.html', {'form': details})



        # manageshop view products edit products delete products
class ManageShop(View):
    def get(self,request):
        data=Products.objects.all()
        return render(request,'admin/shop_view.html',{'datas':data})

                # Post uploaded by the trainers
class TrainersPost(View):
    def get(self, request, trainer_id=None):
        trainer = None
        if trainer_id:
            trainer = TrainerRegistration.objects.filter(id=trainer_id, is_active=True).first()
            posts = Tutorials.objects.filter(is_active=True, lock=trainer).select_related('lock').order_by('-created_at') if trainer else []
        else:
            posts = Tutorials.objects.filter(is_active=True).select_related('lock').order_by('-created_at')
        return render(request, 'admin/trainer_post.html', {
            'media': posts,
            'trainer': trainer
        })
                      #Trainers suggestion view.

class ViewAllSuggestions(View):
    template_name = 'admin/view_all_suggestion.html'

    def get(self, request):
        suggestions = Suggestion.objects.all()
        suggestion_forms = [(suggestion, SuggestionReplyForm(instance=suggestion))
            for suggestion in suggestions
        ]
        return render(
            request,
            self.template_name,
            {'suggestion_forms': suggestion_forms}
        )
    def post(self, request):
        suggestion_id = request.POST.get('suggestion_id')
        suggestion = Suggestion.objects.get(pk=suggestion_id)
        form = SuggestionReplyForm(request.POST, instance=suggestion)

        if form.is_valid():
            form.save()
            return redirect('view_all_suggestions')
        suggestions = Suggestion.objects.all()
        suggestion_forms = [
            (suggestion, SuggestionReplyForm(instance=suggestion))
            for suggestion in suggestions
        ]
        return render(request,self.template_name,{'suggestion_forms': suggestion_forms})

                      # Verify User and Shopkeeper
class Verify(View):
    def get(self,request):
        user_status=LoginDetails.objects.filter(Q(user_type='USER') | Q(user_type='SHOPKEEPER'),status='pending')
        return render(request,'admin/verification.html',{'user_status':user_status})
    def post(self,request,id):
        user_data=get_object_or_404(LoginDetails,id=id)
        new_status=request.POST.get('status')
        other=['verified','rejected']
        if new_status not in other:
            messages.error(request,"status not changed")
            return redirect('verify')
        user_data.status=new_status
        user_data.save()
        messages.success(request,f"{user_data.username} profile {user_data.status} sucessfully")
        return redirect('verify')

                      #Manage status of trainer

class ManageTrainer(View):
    def get(self, request):
        data = LoginDetails.objects.filter(user_type='TRAINER')
        return render(request, 'admin/manage_trainer.html', {'item': data})

    def post(self, request, id):
        try:
            trainer = LoginDetails.objects.get(user_type='TRAINER', pk=id)
            trainer.is_active = request.POST.get('is_active') == 'true'
            trainer.save()
            messages.success(request, 'Status successfully changed.')
        except LoginDetails.DoesNotExist:
            messages.error(request, 'Trainer not found.')
        return redirect('managetrainer')


                        # (Add edit delete) Manage Trainer and Specialist
class TrainerView(View):
    def get(self, request):
        trainer_details = TrainerRegistration.objects.select_related('key').all()
        return render(request, 'admin/trainerdetails_view.html',{'details':trainer_details} )


class EditTrainer(View):
    def get(self, request, id):
        data = get_object_or_404(TrainerRegistration, pk=id)
        form = Trainer_Form(instance=data)
        return render(request, 'admin/trainer_edit.html', {'form': form, 'trainer': data})

    def post(self, request, id):
        data = get_object_or_404(TrainerRegistration, pk=id)
        form = Trainer_Form(request.POST, request.FILES, instance=data)
        if form.is_valid():
            updated_trainer = form.save(commit=False)
            details = LoginDetails.objects.filter(pk=data.key.pk).update(
                username=request.POST.get('username'),
                email=request.POST.get('email')
            )
            updated_trainer.save()
            return redirect('viewtrainers')
        return render(request, 'admin/trainer_edit.html', {'form': form, 'trainer': data})


                     #<---------specialist------------->


class SpecialistView(View):
    def get(self,request):
        data = Specialist_Details.objects.select_related('key').all()
        return render(request,'admin/specialistdetails_view.html',{'object':data})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

class EditSpecialist(View):
    def get(self, request, id):
        data = get_object_or_404(Specialist_Details, pk=id)
        form = Specialist_Form(instance=data)
        return render(request, 'admin/specialist_edit.html', {'datas': data, 'form': form})

    def post(self, request, id):
        data = get_object_or_404(Specialist_Details, pk=id)
        form = Specialist_Form(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('managespecialist')
        return render(request, 'admin/specialist_edit.html', {'form': form, 'datas': data})

class DeleteSpecialist(View):
    def get(self,request,id):
        data=get_object_or_404(Specialist_Details,pk=id)
        return render(request,'admin/confirmation.html',{'specialist':data})
    def post(self, request, id):
        try:
            data = get_object_or_404(Specialist_Details, pk=id)
            data.delete()
            redirect_url = reverse('managespecialist')
            return HttpResponse(
                f'<script>alert("Specialist deleted successfully."); window.location.href="{redirect_url}";</script>'
            )
        except Exception as e:
            redirect_url = reverse('managespecialist')
            return HttpResponse(
                f'<script>alert("Error deleting specialist: {str(e)}"); window.location.href="{redirect_url}";</script>'
            )

               # <-----------complaints from the users -------------------->

class ViewComplaintsView(View):
    def get(self, request, *args, **kwargs):
        complaints = Complaint.objects.filter(reply__isnull=True).order_by('-created_at')
        for complaint in complaints:
            print("jakjdljalj",complaint.complaint_text)

        return render(request, 'admin/view_complaints.html', {'complaints': complaints})

class ReplyComplaintView(View):
    def get(self, request, pk, *args, **kwargs):
        complaint = Complaint.objects.get(pk=pk)
        return render(request, 'admin/reply_complaint.html', {'complaint': complaint})

    def post(self, request, pk, *args, **kwargs):
        complaint = Complaint.objects.get(pk=pk)
        reply = request.POST.get('reply')
        if reply:
            complaint.reply = reply
            complaint.save()
            return redirect('view_complaints')
        return render(request, 'admin/view_complaints.html', {'complaint': complaint})


#    <-----------feedback from users----------->
class UserRating(View):
    def get(self,request):
        review=Feedback.objects.all()
        return render(request,'admin/view_feedback.html',{'reviews':review})
















