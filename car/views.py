from django.shortcuts import render
from .models import Cars
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    return HttpResponse("Hello, World !")

def test_page(request):
    return HttpResponse("Hello")


def sales_sheet(request):
    sales_sheets = Cars.objects.all()
    context = {"sales_sheets": sales_sheets}
    return render(request, 'cars/.html', context=context)