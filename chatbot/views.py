import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "").lower()

        # Intent detection
        if any(word in message for word in ["crop", "grow", "plant", "recommend"]):
            return JsonResponse({
                "reply": "Please enter soil details in the crop recommendation form."
            })

        elif any(word in message for word in ["disease", "leaf", "spot", "infected"]):
            return JsonResponse({
                "reply": "Please upload a leaf image in the disease prediction section."
            })

        elif any(word in message for word in ["soil", "ph", "nutrient"]):
            return JsonResponse({
                "reply": "Healthy soil should have balanced NPK values and pH between 5.5 to 7.5."
            })

        elif any(word in message for word in ["hello", "hi", "hey"]):
            return JsonResponse({
                "reply": "Hello! I am AgriBot. How can I help you today?"
            })

        else:
            return JsonResponse({
                "reply": "I can help with crop recommendation and disease detection."
            })

    return JsonResponse({"reply": "Use POST method"})
