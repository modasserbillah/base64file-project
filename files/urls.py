from django.urls import path

from .views import HomePageView, UploadFileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('file/', UploadFileView.as_view(), name='add_file')
]
