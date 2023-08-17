from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo, priority_choices

# Create your views here.


@login_required(login_url='login')
def home(request):
    todos = Todo.objects.filter(user=request.user)
    total = todos.count()
    pending = todos.filter(completed=False)
    context = {
        'todos':todos,
        'total':total,
        'pending':pending,
    }
    return render(request,'home.html',context)

def Add(request,pk=None):
    if request.method == 'POST':
        description = request.POST.get('inputTodo')
        inputPriority = request.POST.get('inputPriority')
        if inputPriority == '' or description == '':
            messages.error(request,"Fields should not be empty")
            return redirect('add')
        todo = Todo.objects.create(user=request.user,description=description,priority=inputPriority)
        todo.save()
        return redirect('home')
    return render(request,'add.html')

def Edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        todo.description = request.POST.get('inputTodo')
        todo.priority = request.POST.get('inputPriority')
        todo.save()
        return redirect('home')
    context = {
        'todo':todo,
        'priority_choices':priority_choices,
    }
    return render(request,'edit.html',context)
            

def completed(request,pk):
    todo = Todo.objects.get(id=pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('home')

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')

def login_page(request):
    print('login')
    if request.method == 'POST':
        username =  request.POST.get('UserName')
        Password =  request.POST.get('Password')
        user = authenticate(request,username=username,password=Password)
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username =  request.POST.get('UserName')
        Password =  request.POST.get('Password')
        ConfirmPassword =  request.POST.get('ConfirmPassword')
        if username == '' or Password == '' or Password != ConfirmPassword:
            messages.error(request,"Invalid form")
            return redirect('register')
        user = User.objects.create_user(username=username,password=Password)
        user.save()
        return redirect('login')
    return render(request,'register.html')
        
        
        
