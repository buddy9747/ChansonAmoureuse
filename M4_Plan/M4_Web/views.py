from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'M4_Web/index.html')

def about(request):
    return render(request,'M4_Web/aboutus.html')

def careers(request):
    return render(request,'M4_Web/careers.html')

def contact(request):
    return render(request,'M4_Web/contactus.html')

def education(request):
    return render(request,'M4_Web/Education.html')

def fashion(request):
    return render(request,'M4_Web/Fashion.html')

def food(request):
    return render(request,'M4_Web/food.html')

def healthcare(request):
    return render(request,'M4_Web/healthcare.html')

def published(request):
    return render(request,'M4_Web/published_articles.html')

def retail(request):
    return render(request,'M4_Web/retail.html')
