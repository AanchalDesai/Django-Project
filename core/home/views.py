from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import Person
from home.serializers import PeopleSerializer , LoginSerializer , RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterAPI(APIView):
     
    def post(self , request):
        print("cejnvjffffff", request)
        print("dir >> ", request.__dir__)
        data = request.POST
        print("data>.", data)
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors
            }), status.HTTP_400_BAD_REQUEST
        
        serializer.save()

        return Response({'status':'True' , 'message' : 'user created' }, status.HTTP_201_created)

@api_view(['GET' , 'POST'])
def index(request):
    if request.method =='GET':
        json_response = {
            'name' : 'Aanchal',
            'courses' : ['Python' , 'C++'],
            'method' : 'GET'
        }
        return Response(json_response)
    
    elif request.method == 'POST' :
        data = request.data
        print(data)
        json_response = {
            'name' : 'Aanchal',
            'courses' : ['Python' , 'C++'],
            'method' : 'POST'
        }

        return Response(json_response)
    
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
 
    if serializer.is_valid():
        data = serializer.data
        print(data)   
        return Response({'message' : 'success'})
    
    return Response(serializer.errors)

class PersonAPI(APIView):
     permission_classes = [IsAuthenticated]
     authentication_classes = [TokenAuthentication]
     
     def get(self , request):
        print(request.user)
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs , many = True)
        return Response(serializer.data)
    
     def post(self , request):
        data = request.data
        print(data)
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            print(serializer.data)

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

     def put(self , request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
     def patch(self , request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
     def delete(self , request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
    
@api_view(['GET' , 'POST' , 'PUT' , 'PATCH' , 'DELETE'])
def Person_view(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs , many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
    



class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all() 

    def list(self , request,*args, **kwargs):
        print("Hererrerrere")
        search = request.GET.get('search')
        queryset = self.get_queryset()
        print("search >>> ", search)
        if search:
            queryset = queryset.filter(name__istartswith = search)

        serializer = PeopleSerializer(queryset , many=True )
        return Response({'status' : 200 ,'data' : serializer.data})
       
