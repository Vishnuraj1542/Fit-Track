from django.shortcuts import render,redirect
from django.views import View
from .models import*
from Public .models import*
from Trainer .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
          #<-------------view users ------------>
class UserView(View):
    def get(self, request):
        user_data = user_details.objects.all()
        return render(request, 'specialist/user_details.html', {'user_data': user_data})

          #<-----------posts by the trainers -------------->
class TrainingPost(View):
    def get(self, request, trainer_id=None):
        trainer = None
        if trainer_id:
            trainer = TrainerRegistration.objects.filter(id=trainer_id, is_active=True).first()
            posts = Tutorials.objects.filter(is_active=True, lock=trainer).select_related('lock').order_by('-created_at') if trainer else []
        else:
            posts = Tutorials.objects.filter(is_active=True).select_related('lock').order_by('-created_at')

        return render(request, 'specialist/media.html', {
            'media': posts,
            'trainer': trainer
        })


#            <--------------chat from the users --------------------->

# views.py for the specialist app
class UsersListChat(View):
    def get(self, request):
        specialist_id = request.session.get('login_id')
        if not specialist_id:
            return redirect('Manager:login')

        # Get all messages involving the specialist
        user_ids = Message.objects.filter(
            Q(sender_id=specialist_id) | Q(receiver_id=specialist_id)
        ).values_list('sender_id', 'receiver_id')

        # Extract unique user IDs excluding the specialist's ID
        unique_user_ids = {uid for ids in user_ids for uid in ids if uid != specialist_id}

        # Fetch user objects
        users = User.objects.filter(id__in=unique_user_ids)

        return render(request, 'specialist/users_list_chat.html', {'users': users})




class ChatWithUser(View):
    def get(self, request, user_id):
        specialist_id = request.session.get('login_id')
        if not specialist_id:
            return redirect('Manager:login')

        # Fetch messages between the specialist and the specific user
        messages = Message.objects.filter(
            sender_id=specialist_id, receiver_id=user_id
        ) | Message.objects.filter(
            sender_id=user_id, receiver_id=specialist_id
        ).order_by('timestamp')

        return render(request, 'specialist/user_chat.html', {'messages': messages, 'user_id': user_id})

    def post(self, request, user_id):
        specialist_id = request.session.get('login_id')
        print("kjasdk",specialist_id)
        if not specialist_id:
            return redirect('Manager:login')



        message_text = request.POST.get('message')
        if message_text:
            Message.objects.create(sender_id=specialist_id, receiver_id=user_id, message=message_text)

        return redirect('user_chat', user_id=user_id)





