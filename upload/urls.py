from django.urls import path
from .views import meeting_list, upload_document

app_name = 'upload'

urlpatterns = [
    path('uploads/', meeting_list, name='upload-list'),
    path('add/', upload_document, name='upload'),
]
