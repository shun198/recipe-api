from django.contrib.auth import get_user_model

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
