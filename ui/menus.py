from core.machine import product_manager, beep_queue, transaction_manager
from core.objects import Transaction


class Menu:
    def __init__(self, name):
        self.__name = name

    def run(self):
        pass

    def get_name(self):
        return self.__name


class Beep(Menu):
    def __init__(self):
        super().__init__("바코드 찍기")

    def compare_code(self, code):
        return lambda transaction: transaction.get_code() == code

    def run(self):
        print("코드를 입력하세요 : ")
        code = input()

        product = product_manager.find(self.compare_code(code))

        print(product)
        beep_queue.append(product)


class Pay(Menu):
    def __init__(self):
        super().__init__("결제하기")
        self.CARD = 1
        self.CASH = 2
        self.CANCEL = 3

    def compare_id(self, id):
        return lambda product: product.get_id() == id

    def run(self):
        transaction = Transaction()

        for front in beep_queue:
            transaction.append_products(front)

        print("총비용 : {}원".format(transaction.get_total_price()))
        print("1. 카드 2. 현금 3. 결제 취소")

        payment_type = int(input())

        if payment_type == self.CARD:
            transaction.set_payment_type(self.CARD)
            transaction.set_is_complete(True)
        elif payment_type == self.CASH:
            transaction.set_payment_type(self.CASH)
            transaction.set_is_complete(True)
        elif payment_type == self.CANCEL:
            transaction.set_is_complete(False)
        else:
            # TODO exception
            return SystemError
        if transaction.get_is_complete():
            # 상품 갯수 갱신
            for product in transaction.get_products():
                if product.get_event():
                    product.set_count(product.get_count() - 2)
                else:
                    product.set_count(product.get_count() - 1)
                product_manager.update(self.compare_id(product.get_id()), product)

        # 트랜젝션 생성
        transaction_manager.create(transaction)
        # 빕 큐 초기화
        beep_queue.clear()

class Exit(Menu) :
    def __init__(self):
        super().__init__("시스템 종료")

    def run(self):
        exit()