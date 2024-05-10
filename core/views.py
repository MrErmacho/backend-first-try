from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def singup(request):
    return render(request, 'core/signup.html')

def magic(request):
    if request.method == "POST":
        random_number = random.randint(0, 10)
        user_guess = int(request.POST.get('user_guess'))
        if random_number == user_guess:
            result = "Молодец"
        else:
            result = f"Ты проиграл, магическое число было: {random_number}"    
        return render(request, 'core/magic.html', {'result': result})
    return render(request, 'core/magic.html')

def singup(request):
    return render(request, 'core/signup.html')
    