from django.urls import path , include
from home.views import index, Person_view, login , PersonAPI , PeopleViewSet , RegisterAPI
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('people' , PeopleViewSet, basename='people')
urlpatterns = router.urls

urlpatterns = [
    path('' , include(router.urls)),
    path('register/', RegisterAPI.as_view()),
    path('api-token-auth/', obtain_auth_token , name='api_token_auth'),
    path('index/', index),
    path('person/', Person_view),
    path('login/', login),
    path('persons/', PersonAPI.as_view()),  
]