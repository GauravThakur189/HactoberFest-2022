from django.shortcuts import render

# Create your views here.#csc
def index(request):
    return render(request, 'Desk/index.html')