import util
from PlotChart import Plot
class Sakura(Plot):
    def __init__(self, hwnd, name, pos):
        self.hwnd = hwnd
        self.name = name
        self.pos_x = pos.x
        self.pos_y = pos.y

    def begin(self):
        util.click_pos(self.hwnd, self.pos_x, self.pos_y)
        util.sleep(1000)
        util.screen_shot(self.hwnd, self.name)
        x, y = util.get_location('temp\\' + self.name + '\\screenshot.png', 'selectterm.png')
        while x < 1000:
            util.click_pos(self.hwnd, self.pos_x, self.pos_y)
            util.sleep(1000)
            util.screen_shot(self.hwnd, self.name)
            x, y = util.get_location('temp\\' + self.name + '\\screenshot.png', 'selectterm.png')

        util.click_pos(self.hwnd, 1002, 573)

    def end(self):
        util.screen_shot(self.hwnd, self.name)
        x, y = util.get_location('temp\\' + self.name + '\\screenshot.png', 'shen.png')
        if x ==156:
            return 1
        else:
            return 0