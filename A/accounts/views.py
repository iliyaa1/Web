from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy

class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
            )
            messages.success(request, 'ساخت حساب کاربری با موفقیت انجام شد')
            return redirect('accounts:user_login')
            
        
        else:
            return render(request, 'register.html', {'form': form})
        


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    

    def form_valid(self, form):
        messages.success(self.request, 'ورود به حساب کاربری با موفقیت انجام شد')
        return super().form_valid(form)
    next_page = reverse_lazy('home:home')




class UserLogoutView(View):
    def get(self, request):
        auth_logout(request)
        messages.success(request, "شما با موفقیت از حساب خود خارج شدید")
        return redirect('home:home')
        



    
    




