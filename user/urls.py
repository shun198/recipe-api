from django.urls import path
from user.views import CreateUserView

# テストコードからエンドポイントを逆参照する時に使用
app_name = "user"

urlpatterns = [
    # name="create"を指定することで逆参照できる
    path("create/", CreateUserView.as_view(), name="create")
]
