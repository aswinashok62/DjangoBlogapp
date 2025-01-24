# Django-Blog-master/admin/views.py
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
# Django-Blog-master/admin/views.py
# ... existing imports ...
from django.urls import reverse
from django.contrib.auth import logout

class CustomAdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect(reverse('admin-dashboard'))  # Redirect to the admin dashboard
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'admin_login.html')
        

# Django-Blog-master/admin/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required  # Ensure that only logged-in users can access this view
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')   


class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # Log the user out
        messages.success(request, 'You have been logged out successfully.')  # Optional success message
        return redirect('/custom-admin/login/')
    

# Django-Blog-master/admin/views.py
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Blog  # Assuming you have a Blog model

class UsersListView(View):
    def get(self, request):
        users = User.objects.all()  # Fetch all users
        return render(request, 'users_list.html', {'users': users})

class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()  # Fetch all blogs
        return render(request, 'blog_list.html', {'blogs': blogs})    
    
# Django-Blog-master/admin/views.py
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

def block_user(request, user_id):
    if request.method == 'POST':
        user_to_block = get_object_or_404(User, id=user_id)
        # Implement your blocking logic here
        # For example, you might want to set a field on the user or add them to a blocked list
        user_to_block.is_active = False  # Example: deactivate the user
        user_to_block.save()
        
        messages.success(request, f'User {user_to_block.username} has been blocked.')
        return redirect('users_list')  # Redirect to the user list page    

def unblock_user(request, user_id):
    if request.method == 'POST':
        user_to_unblock = get_object_or_404(User, id=user_id)
        user_to_unblock.is_active = True  # Reactivate the user
        user_to_unblock.save()
        
        messages.success(request, f'User {user_to_unblock.username} has been unblocked.')
        return redirect('users_list')  # Redirect to the user list page    


# ... existing code ...
def remove_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()  # Remove the user
    return redirect('users_list')  # Redirect to the user list page
# ... existing code ...


# Django-Blog-master/admin/views.py
from django.shortcuts import render
from .models import Blog  # Adjust the import based on your Blog model

# Django-Blog-master/admin/views.py
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in
def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)  # Filter blogs by the logged-in user
    return render(request, 'admin/blog_list.html', {'blogs': blogs})  # Render the template with blogs # Render the template with blogs
# ... existing code ...