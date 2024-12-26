from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from Trainer.forms import *
from django.http import HttpResponse
from Specialist.forms import *
from Specialist.models import *
from Shop.models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib import messages
from Trainer.models import TrainerRegistration,Tutorials


# Create your views here.

                         # Trainer registration view
class TrainerRegistration(View):
    def get(self,request):
        return render(request,'admin/trainer_register.html')
    def post(self,request):
        data=Trainer_Form(request.POST,request.FILES)
        if data.is_valid():
            data.save(commit=False)
            details=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='TRAINER',
                status='verified'
            )
            data.key=details
            data.save()
            return HttpResponse ('trainer added sucessfully')
        return render(request,'admin/trainer_register.html')

                    #Specialist Registration
class Specialist_Registration(View):
    def get(self,request):
        return render(request,'admin/specialist_register.html')
    def post(self,request):
        details= Specialist_Form(request.POST,request.FILES)
        if details.is_valid():
            details.save(commit=False)
            data=LoginDetails.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                user_type='SPECIALIST',
                status = 'verified'
            )
            details.key=data
            details.save()
            return HttpResponse('specialist added sucessfully')
        return render(request,'admin/specialist_register.html')


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
        # Fetch trainers only
        data = LoginDetails.objects.filter(user_type='TRAINER')
        return render(request, 'admin/manage_trainer.html', {'item': data})

    def post(self, request, id):
        try:
            # Fetch the trainer with the given ID
            trainer = LoginDetails.objects.get(user_type='TRAINER', pk=id)
            # Update the is_active status
            trainer.is_active = request.POST.get('is_active') == 'true'
            trainer.save()
            messages.success(request, 'Status successfully changed.')
        except LoginDetails.DoesNotExist:
            # Handle case when trainer is not found
            messages.error(request, 'Trainer not found.')
        return redirect('managetrainer')



        # Manage Trainer and Specialist
class TrainerView(View):
    def get(self, request):
        trainer_details = TrainerRegistration.objects.all()

        # print(trainer_details)
        return render(request, 'admin/trainerdetails_view.html', )


class ManageSpecialist(View):
    def get(self,request):
        data = Specialist_Details.objects.select_related('key')
        return render(request,'admin/manage_specialist.html',{'object':data})

























