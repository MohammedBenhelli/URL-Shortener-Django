from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from short.views import root, index, post

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('postUrl/', post, name='post'),
    path('<str:url_hash>/', root, name='root'),
    path('', index, name='index'),
]