from django.shortcuts import render, redirect
from .models import Member
from django.contrib import auth

# Create your views here.



def logout(request):
    auth.logout(request)
    return redirect('/')

def mypage(request):
    user = request.user
    member = Member.objects.get(user=user)
    context = {
        'member':member,
        }
    return render(request, 'accounts/mypage.html', context)

def newinfo(request):
    return render(request, 'accounts/information.html')

def information(request):
    user= request.user
    new_info = Member()
    new_info.user = request.user
    new_info.name = request.POST['name']
    new_info.gender = request.POST['gender']
    new_info.sports = request.POST['sports']
    new_info.save()
    return redirect('accounts:mypage')
