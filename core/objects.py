"""
서버에서 제공해주는 품목에 대한 데이터는 POST SYSTEM에서 변경하면 안되므로 setter는 없다.
"""


class Object:
    def __init__(self):
        self.__id

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id


class OriginProduct(Object):
    def __init__(self, name=None,
                 price=None,
                 code=None,
                 selling_price=None):
        self.__name = name
        self.__price = price  # 사는 가격
        self.__code = code
        self.__selling_price = selling_price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_code(self):
        return self.__code

    def get_selling_price(self):
        return self.__selling_price


class Product(OriginProduct):
    def __init__(self, name=None,
                 price=None,
                 code=None,
                 selling_price=None,
                 count=None,
                 event=None,
                 discount=None):
        super().__init__(name, price, code, selling_price)
        self.__count = count
        self.__event = event
        self.__discount = discount  # 할인율

    def __str__(self):
        return "상품명 : {}, 희망소비자가격 : {}, 이벤트 여부 : {}, 할인률 : {} ".format(
            self.get_name(),
            self.get_selling_price(),
            self.get_event(),
            self.get_discount()
        )

    def get_count(self):
        return self.__count

    def get_event(self):
        return self.__event

    def get_discount(self):
        return self.__discount

    def set_count(self, count):
        self.__count = count

    def set_event(self, event):
        self.__event = event

    def set_discount(self, discount):
        self.__discount = discount


class Transaction(Object):
    def __init__(self):
        self.__products = []
        self.__total_price = 0
        self.__payment_type = None
        self.__is_complete = None

    def append_products(self, object):
        self.__products.append(object)
        self.__total_price += object.get_selling_price() - int(object.get_selling_price() / 100 * object.get_discount())

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def get_products(self):
        return self.__products

    def get_total_price(self):
        return self.__total_price
    def get_is_complete(self):
        return self.__is_complete
    def set_is_complete(self,is_complete):
        self.__is_complete = is_complete