from hashlib import md5

pg_order_id=111
pg_merchant_id=535456
pg_amount=100
pg_description='test-bega'
pg_salt='some-salt'



# 'init_payment.php;777;test-bega;535456;23;molbulak;LeFnP16MP6AU6YKc'
data = f'init_payment.php;{pg_amount};{pg_description};{pg_merchant_id};{pg_order_id};{pg_salt};LeFnP16MP6AU6YKc'
ps_sig = md5(data.encode('utf-8')).hexdigest()

# https://api.paybox.money/init_payment.php?pg_order_id=23&pg_merchant_id=535456&pg_amount=25&pg_description=test&pg_salt=molbulak&pg_sig=23febebc43dc0b1d5a15d800841d9d62


post_url = f'https://api.paybox.money/init_payment.php?pg_order_id={pg_order_id}&pg_merchant_id={pg_merchant_id}&pg_amount={pg_amount}&pg_description={pg_description}&pg_salt={pg_salt}&pg_sig={ps_sig}'
print(post_url)