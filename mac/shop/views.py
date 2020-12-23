from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact,Order
from django.contrib.auth.models import User,auth
from django.contrib import messages
from math import ceil
# Create your views here.
def index(request):
    products=product.objects.all()
    allProds=[]
    catprods= product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
   
    return render(request,'shop/index.html',params)

def checkout(request):    
    return render(request,'shop/checkout.html')

def address(request):  
    if (request.method =="POST"):
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(itemsJson=itemsJson, name=name, email=email, address=address, city=city, state=state,
                      zip_code=zip_code, phone=phone)
        order.save()   
    return render(request,'shop/address.html')

def contact(request):
    if (request.method =="POST"):
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')




def about(request):
    return render(request,'shop/about.html')
def tracker(request):
    return HttpResponse('tracker')
def productView(request):
     return HttpResponse('productView')




def login(request):
    if (request.method =="POST"):
        username =request.POST.get('username','')
        password =request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'shop/address.html')
        else:
            messages.info(request, 'Plese register first')
            return render(request,'shop/login.html')
    else:
        return render(request,'shop/login.html')

def register(request):
    if (request.method =='POST'):
        username =request.POST['username']
        password =request.POST['password']
        password2 =request.POST['password2']
        email = request.POST['email']
        if (password == password2):
            user =User.objects.create_user(username=username, password=password,email=email)
            user.save()
            print("User created")
            return render(request,'shop/login.html')
        else:
            print(request, 'Plese enter correct password')
            return HttpResponse("Plese enter correct password")
    else:
        return render(request,'shop/register.html')

def payment(request):    
    return render(request,'shop/payment.html')