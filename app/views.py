import PIL
import random
import string
from qrcode import *
from MSSN.settings import *
from .models import info
from django.http import HttpResponse
from paystackapi.paystack import Paystack
from django.shortcuts import render, redirect
from paystackapi.transaction import Transaction
from django.core.files.base import ContentFile

def index(request):
    if request.method == 'POST':
        global email, surname
        surname = request.POST['surname']
        other = request.POST['other']
        email = request.POST['email']
        regno = request.POST['regno']
        department = request.POST['department']
        phone = request.POST['phone']
        
        #generate QR
        qr = QRCode(
        version = 1,
        error_correction = constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
        )

        qr.add_data(f"Name: {other} {surname}\nReg No: {regno}\nEmail Address: {email}\nDepartment: {department} \nPhone No: {phone}")
        qr.make(fit = True)
        img = qr.make_image(fill_color = "black", black_color = "white")
        img.save(f"{MEDIA_ROOT}/{surname}.png")        

        with open(f"{MEDIA_ROOT}/{surname}.png", "rb") as f:
            data = f.read()

        if not info.objects.filter(email = email):
            obj = info()
            obj.email = email
            obj.surname = surname
            obj.phone = phone
            obj.other = other
            obj.department = department
            obj.regno = regno
            obj.qr_code.save(f'{surname}.png', ContentFile(data))
            obj.save()
            return redirect('payment')
        return redirect('/')
    return render(request, 'index.html')

def payment(request):
    rand = ''.join(

    [random.choice(
        string.ascii_letters + string.digits) for n in range(7)])
    Paystack(paySECRET_KEY)
    response = Transaction.initialize(reference = rand, amount = '500', email = email)
    global Con
    Con = response['status']
    if Con:
        return redirect(response['data']['authorization_url'])
    else:
        return redirect('/')
        
def success(request):
    
    obj = info.objects.filter(email = email)

    return render(request, "success.html", {'data':obj})
