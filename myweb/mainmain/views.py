from django.shortcuts import render
def base(request):
    return render(request, 'base.html')
def main(request):
    return render(request, 'main.html')
def agenda(request):
    return render(request, 'agenda.html'    )

# Create your views here.
