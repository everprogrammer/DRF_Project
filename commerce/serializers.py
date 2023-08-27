from rest_framework import serializers
from .models import CustomUser, Product

class CustomUserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = CustomUser
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')

    class Meta:
        model = Product
        fields = '__all__'

