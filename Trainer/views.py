from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import HttpResponse
from Public .models import*
from Manager.models import LoginDetails
from .forms import*
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
                          #view all users
class UserView(LoginRequiredMixin,View):
    def get(self,request):
        user_data = user_details.objects.all()
        return render(request, 'trainer/user_details.html', {'user_data': user_data})

                       #Add post
class AddPost(View):
    def get(self, request):
        return render(request, 'trainer/tutorials.html')
    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('Manager:login')
        try:
            login = LoginDetails.objects.get(id=request.session['login_id'])
            trainer = TrainerRegistration.objects.filter(key=login).first()
            if not trainer:
                messages.error(request, 'You are not authorized to upload a tutorial.')
                return redirect('Manager:login')
        except LoginDetails.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('Manager:login')
        video = TutorialForm(request.POST, request.FILES)
        if video.is_valid():
            c = video.save(commit=False)
            c.lock = trainer
            c.connect = login
            c.save()
            messages.success(request, 'Video added successfully.')
            return redirect('viewpost')
        else:
            messages.error(request, 'Unable to upload video. Please try again.')
        return render(request, 'trainer/tutorials.html')

                           #Viewposts
class ViewPost(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Tutorials.objects.filter(connect=content)
        except LoginDetails.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'trainer/media_view.html', {'content': content_media})

                              #Delete Posts

class DeletePost(LoginRequiredMixin, View):
    def get(self, request, id):
        item = get_object_or_404(Tutorials, id=id)
        return render(request, 'trainer/confirmation.html')
    def post(self, request, id):
        item = get_object_or_404(Tutorials, id=id)
        item.delete()
        messages.success(request, 'Video deleted successfully.')
        return redirect('viewpost')


                       #Edit Post
class EditPost(View):
    def get(self,request,id):
        items=get_object_or_404(Tutorials,pk=id)
        return render(request,'trainer/media_edit.html',{'item':items})
    def post(self,request,id):
        items=get_object_or_404(Tutorials,pk=id)
        item=TutorialForm(request.POST,request.FILES,instance=items)
        if item.is_valid():
            data=item.save(commit=False)
            data.connect = LoginDetails.objects.get(id=request.session['login_id'])
            data.save()
            messages.success(request,'Video edited sucessfully')
            return redirect('viewpost')
        return render(request,'trainer/edit_page.html',{'item':items})

                        #suggestion to admin

class SuggestionView(View):
    template_name = 'trainer/submit_suggestion.html'
    def get(self, request, *args, **kwargs):
        form = SuggestionForm()
        suggestions = Suggestion.objects.filter(
            sender=LoginDetails.objects.get(id=request.session['login_id'])
        ).order_by('-created_at')
        return render(request, self.template_name, {'form': form, 'suggestions': suggestions})
    def post(self, request, *args, **kwargs):
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.sender = LoginDetails.objects.get(id=request.session['login_id'])
            suggestion.save()
            return redirect('submit_suggestion') 
        suggestions = Suggestion.objects.filter(
            sender=LoginDetails.objects.get(id=request.session['login_id'])
        ).order_by('-created_at')
        return render(request, self.template_name, {'form': form, 'suggestions': suggestions})
