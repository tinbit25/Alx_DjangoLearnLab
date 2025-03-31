from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm  # Import your custom form

def register(request):
    if request.method == "POST":  # Ensure method is checked
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserRegisterForm()

    return render(request, 'blog/register.html', {'form': form})
