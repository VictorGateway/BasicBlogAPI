from rest_framework.serializers import LoginSerializer as RestAuthLoginSerializer

class LoginSerializer(RestAuthLoginSerializer):
    username=None

