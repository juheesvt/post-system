from core.machine import is_running
from ui.menus import Pay, Beep, Exit


class UI:
    def __init__(self):
        self.__menus = [Beep(), Pay(), Exit()]

    def draw(self):
        MENU_UI = " ".join(
            map(lambda enum: "{}. {}".format(str(enum[0] + 1), enum[1].get_name()),
                enumerate(self.__menus)
                )
        )
        print(MENU_UI)

    def run(self):
        while is_running:
            self.draw()
            # try:
            order = int(input())
            self.__menus[order - 1].run()
        # except:
    # TODO: 예외처리

    # pass
