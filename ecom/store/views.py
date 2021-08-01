from django.db.models.fields import EmailField
from django.http import request
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher, make_password, check_password
from django.views import View
from django.core.mail import send_mail
from .models import *
# Create your views here.


def main(request):
    if request.method=='POST':
        product = request.POST['product']
        remove = request.POST.get('remove')
        print(remove)
        

        cart = request.session.get('cart')
        
        if cart:
            quantity= cart.get(product)
           
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                    
                else:
                    cart[product] = quantity+1


                
            else:
                cart[product] = 1            
        else:
            cart = {}
            cart[product] = 1

        
        request.session['cart'] = cart
        print(request.session['cart'] )
        return redirect('main')
    else:
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = Product.objects.all()
        context ={'products':products}
        print(request.session.get('customer_email'))
        return render(request,'store.html',context)
        
        
def content(request,header):
    data=Product.objects.get(name=header)
    context = {'data':data,'header':header}
    if (data):
        return render(request,'content.html',context)
    else:
        return render(request,'store.html')

        

#def checkout(request):
    #data=Product.objects.get(name=header)
    #context = {'data':data,'header':header}
    #if (data):
    #return render(request,'checkout.html')
    #else:
        #return render(request,'store.html')
    

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        value ={
            'firstname':firstname,
            'lastname':lastname,
            'phone':phone,
            'email':email
        }

        #validation
        error_message = None
        customer = Customer(first_name=firstname,
                                last_name=lastname,
                                phone=phone,
                                email=email,
                                password=password)

        error_message = self.validateCustomer(customer)
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('main')
            #return redirect('http://127.0.0.1:8000/') works but if domain changes will have to manually change in all places
            #return render(request,'store.html')
        else:
            data = {
                'error':error_message,
                'value':value
            }
            return render(request,'signup.html',data)
        
        
    def validateCustomer(self,customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required"
        elif len(customer.first_name)<4:
            error_message = "First name must be four character long"
        elif (not customer.email):
            error_message = "Email Required"
        elif (not customer.password):
            error_message = "Password Required"       
        elif Customer.objects.filter(email=customer.email).exists(): #method 3 to keep email unique
            error_message="Email Address Already Exists"


        return error_message

class Login(View):
    def get(self,request):
        return render(request,'login.html')
        


    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        customer= Customer.getCustomer(email)
        error_message = None

        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id']= customer.id
                request.session['customer_email']= customer.email
                
                return redirect('main')
            else:
                error_message = 'Email or Password invalid !'
                
        else:
            error_message = 'Email or Password invalid !'

        return render(request,'login.html',{'error':error_message})


class Cart(View):
    def get(self,request):
        ids = (list(request.session.get('cart').keys()))
        products=Product._get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})

    def post(self,request):
        ids = (list(request.session.get('cart').keys()))
        products=Product._get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})


def logout(request):
    request.session.clear()
    return redirect('login')


class Checkout(View):
    def get(self,request):
        ids = (list(request.session.get('cart').keys()))
        products=Product._get_products_by_id(ids)
        print(products)
        return render(request,'checkout.html',{'products':products})


    def post(self,request):
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        msg_order = "Dear Customer,\n Your order details are as follows"
        msg_deliver = "And deliver credentials are as follows"
        
        total_products = request.POST['total_products']
        total_bill = request.POST['total_bill']
        body =msg_order + '\n' + total_products + '\n' + total_bill+'\n' +msg_deliver+'\n' + name + '\n' + address + '\n' + email + '\n' + phone + '\n' 

        print(body)
        
        if send_mail('E-buy Order Confirmation',body,'django78692@gmail.com',[email], fail_silently=False):
            print('Success')
            request.session.clear()
            return redirect('main')
        else:
            print("Failed")
            return redirect('checkout')
        



