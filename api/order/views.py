from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Order
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def validata_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

def add(request, id, token):
    if not validata_user_session(id, token):
        return JsonResponse({'error':'Please re-login', 'code':'1'})
    
    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_pro = len(products.split(',')[:-1])

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'User does not exit'})

    ordr = Order(user = user_id, product_names = products,  total_products = total_pro, transaction_id=transaction_id, total_amount = amount)
    ordr.save()
    return JsonResponse({'success':True, 'error': False, 'message':'order placed successfully'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer