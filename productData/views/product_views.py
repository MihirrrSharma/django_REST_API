from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from productData import models
from productData.serializers import MyProductSerializers

class FetchProducts(APIView):
    def get(self, request):
        prods = models.Products.objects.all()
        resp = MyProductSerializers(prods, many=True)
        return Response(resp.data)

class MakeProduct(APIView):
    def post(self, request):
        prod_request = request.data
        prod_data = MyProductSerializers(data=prod_request)
        if prod_data.is_valid():
            prod_data.save()
            return Response({'msg': "received"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': prod_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetProductByID(APIView):
    def get(self, request, id):
        prod = get_object_or_404(models.Products, id=id)
        resp = MyProductSerializers(prod, many=False)
        return Response(resp.data)
    
class ProductUpdateByID(APIView):
    def put(self, request, id):
        prod = get_object_or_404(models.Products, id=id)
        prod_data = MyProductSerializers(prod, data=request.data)
        if prod_data.is_valid():
            prod_data.save()
            return Response(prod_data.data)
        return Response(prod_data.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductByID(APIView):
    def delete(self, request, id):
        product = get_object_or_404(models.Products, id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
