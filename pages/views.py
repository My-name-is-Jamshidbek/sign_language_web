from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid
# from .regenerate_module import regenerate


def home(request):
    return render(request, 'pages/home.html')


@csrf_exempt  # Alternatively, ensure CSRF token is handled correctly
def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Save the uploaded image to a temporary location
        temp_filename = f"temp_{uuid.uuid4()}.png"
        temp_path = os.path.join(settings.MEDIA_ROOT, temp_filename)
        with default_storage.open(temp_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        try:
            # Call your regenerate function
            # regenerated_image_name = regenerate(temp_path)  # Ensure this returns the path to the regenerated image
            regenerated_image_name = temp_filename  # Ensure this returns the path to the regenerated image
            regenerated_image_path = f"media/{regenerated_image_name}"
            return JsonResponse({'regenerated_image_url': regenerated_image_path})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        # finally:
        #     # Clean up the temporary file
        #     if default_storage.exists(temp_path):
        #         default_storage.delete(temp_path)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)