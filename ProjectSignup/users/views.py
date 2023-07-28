from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import forms,login,authenticate
from .forms import RegistrationForm




class Target(generic.CreateView):
 form_class = forms.UserCreationForm()
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

def signup(request):
        if request.method=='POST':
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data.get('username')
                # raw_password = form.cleaned_data.get('password1')
                # user = authenticate(username=username, password=raw_password)
                # login(request, user)
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'users/signup.html', {'form': form})

