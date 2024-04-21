from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    
    def get(self, request):
        return render(request, 'home.html')
    
class AboutView(View):
    
    def get(self, request):
        return render(request, 'about.html')
    
class ServiceView(View):

    def get(self, request):
        return render(request, 'service.html')
    
class ProductView(View):

    def get(self, request):
        return render(request, 'product.html')
    
class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')