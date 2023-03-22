from rest_framework import serializers
from .models import Product, Statistic


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
        
        
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    code = serializers.CharField(max_length=20)
    expire = serializers.DateField()
    created = serializers.DateField(read_only=True)
    
    def validate_code(self, value):
        if Product.objects.filter(code=value).exists():
            raise serializers.ValidationError('Bu kodda mehsul movcuddur!')
        return value
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.price = validated_data['price']
        instance.code = validated_data['code']
        instance.expire = validated_data['expire']
        instance.save()
        return instance
    