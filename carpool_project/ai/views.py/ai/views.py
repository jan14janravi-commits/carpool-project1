# ai/views.py
from django.http import JsonResponse

def suggest_ride(request):
    user_location = request.GET.get('location')
    # AI logic (example)
    suggestions = ["Car A near you", "Car B - 5 mins away"]
    return JsonResponse({'suggestions': suggestions})
