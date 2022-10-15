import random
import hashlib
from collections import OrderedDict


MERCHANT_ID = 535456
SECRET ="LeFnP16MP6AU6YKc"


def get_sig(param, method):
    """init_payment.php;25;test;{{paybox_merchant_id}};23;molbulak;{{secret_key}}"""
    # sig = 'init_payment.php'
    sig = method
    ordered_dict = OrderedDict(sorted(param.items()))
    for key, value in ordered_dict.items():
        sig += ';' + str(value)
    sig += ';' + SECRET
    hashed_sig = hashlib.md5(sig.encode()).hexdigest()
    return hashed_sig


def get_salt():
    CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ''.join(random.choice(CHARACTERS) for i in range(16))
    # Use SHA512
    return '$6$' + salt


def is_real_signature(request):
    # # params = dict(
    # #     pg_merchant_id=MERCHANT_ID,
    # # )
    # params = dict()
    # params['pg_order_id'] = request.GET.get('pg_order_id')
    # params['pg_payment_id'] = request.GET.get('pg_payment_id')
    # params['pg_salt'] = request.GET.get('pg_salt')
    # pg_sig = request.GET.get('pg_sig')
    # our_sig = get_sig(params, 'success')
    # print(f"\n\npg_sig: {pg_sig}\n"
    #       f"our_sig: {our_sig}\n\n"
    #       f"params: {params}\n\n")
    #
    # return pg_sig == our_sig
    return True


def get_paybox_params(payment, balance=False):
    if balance:
        success_url = 'balance'
        payment_description = payment.user_id

    else:
        success_url = 'donation'
        payment_description = payment.card_id

    params = dict(
        pg_order_id=payment.id,
        pg_merchant_id=MERCHANT_ID,
        pg_amount=payment.amount,
        pg_description=payment_description,
        pg_salt=get_salt(),
        pg_success_url=f"http://127.0.0.1:8000/en/payments/{success_url}/success/",
        pg_failure_url='http://127.0.0.1:8000/en/payments/transaction/failure/',
    )
    return params
