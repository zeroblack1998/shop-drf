from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer


class ProductCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new product
    queryset = Product.objects.all(),
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    # API endpoint that allows product to be viewed.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single product by pk.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a product record to be updated.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a product record to be deleted.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
