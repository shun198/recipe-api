from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

# Create your views here.
# genericsのCreateAPIViewを使用
class CreateUserView(generics.CreateAPIView):
    # UserSerializerを使用
    # シリアライザ内のModelを使用できる
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    # 自作した認証用シリアライザを使用
    serializer_class = AuthTokenSerializer
    # api_settingsに記載されている
    # REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.TemplateHTMLRenderer',
    # ],
    # OpenAPI用に指定
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# getとpatchとput
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
