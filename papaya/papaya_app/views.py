from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Papaya, Task
import json

# Create your views here.

class Papayas(View):
    def get(self, request):
        return JsonResponse({'status': 'ok', 'papayas': list(Papaya.objects.values().all())})
    def post(self, request):
        our_data = json.loads(request.body.decode())
        print(our_data, type(our_data))
        return JsonResponse({'status': 'ok'})

class PapayaDetails(View):
    def get(self, request, papaya_id):
        return JsonResponse({'status': 'ok'})
    def put(self, request, papaya_id):
        return JsonResponse({'status': 'ok'})
    def delete(self, request, papaya_id):
        return JsonResponse({'status': 'ok'})

class Tasks(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'okay'})
