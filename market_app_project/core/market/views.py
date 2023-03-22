from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product, Statistic
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    if request.method == 'GET':
        product = Product.objects.filter(pk=pk).first()
        if product:
            # serializer = ProductSerializer({
            #     'id': 1, 
            #     'title': 'slavyanka',
            #     'price': 1.2,
            #     'code': '1851935',
            #     'expire': '2023-03-25',
            #     'created': '2023-02-22',
            # })
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    # elif request.method == 'PATCH':
    #     product = get_object_or_404(Product, pk=pk)
    #     serializer = ProductSerializer(product, request.data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        