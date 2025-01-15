from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET' , 'POST' , 'PUT'])
def index(request):
    courses = {  # Use '=' to assign a dictionary
        'course_name': 'Python',
        'learn': ['flask', 'Django', 'Tornado', 'FastApi'],
        'course_provider': 'Aanchal',
        }
    if request.method == 'GET' :
        print('you hit a get method')
        return Response(courses)
    elif request.method == 'POST':
        print('you hit a post method')      
        return Response(courses)
    elif request.method == 'PUT':
        print('you hit a put method')      
        return Response(courses)

