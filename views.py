# users/views.py

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.'})
        else:
            return JsonResponse({'message': 'Invalid credentials.'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform validation and create the user
        # You can use Django's built-in UserCreationForm or customize it as per your requirements
        return JsonResponse({'message': 'User created successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Implement the logic to send password reset instructions to the user's email
        return JsonResponse({'message': 'Password reset instructions sent.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful.'})
