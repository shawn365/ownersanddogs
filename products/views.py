#from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog, Actor_Movie, Actor, Movie

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
            owner_id = owner.id
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
                    "owner_name" : dog.owner.name,
                    "owner_email" : dog.owner.email,
                    "owner_age" : dog.owner.age
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"dogs and owners" :results}, status=200) 

    def post(self, request):
        data     = json.loads(request.body)

        actor     = Actor.objects.create(
            first_name    = data['firstname'],
            last_name     = data['lastname'],
            date_of_birth = data['birthday']
        )
        movie = Movie.objects.create(
            title        = data['title'],
            release_date = data['releasedate'],
            running_time = data['runningtime']
        )
        actor_movie = Actor_Movie.objects.create(
            actor_id = actor.id,
            movie_id = movie.id        
        )
        return JsonResponse({'messasge':'created'}, status=201)


    def get(self, request):
        #GET 127.0.0.1:8000/product
        actors_movies = Actor_Movie.objects.all()
        print(f"actors_movies objects :: {actors_movies}")

        results = []

        for actor_movie in actors_movies:
            results.append(
                {
                    "first_name" : actor_movie.actor.first_name,
                    "last_name" : actor_movie.actor.last_name,
                    "date_of_birth" : actor_movie.actor.date_of_birth,
                    "title" : actor_movie.movie.title,
                    "release_date" : actor_movie.movie.release_date,
                    "running_time" : actor_movie.movie.running_time
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"actors and movies" :results}, status=200) 



