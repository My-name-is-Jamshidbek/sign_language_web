import cv2
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid

from signlang.settings import signToTxt


# from .regenerate_module import regenerate


def home(request):
    return render(request, 'pages/home.html')


@csrf_exempt
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
            # Read the image from the temporary file
            frame = cv2.imread(temp_path)

            # Ensure the frame is read correctly
            if frame is None:
                return JsonResponse({'error': 'Unable to process the uploaded image'}, status=400)

            # Process the image using SignToTXT
            predicted_characters = signToTxt.frame_to_txt(frame)

            # Return the predicted characters
            return JsonResponse({'predicted_characters': predicted_characters})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        finally:
            # Clean up the temporary file
            if default_storage.exists(temp_path):
                default_storage.delete(temp_path)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)