from rest_framework import serializers
from .models import User
from rest_framework import status

class usersearilizers(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=34)
    password=serializers.CharField(max_length=34)
    phone=serializers.CharField(max_length=34)

    class Meta:
        model=User
        fields=('email', 'password', 'phone')


    def validate(self, attrs):
        email=attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            return serializers.ValidationError({'email', 'email is already exit'},status.HTTP_400_BAD_REQUEST )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class loginserailizers(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=34)
    password=serializers.CharField(max_length=34)

    class Meta:
        model=User
        fields=['email', 'password']

class calculatesearizilers(serializers.Serializer):
    x=serializers.IntegerField()
    n=serializers.IntegerField()
