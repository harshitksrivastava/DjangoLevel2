from django.shortcuts import render
from user_info.models import User
# Create your views here.
def index(request):
    return render(request,'user_info/index.html')

def user(request):
    user_info = User.objects
    return render(request,'user_info/user.html',{'user_info':user_info})
