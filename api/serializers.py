from django.contrib.auth import get_user_model
from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AccountMovement, AMOptions

# login
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super( LoginSerializer, cls).get_token(user)
        token['username']= user.username
        return token 
# getUserDetail
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model= get_user_model() 
        fields= ('id', 'username')
# register
class RegisterSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required= True , validators=[validate_password])
    password2 = serializers.CharField(write_only= True, required= True)

    class Meta:
        model= User
        fields=('username','password','password2','email','first_name','last_name')
        extra_kwargs= {
            'first_name':{'required':True},
            'last_name':{'required':True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username'],
            email= validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
# changePassword 
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only= True, required=True)

    class Meta:
        model =User
        fields = ('old_password','password','password2')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password Fields didn't match."})
        return attrs
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password":"Old Password is not Correct"})
        return value
    
    def update(self, instance, validated_data ):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

# accountSerializer
class AccountMovementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AccountMovement
        fields = ['id','Amount','detail','options']
# accountMovementOptionsSerializer
class AMOptionsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AMOptions
        fields = ['id','name']
