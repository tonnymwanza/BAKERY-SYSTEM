from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from . models import Subscribing
from django.views import View
from . forms import ContactForm
from . models import Contact
from . models import Products
from . models import Order
# Create your views here.

class HomeView(View):
    
    def get(self, request):
        subscriber_ = Subscribing.objects.count()
        context = {
            'subscriber_': subscriber_
        }
        return render(request, 'home.html', context)

    
class AboutView(View):
    
    def get(self, request):
        return render(request, 'about.html')
    
class ServiceView(View):

    def get(self, request):
        return render(request, 'service.html')
    
class ProductView(View):

    def get(self, request):
        products = Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product.html', context)
    
class ContactView(View):

    def get(self, request):
        form = ContactForm(request.GET)
        context = {
            'form': form 
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message']
            )
            form = ContactForm()
            messages.info(request, 'message send successfully')
        else:
            messages.error(request, 'error sending message')
        context = {
            'form': 'form'
        }
        return redirect('contact')
    
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'the username is in use. find another one')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = firstname, username = username, email = email, password = password)
                return redirect('login')
        else:
            messages.error(request, 'the passwords given dont match')
            return redirect('register')
    return render(request, 'register.html')

def login(request): #login function
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else: 
                return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def order(request, pk):
    products = Products.objects.get(id=pk)
    order = Order.objects.create(products=products)
    context = {
        'products': products,
        'order': order
    }
    return redirect('order_success')

class OrderViewSuccess(View):

    def get(self, request):
        return render(request, 'order_success.html')