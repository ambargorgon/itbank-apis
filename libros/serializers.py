from rest_framework import serializers
from .models import Libro
from django.contrib.auth.models import User

# class LibroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Libro
#         #indicamos que use todos los campos
#         fields = "__all__"
#         #les decimos cuales son los de solo lectura
#         read_only_fields = (
#             "id",
#             "created_at",
#             "updated_at",
#         )
#         owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    libros = serializers.PrimaryKeyRelatedField(many=True, queryset=Libro.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'libros']

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Libro
        fields = ['title','genre','year','author','created_at','updated_at','owner']
                
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     libros = serializers.HyperlinkedRelatedField(many=True, view_name='libro-detail',read_only=True)
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'libros']