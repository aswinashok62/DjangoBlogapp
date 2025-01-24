from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


# Example view for handling the registration
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm

# ... existing code ...
# ... existing code ...
def register(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)
        password = request.POST.get('password')  # Get the password from the form
        confirm_password = request.POST.get('confirm_password')  # Get the confirm password from the form
        
        if user_form.is_valid() and profile_form.is_valid() and password == confirm_password:
            user = user_form.save(commit=False)  # Save the user first
            user.set_password(password)  # Set the user's password
            user.save()  # Save the user
            
            # Check if the profile already exists
            profile, created = Profile.objects.get_or_create(user=user)  # Get or create the profile
            if created:
                # If a new profile was created, update it with the profile form data
                profile = profile_form.save(commit=False)  # Create profile but don't save yet
                profile.user = user  # Associate the profile with the user
                profile.save()  # Now save the profile
            else:
                # If the profile already exists, update it
                profile_form.instance = profile  # Set the instance to the existing profile
                profile_form.save()  # Save the existing profile with new data
            
            return redirect('login')  # Redirect after successful registration
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/register.html', context)
# ... existing code ...


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile_image_url': request.user.profile.image.url if request.user.profile.image else None  # Ensure image URL is passed
    }

    return render(request, 'users/profile.html', context)


