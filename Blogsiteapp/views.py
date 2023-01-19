from collections import UserDict
from django.shortcuts import render,redirect
from .models import Blogsite,Profile
from .form import Blogsite_form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def form(request):
    if request.method =="GET":
       form = Blogsite_form
       return render(request,'home.html',{'form':form})

    else:
        form = Blogsite_form(request.POST,request.FILES)
        if form.is_valid():
          form.save()
        return redirect('show')

@login_required(login_url='login')
def show(request):
    data = Blogsite.objects.all()
    return render(request,'show.html',{'data':data})

def delete(request,id):
    data = Blogsite.objects.get(id=id)
    data.delete()
    return redirect('show') 

@login_required(login_url='login')
def update(request,id):
        data = Blogsite.objects.get(id=id)
        if request.method=="GET":
            form = Blogsite_form(instance=data)
            return render(request,'home.html',{'form':form})

        else:
             form = Blogsite_form(request.POST,instance=data)
             if form.is_valid():
                   form.save()
                   return redirect('show')

@login_required(login_url='login')
def readmore(request,id):
    data = Blogsite.objects.get(id=id)
    return render(request,'readmore.html',{'data':data})

def register(request):
    if request.method  == "POST":
        username = request.POST['username']
        email = request.POST['email']
        Password = request.POST['password']
        Re_Password = request.POST['confirm_password']
        
        if Password==Re_Password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USER ALREADY EXISTS")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL ALREADY EXISTS")
            else:
                user = User.objects.create_user(username=username,email=email,password=Password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password Does Not Match")
            return redirect('register')
    return render(request,'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('show')
        else:
            messages.info(request,"Password/USERNAME Does Not Match")
            return redirect('login')



    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def search(request):
    s =  request.POST['search']
    data = Blogsite.objects.filter(title__contains=s)
    return render(request,'show.html',{'data':data})

@login_required(login_url='login')
def edit(request,id):
    data = Blogsite.objects.get(id=id)
    
    if User:
        if request.method =="GET":
            form = Blogsite_form(instance=data)
            return render(request,'Edit.html',{'form':form})
        else:
            form = Blogsite_form(request.POST,request.FILES,instance=data)
            if form.is_valid():
                form.save()
                return redirect('show')
    else:
        return render(request,'Edit.html',)
    
def delete_b(request,id):
    data = Blogsite.objects.get(id=id)
    data.delete()
    return redirect('show')    


def profile_func(request):
    user = request.user
    p = Profile.objects.filter(user__exact=user).values('first_name')
    if p:
        d = Profile.objects.filter(user__exact=user)
        return render(request,'Profile.html',{'p':d,'done':p})
    else:   
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = request.user
            email = request.POST['email']
            profile_pic = request.FILES['img']
            ab = request.POST['about_me']

            data = Profile(first_name=first_name,last_name=last_name,
            user=user,email=email,profile_pic=profile_pic,
            about_me = ab)
            data.save()
            return redirect('show')
        else:
            return render(request,'Profile.html')

    
        
def editprofile(request,id):
    data = Profile.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = request.POST['username']
        email = request.POST['email']
        profile_pic = request.FILES['img']
        ab = request.POST['about_me']
       
        data = Profile(id = id ,first_name=first_name,last_name=last_name,user=user,email=email,profile_pic=profile_pic,about_me = ab).save()
        
        return redirect("profile")

    else:
        return render(request,'editprofile.html',{'data':data}) 

def about_us(request):
    return render(request,'about.html')



         