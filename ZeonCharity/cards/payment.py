from hashlib import md5

url = 'https://api.paybox.money/init_payment.php'
pg_order_id=23
pg_merchant_id=535456
pg_amount=25
pg_description='test'
pg_salt=molbulak'
pg_sig={{paybox_signature}}
pg_payment_method='mobile_commerce'


# 'init_payment.php;777;test-bega;535456;23;molbulak;LeFnP16MP6AU6YKc'
data = f'init_payment.php;{pg_amount};{pg_description};{pg_merchant_id};{pg_order_id};molbulak;LeFnP16MP6AU6YKc'

print(data)