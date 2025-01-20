from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class StudentApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            "status": True,
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Student added successfully",
                "data": serializer.data
            }, status=201)
        return Response({
            "status": False,
            "errors": serializer.errors
        }, status=400)
    

class LoginAPI(APIView):
    def post(self , request): 
        data = request.data
        print("Request data:", data)
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid(): 
            return Response({
            "status":False,
            "data": serializer.errors
        })
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user_obj = authenticate(username = username , password = password)
        if user_obj:
            Token_obj, _= Token.objects.get_or_create(user=user_obj)
            #print("Token:", Token_obj.key)
            return Response({
            "status": True,
            "data":{'Token' :Token_obj.key }
        })


        """print("Username:", username)
        print("Password:", password)"""

        return Response({
            "status": True,
            "data": {
                "message" : "Invalid credentials"
            }
        })
    
"""class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Login successful"})
        return Response({"errors": serializer.errors}, status=400)    
"""