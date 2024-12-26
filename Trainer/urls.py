from django.urls import path
from .views import*

urlpatterns=[
    path('viewusers/',UserView.as_view(),name='viewstudents'),
    path('addmedias/',AddPost.as_view(),name='addpost'),
    path('viewmedias/',ViewPost.as_view(),name='viewpost'),
    path('deletemedia/<int:id>/',DeletePost.as_view(),name='deletepost'),
    path('editmedia/<int:id>/',EditPost.as_view(),name='editpost'),
    path('submit-suggestion/', SuggestionView.as_view(), name='submit_suggestion'),
]