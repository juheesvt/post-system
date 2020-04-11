import random

from core.manage import ObjectManager
from core.objects import Product
from core.settings import DATABASES

#모든 디비 초기상태로 리셋
for DATABASE_KEY in DATABASES:
    OM = ObjectManager(DATABASES[DATABASE_KEY])
    OM.write([])

#TODO: origin db 초기화

#product db 초기화
OM = ObjectManager(DATABASES["PRODUCT_DB"])

for i in range(10):
    price = random.randint(5, 100) * 100
    selling_price = price + random.randint(5, 100) * 10
    OM.create(Product(
        "상품" + str(i),
        price,
        str(i),
        selling_price,
        random.randint(1, 99),
        random.choice([True, False]),
        random.randint(0, 50)
    ))
