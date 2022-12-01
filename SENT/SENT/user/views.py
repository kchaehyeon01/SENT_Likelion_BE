from django.contrib.auth.models import User
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, ProfileRegisterSerializer, LoginSerializer
from .permissions import IsAuthenticated


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class ProfileRegisterView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key, "user_id": token.user_id }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"success" : "로그아웃에 성공했습니다.!"}, status=status.HTTP_200_OK)

# Create your views here.
