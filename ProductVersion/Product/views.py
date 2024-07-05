from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from rest_framework.viewsets import ModelViewSet

from .models import Product, Version
from .serializer import VersionSerializer, ProductSerializer


# Create your views here.
def main(request):
    versions = Version.objects.all()
    return render(request, 'Product/main.html', {'versions': versions})


def Wrap(request):
    products = Product.objects.get(title="Wrap")
    versions = products.versions.all()
    return render(request, 'Product/Wrap.html', {'versions': versions, 'products': products})


def Wrap4D(request):
    products = Product.objects.get(title="Wrap4D")
    versions = products.versions.all()
    return render(request, 'Product/Wrap4D.html', {'versions': versions, 'products': products})


def ZWrap(request):
    products = Product.objects.get(title="ZWrap")
    versions = products.versions.all()
    return render(request, 'Product/ZWrap.html', {'versions': versions, 'products': products})


class VersionView(ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
