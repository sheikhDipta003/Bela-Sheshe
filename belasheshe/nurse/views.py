from django.shortcuts import render

# Create your views here.
def nurse_dashboard(request):
    return render(request, 'nurse/dashboard.html')
