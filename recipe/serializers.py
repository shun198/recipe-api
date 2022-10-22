from rest_framework import serializers
from user.models import (
    Recipe,
    Tag,
)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id","title","time_minutes","price","link"]
        read_only_fields = ["id"]



class RecipeDetailSerializer(RecipeSerializer):
    # RecipeSerializerのMetaクラスを継承
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description"]


class TagSerializer(serializers.ModelSerializer):
      class Meta:
          model = Tag
          fields = ["id","name"]
          read_only_fields = ["id"]
