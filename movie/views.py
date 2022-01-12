import json

from django.views import View
from django.http  import JsonResponse

from products.models       import Movie, Actor_Movie, Actor

class MovieView(View):
    def post(self, request):
        data     = json.loads(request.body)

        movie = Movie.objects.create(
            title        = data['title'],
            release_date = data['releasedate'],
            running_time = data['runningtime']
        )

        return JsonResponse({'messasge':'created'}, status=201)


    def get(self, request):
        #GET 127.0.0.1:8000/product
        movies = Movie.objects.all()
        print(f"movies objects :: {movies}")
        results = []

        for movie in movies:
            actors_movies = Actor_Movie.objects.filter(movie_id = movie.id)
            results.append(
                {
                    "id" : movie.id,
                    "title" : movie.title,
                    "release_date" : movie.release_date,
                    "running_time" : movie.running_time,
                    "actors" : [{
                        "first_name" : actor_movie.actor.first_name,
                        "last_name" : actor_movie.actor.last_name,
                        "date_of_birth" : actor_movie.actor.date_of_birth
                    } for actor_movie in actors_movies]
                }
            )

        print(f"results objects :: {results}")

        return JsonResponse({"movies" :results}, status=200) 