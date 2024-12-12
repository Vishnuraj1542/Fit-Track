from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import HttpResponse
from Public .models import*
from .forms import*

# Create your views here.
class UserView(View):
    def get(self,request):
        user_data = user_details.objects.all()
        return render(request, 'trainer/user_details.html', {'user_data': user_data})

class AddPost(View):
    def get(self,request):
        return render(request,'trainer/tutorials.html')
    def post(self,request):
        video=TutorialForm(request.POST,request.FILES)
        if video.is_valid():
            c=video.save(commit=False)
            c.connect=LoginDetails.objects.get(id=request.session['login_id'])
            c.save()
            return HttpResponse('''<script>alert("videos added sucessfully");window.location="{% url 'viewpost' %}"</script>''')
        return render(request,'trainer/tutorial.html')
    

class ViewPost(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Tutorials.objects.filter(connect=content)
        except LoginDetails.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'trainer/media_view.html', {'content': content_media})

class DeletePost(View):
    def get(self,request,id):
        item=get_object_or_404(Tutorials,id=id)
        return HttpResponse('''<script>alert("delete post")</script>''')
    def post(self,request,id):
        item=get_object_or_404(Tutorials,id=id)
        item.delete()
        return HttpResponse('''<script>alert("sucessfully deleted");location''')

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
            return HttpResponse('''<script>alert("Edited sucessfully");window.location="{% url 'viewpost' %}"</script>''')
        return render(request,'trainer/edit_page.html',{'item':items})