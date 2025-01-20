from rest_framework import serializers
from .models import Person , ColorSerializer
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password =serializers.CharField()
     
    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('username is taken')
        
        if User.objects.filter(email =data ['username']).exists():
            raise serializers.ValidationError('email is taken')
        
        return data
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =serializers.CharField()

"""class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name' , 'id']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_color_info(self , obj):
      color_obj = Color.objects.get(id = obj.color.id)
      print(color_obj)
      print(color_obj.color_name)
      return {'color_name' : color_obj.color_name , 'hex_code' : '#000'}
      """

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_color_info(self, obj):
        color_obj = obj.color
        return {
            'color_name': color_obj.color_name,
            'hex_code': '#000'  # Example static value; update as needed
        }

    def create(self, validated_data):
        # Extract nested 'color' data
        color_data = validated_data.pop('color', None)
        if color_data:
            color = Color.objects.create(**color_data)  # Create new Color object
        else:
            color = None
        # Create Person object with color
        person = Person.objects.create(color=color, **validated_data)
        return person

    def update(self, instance, validated_data):
        # Handle nested 'color' updates
        color_data = validated_data.pop('color', None)
        if color_data:
            # Update existing color object
            Color.objects.filter(id=instance.color.id).update(**color_data)
        # Update Person fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



    def validate(self, data):
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if any(c in special_characters for c in data['name']):
           raise serializers.ValidationError('name cannot contain special chars') 
  
        if data.get('age') and data['age'] <18 :
            raise serializers.ValidationError('age should be greater than 18')

        return data 