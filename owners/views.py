import json

#from django.shortcuts import render
from django.http   import JsonResponse
from django.views import View
#from flask           import request

from owners.models import Owners,Dogs

# Create your views here.
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owners.objects.create(
            name  = data['owner'],
            email  = data['email'],
            age    = data['age'],       
            )
        '''
        dog = Dogs.objects.create(
            owner  = owner
            name  = data['dog'],
            age    = data['dog_age']    
            )  
        '''      
        return JsonResponse({'message':'created'}, status=201) # 201 created

class DogsView(View):
    def post(self,request):
        data = json.loads(request.body)
        owner = Owners.objects.get(id=data['owner_id'])
        Dogs.objects.create(
            id = data['id'],
            owner_id = owner.id ,  # owner=owner 이렇게 넣으려면? 
            name  = data['dog'],
            age    = data['dog_age']    
            )
        return JsonResponse({'message':'created'}, status=201) # 201 created