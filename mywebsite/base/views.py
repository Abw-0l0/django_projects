from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51LLqo7JfJLK6M5jB8TCwPSAIxnEdzBqiVgAiFXJmFJ0VTv066wEJmZSbaKDfWw1b1PNC1bDW4KBQH8oqeIuID8Qg00LpBZAsaB"


def home(request):
    return render(request, 'base/home.html')


def support(request):
    return render(request, 'base/support.html')

def paypal(request):
    return render(request, 'base/paypal.html')

def contact(request):
    return render(request, 'base/contact.html')


def stripee(request):
    return render(request, 'base/stripe.html')


def charge(request):

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="donation"
        )

    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})
