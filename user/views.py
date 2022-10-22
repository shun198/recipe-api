from rest_framework import generics
from user.serializers import UserSerializer

# Create your views here.
# genericsのCreateAPIViewを使用
class CreateUserView(generics.CreateAPIView):
    # UserSerializerを使用
    # シリアライザ内のModelを使用できる
    serializer_class = UserSerializer
