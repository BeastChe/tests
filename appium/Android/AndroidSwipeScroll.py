import time

def size(self):
    window_size = self.driver.get_window_size()
    max_width = window_size["width"]
    max_height = window_size["height"]
    return max_width, max_height


def left(self):
    time.sleep(2)
    max_width, max_height = size(self)

    start_x = round(max_width-10)
    start_y = round(max_height / 2)
    end_x = 5
    end_y = 0
    return (start_x, start_y, end_x, end_y)


def right(self):
    time.sleep(2)
    max_width, max_height = size(self)

    start_x = 5
    start_y = round(max_height / 2)
    end_x = round(max_width-10)
    end_y = 0
    return (start_x, start_y, end_x, end_y)


def up(self):
    time.sleep(2)
    max_width, max_height = size(self)

    start_x = round(max_width / 2)
    start_y = round(max_height - 20)
    end_x = 0
    end_y = 5
    return (start_x, start_y, end_x, end_y)


def down(self):
    time.sleep(2)
    max_width, max_height = size(self)

    start_x = round(max_width / 2)
    start_y = 100
    end_x = 0
    end_y = round(max_height - 20)
    return (start_x, start_y, end_x, end_y)

