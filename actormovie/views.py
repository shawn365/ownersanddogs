import json

from django.views import View
from django.http  import JsonResponse

from products.models       import Actor_Movie
# Create your views here.
class ActorMovieView(View):
    def post(self, request):
        data     = json.loads(request.body)

        actor_movie     = Actor_Movie.objects.create(
            actor_id = data['actor_id'],
            movie_id = data['movie_id']
        )
        return JsonResponse({'messasge':'created'}, status=201)
