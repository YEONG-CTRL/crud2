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

    def get(self, request):
        owners = Owners.objects.all()
        results = []

        for owner in owners:
            for owner_dog in owner.dogs_set.all():
                results.append(
                    {
                        "name" : owner.name,
                        "email" : owner.email,
                        "age"   : owner.age,
                        "owner's_dog" : owner_dog.name,
                        "owner's_dog_age": owner_dog.age,
                    }
                )    
        return JsonResponse({'results':results}, status=200)

                        # "owner's_dog": [
                        #     for i in owner.dogs_set.all():
                        #         {"dog_name":print(i.name),
                        #          "dog_age"  :print(i.age) 
                        #         ]
                        # }
              
        
        


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

    def get(self,request):
        dogs =Dogs.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name": dog.name,
                    "age": dog.age,
                    "owner":dog.owner.name,
                }
            )
        return JsonResponse({'results':results}, status=200)