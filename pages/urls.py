from django.urls import path

from .views import home, process_image

urlpatterns = [
    path('', home, name='home'),
    path('process-image/', process_image, name='process_image'),
]