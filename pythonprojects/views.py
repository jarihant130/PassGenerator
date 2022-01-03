from django.http import HttpResponse
from django.shortcuts import render
import string, random


def index(request):
    return render(request, 'index.html')

def generator(request):
    # Check checkbox values
    punctuation = request.POST.get('punctuation', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    digits = request.POST.get('digits', 'off')
    length = request.POST['length']
    removeduplicates = request.POST.get('removeduplicates', 'off')
    password = request.POST.get('password', 'error')
    
    password_selection = ""
    included_string = ""
    password_range = [i for i in range(6, 257)]
    
    # Check which checkbox is on
    if (punctuation == "on"):
        password_selection = password_selection + string.punctuation
        included_string += "Puctuation, "

    if (lowercase == "on"):
        password_selection = password_selection + string.ascii_lowercase
        included_string += "All Lower Case, "
    if (uppercase == "on"):
        password_selection = password_selection + string.ascii_uppercase
        included_string += "All Upper Case, "
 
    if (digits == "on"):
        password_selection = password_selection + string.digits
        included_string += "Digits, "
    
    if (digits == "on") or (lowercase == "on") or (uppercase == "on") or (punctuation == "on"):
        password = []
        password_selection = list(password_selection)
        random.shuffle(password_selection)
        for i in range(int(length)):
            password.append(random.choice(password_selection))
        random.shuffle(password)
        password = "".join(password)
        params = {'purpose': 'Include {}'.format(included_string[:-2]), 'generated_text': password, "length": length, 'password_range': password_range}
        return render(request, 'generator.html', params)
    
    else:
        return HttpResponse("Error")
