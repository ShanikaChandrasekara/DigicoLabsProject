from django.shortcuts import redirect, render

def hi(request):
    return render(request, 'dashboard.html')

def hello(requset):
    return render(requset, 'MyApp/Scaffold/assets/css/style.css')
