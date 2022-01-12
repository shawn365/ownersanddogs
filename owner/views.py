import json

from django.views import View
from django.http  import JsonResponse

from products.models      import Owner, Dog
# Create your views here.
class OwnerView(View):
    def post(self, request):
        data     = json.loads(request.body)

        owner     = Owner.objects.create(
            name    = data['ownername'],
            email   = data['email'],
            age     = data['ownerage']
        
        )
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        #GET 127.0.0.1:8000/product
        owners = Owner.objects.all()
        print(f"owners objects :: {owners}")

        results = []

        for owner in owners:
            results.append(
                {
                    "id" : owner.id,
                    "name" : owner.name,
                    "age" : owner.age,
                    "email" : owner.email,
                    "dogs" :[{
                        "id" : dog.id,
                        "name" : dog.name,
                        "age" : dog.age
                    } for dog in owner.dog_set.all()]
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"owners" :results}, status=200)