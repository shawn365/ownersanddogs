import json

from django.http   import JsonResponse
from django.views  import View

from products.models       import Dog

# Create your views here.
class DogView(View):
    def post(self, request):
        data     = json.loads(request.body)

        dog = Dog.objects.create(
            name     = data['dogname'],
            age      = data['dogage'],
            owner_id = data['owner_id']
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        #GET 127.0.0.1:8000/product
        dogs = Dog.objects.all()
        print(f"dogs objects :: {dogs}")

        results = []

        for dog in dogs:
            results.append(
                {
                    "id" : dog.id,
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" :{
                        "id" : dog.id,
                        "name" : dog.owner.name,
                        "owner_email" : dog.owner.email,
                        "owner_age" : dog.owner.age
                    }
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"dogs" :results}, status=200) 
