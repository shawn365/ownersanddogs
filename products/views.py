#from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class ProductsView(View):
    def post(self, request):
        data     = json.loads(request.body)

        owner     = Owner.objects.create(
            name    = data['ownername'],
            email   = data['email'],
            age     = data['ownerage']
        
        )
        dog = Dog.objects.create(
            name     = data['dogname'],
            age      = data['dogage'],
            owner_id = owner
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        #GET 127.0.0.1:8000/product
        dogs = Dog.objects.all()
        owners = Owner.objects.all()
        print(f"dogs objects :: {dogs}")

        results = []

        for dog in dogs:
            results.append(
                {
                    "dog_name" : dog.name,
                    "dog_age" : dog.age,
                    "owner_name" : dog.owner_id.name,
                    "owner_email" : dog.owner_id.email,
                    "owner_age" : dog.owner_id.age
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"dogs and owners" :results}, status=200) 


