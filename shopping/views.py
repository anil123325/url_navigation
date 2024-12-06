from django.shortcuts import render


# Create your views here.
def shop(request):
    return render(request,'shopping.html')
def dress(request):
    return render(request,'dress.html')