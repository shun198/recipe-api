from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# UserManagerクラスを編集
class UserManager(BaseUserManager):

    # ユーザを作成
    # extra_fieldを指定することでいちいちcreate_userを上書きせずに済む
    def create_user(self,email,password=None,**extra_field):
        if not email:
            raise ValueError("メールアドレスは必須です")
        user = self.model(email=email,**extra_field)
        # PermissionsMixinから継承
        # パスワードを暗号化
        user.set_password(password)
        # _create_userメソッドで使用
        # 複数DBに対応するためにself._dbをつける
        user.save(using=self._db)

        return user


    # UserManagerクラスから継承
    # ユーザ名を入力する代わりにemailを指定しているのでoverrideする必要がある
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        # PermissionsMixinから
        user.is_superuser = True
        # UserManagerクラスの_create_userメソッドで使用
        # 複数DBに対応するためにself._dbをつける
        user.save(using=self._db)

        return user

# User
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # django-adminにログインできるかどうか
    is_staff = models.BooleanField(default=False)

    # AbstractUserクラスで定義されている
    # UserManagerクラスを紐つけることでAbstractBaseUserやPermissionsMixinのメソッドやプロパティが使用できる
    objects = UserManager()

    # AbstractUserクラスで定義されている
    # デフォルトで必須
    # 今回はemail
    # ユーザ名を入力する代わりにemailを指定
    USERNAME_FIELD = "email"
