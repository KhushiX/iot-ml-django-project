from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Your prediction logic
def predict_behavior(soil, ldr, time):
    # dummy prediction logic
    if soil < 50 and ldr > 200 and 6 <= time <= 18:
        return 1
    else:
        return 0

@csrf_exempt
def get_prediction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        soil = data.get('soil')
        ldr = data.get('ldr')
        time = data.get('time')
        prediction = predict_behavior(soil, ldr, time)
        return JsonResponse({'prediction': prediction})
    return JsonResponse({'error': 'Only POST method allowed'}, status=400)
