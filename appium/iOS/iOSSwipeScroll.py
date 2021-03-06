import time

class SwipeScroll:

    def __init__(self, app):
        self.app = app

    def size(self):
        window_size = self.app.driver.get_window_size()
        max_width = window_size["width"]
        max_height = window_size["height"]
        return max_width, max_height


    def left(self):
        time.sleep(1)
        max_width, max_height = size(self)

        start_x = round(max_width - 10)
        start_y = round(max_height / 2)
        end_x = 5 - start_x
        end_y = 0
        return (start_x, start_y, end_x, end_y)

    #сделать нннадо

    def right(self):
        time.sleep(1)
        max_width, max_height = size(self)

        start_x = 5
        start_y = round(max_height / 2)
        end_x = round(max_width-10)
        end_y = 0
        return (start_x, start_y, end_x, end_y)

    #сделать нннадо
    def up(self):
        time.sleep(1)
        max_width, max_height = size(self)

        start_x = round(max_width / 2)
        start_y = round(max_height - 20)
        end_x = 0
        end_y = -200
        return (start_x, start_y, end_x, end_y)


    def down(self):
        time.sleep(1)
        max_width, max_height = size(self)

        start_x = round(max_width / 2)
        start_y = 20
        end_x = 0
        end_y = 0 - round(max_height - 20)
        return (start_x, start_y, end_x, end_y)


