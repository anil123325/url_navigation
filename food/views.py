from django.shortcuts import render

# Create your views here.
def biriyani(request):
    return render(request,'food.html')
def nonveg(request):
    return render(request,'nonveg.html')
