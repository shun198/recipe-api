from django.urls import path
from user.views import (
    CreateUserView,
    CreateTokenView,
    ManageUserView,
)

# テストコードからエンドポイントを逆参照する時に使用
app_name = "user"

urlpatterns = [
    # name="create"を指定することで逆参照できる
    path("create/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="me"),
]
