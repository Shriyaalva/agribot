import pickle
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

with open("models_ml/crop_model.pkl", "rb") as f:
    crop_model = pickle.load(f)

with open("models_ml/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)
@csrf_exempt
def crop_predict(request):
    if request.method == "POST":
        try:
            data = request.POST

            features = np.array([[
                float(data["N"]),
                float(data["P"]),
                float(data["K"]),
                float(data["temperature"]),
                float(data["humidity"]),
                float(data["ph"]),
                float(data["rainfall"])
            ]])

            prediction = crop_model.predict(features)[0]
            crop_name = label_encoder.inverse_transform([prediction])[0]

            return JsonResponse({"recommended_crop": crop_name})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    # 👇 HANDLE GET REQUEST
    return JsonResponse({
        "message": "Use POST method with crop parameters"
    })
