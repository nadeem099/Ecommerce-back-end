from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="mtgfpp97zk5ymh2q",
        public_key="hq8cf4xhkzsw6s7s",
        private_key="ab2c5ead9f4bef1a2f9d0549424eae20"
    )
)

def validate_user_session(id, token):
    UserModel=get_user_model
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'invalid session please login again!'})
    return JsonResponse({'clientToken':gateway.client_token.generate(),'success':True})

@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'invalid session please login again!'})
    nonce_from_the_client = request.POST['paymentMethodNonce']
    amount_from_the_client = request.POST['amount']

    result = gateway.transaction.sale({
        "amount":amount_from_the_client,
        "payment_method_nonce":nonce_from_the_client,
        "options":{
            "submit_for_settlement":True
        }
        
    })
    if result.is_success:
        return JsonResponse({'success':result.is_success, 'transaction':{"id": result.transaction.id, "amount":result.transaction.amount}})
    else:
        return JsonResponse({'error':True, 'success':False})