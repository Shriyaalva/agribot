import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO

# Load model once
model = load_model("models_ml/disease_model.h5")

CLASS_NAMES = [
    "Bacterial_leaf_blight",
    "Brown_spot",
    "Leaf_smut"
]

REMEDY = {
    "Bacterial_leaf_blight": "Use resistant varieties and proper drainage.",
    "Brown_spot": "Apply fungicide and avoid excess nitrogen.",
    "Leaf_smut": "Remove infected plants and use certified seeds."
}

@csrf_exempt
def disease_predict(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES["image"]

            # ✅ Convert Django file to BytesIO
            img_bytes = BytesIO(uploaded_file.read())

            img = image.load_img(img_bytes, target_size=(224, 224))
            img = image.img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            prediction = model.predict(img)
            index = np.argmax(prediction)
            disease = CLASS_NAMES[index]

            return JsonResponse({
                "disease": disease,
                "remedy": REMEDY[disease]
            })

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({
        "message": "Use POST method with image file"
    })
