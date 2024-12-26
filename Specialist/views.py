from django.shortcuts import render,redirect
from django.views import View
from Public .models import*
from Trainer .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
class UserView(View):
    def get(self, request):
        user_data = user_details.objects.all()
        return render(request, 'specialist/user_details.html', {'user_data': user_data})

class TrainingPost(View):
    def get(self, request, trainer_id=None):
        trainer = None
        if trainer_id:
            trainer = TrainerRegistration.objects.filter(id=trainer_id, is_active=True).first()
            posts = Tutorials.objects.filter(is_active=True, lock=trainer).select_related('lock').order_by('-created_at') if trainer else []
        else:
            posts = Tutorials.objects.filter(is_active=True).select_related('lock').order_by('-created_at')

        return render(request, 'specialist/manage_trainer.html', {
            'media': posts,
            'trainer': trainer
        })






