from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from .RegEx import search_word_position, find_all_words,search_item
from .forms import StudentForm


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    positions = search_word_position('The rainin spain', 'ai')
    try:
        return render(request, 'blog/home.html', {'positions': positions})
    except FileNotFoundError:
        raise Http404("Template does not exist")

def login(request):
    return render(request, 'blog/login.html')

def menuitem(request):
    items = ["burger", "pizza", "sushi", "pasta", "salad"]
    result = ""
    for item in items:
        result += f"<h1 style='color:blue'>you ordered {item}</h1>"
    return HttpResponse(result)

def inherit1(request):
    position = find_all_words('hello palnet')
    position2 = search_item("The rain in Spain")

    context = {'position': position, 'position2': position2}
    
    return render(request, 'blog/inherit1.html', context)




@csrf_exempt
def form_view(request):
    if request.method == 'POST':
        # Access form data
        address = request.POST.get('address')
        city = request.POST.get('city')
        region = request.POST.get('region')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        topic_selection = request.POST.getlist('topic_selection')
        billing_frequency = request.POST.get('billing_frequency')

        

        return HttpResponse('Form data received.')
    else:
        return HttpResponse('Invalid request.')


# views.py



def student_form_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect after POST
        else:
            form = StudentForm()

    return render(request, 'blog/form.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, such as logging in the user
            return HttpResponse('User created successfully!')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})





def set_cookie(request):
   response = HttpResponse("Cookie set!")
   response.set_cookie('username', 'john_doe', max_age=3600) # Set cookie with a username and max_age of 1 hour

   return response


def get_cookie(request):
   username = request.COOKIES.get('username')
   if username:
      return HttpResponse(f"Hello, {username}! Welcome back.")
   else:
      return HttpResponse("No cookie found!")
   
   

