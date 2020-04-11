from core.manage import ObjectManager
from core.settings import DATABASES

transaction_manager = ObjectManager(DATABASES["TRANSACTION_DB"])
product_manager = ObjectManager(DATABASES["PRODUCT_DB"])
origin_product_manager = ObjectManager(DATABASES["ORIGIN_PRODUCT_DB"])

