import json

from django.views import View
from django.http  import JsonResponse


from products.models       import Actor, Actor_Movie, Movie

# Create your views here.
class ActorView(View):
    def post(self, request):
        data     = json.loads(request.body)

        actor     = Actor.objects.create(
            first_name    = data['firstname'],
            last_name     = data['lastname'],
            date_of_birth = data['birthday']
        )
        return JsonResponse({'messasge':'created'}, status=201)


    def get(self, request):
        #GET 127.0.0.1:8000/product
        actors = Actor.objects.all()
        print(f"actors objects :: {actors}")
        results = []

        for actor in actors:
            actors_movies = Actor_Movie.objects.filter(actor_id = actor.id)
            results.append(
                {
                    "id" : actor.first_name,
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "date_of_birth" : actor.date_of_birth,
                    "movies" : [{
                        "title" : actor_movie.movie.title,
                        "release_date" : actor_movie.movie.release_date,
                        "running_time" : actor_movie.movie.running_time
                    } for actor_movie in actors_movies]
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"actors and movies" :results}, status=200) 