from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # どのモデルやフィールドを使うか指定
    class Meta:
        # ユーザモデルからデータを取得
        model = get_user_model()
        fields = ["email","password","name"]
        # フィールドに条件を指定(今回だとパスワードはwrite_onlyにしたい)
        extra_kwargs = {"password":{"write_only":True,"min_length":4}}

    # createメソッドをオーバーライド
    # パスワードをencryptするためにオーバーライド
    def create(self, validated_data):
        # UserManagerのcreate_userメソッドを使用
        return get_user_model().objects.create_user(**validated_data)

    # updateメソッドをオーバーライド
    # instanceに既存のデータ、validated_dataにputまたはpostするデータが入る
    def update(self, instance, validated_data):
        # validated_dataからパスワードを取り出す(Listからなくなる)
        password = validated_data.pop("password")
        # ModelSerializerクラスのupdateメソッドを定義(使用)
        # 通常のoverrideだと基底クラスの処理が無効化されてしまう
        # そのため、今回はModelSerializerのupdateメソッドを無効化せずに使用したい
        user = super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save

        return user


class AuthTokenSerializer(serializers.Serializer):
    # emailとpassword用のFieldを自作
    email = serializers.EmailField()
    password = serializers.CharField(
        # Swaggerを使う際にパスワードを
        style={"input_type":"password"},
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg = _("認証失敗")
            raise serializers.ValidationError(msg,code="authorization")

        attrs["user"] = user
        return attrs
