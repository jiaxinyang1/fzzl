import util
class Plot(object):
    def __init__(self,hwnd,name,pos):
        self.hwnd=hwnd
        self.name=name
        self.pos_x=pos.x
        self.pos_y=pos.y

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

        util.click_pos(self.hwnd, 1001, 571)
        util.sleep(1000)
        util.click_pos(self.hwnd, 999, 571)
        util.sleep(1000)
        util.click_pos(self.hwnd, 1169, 669)
    def attack(self):
        util.screen_shot(self.hwnd,self.name)
        x,y=util.get_location('temp\\'+self.name+'\\screenshot.png','zhandouclick.png')

        if x>1000 and y>400:
            util.sleep(1000)
            util.click_pos(self.hwnd,x,y)
            self.sell()
            util.sleep(1000)
            util.click_pos(self.hwnd, 1194, 172)
        else:
            util.click_pos(self.hwnd, 516, 456)

    def sell(self):
        util.screen_shot(self.hwnd,self.name)
        x,y=util.get_location('temp\\'+self.name+'\\screenshot.png','sell.png')
        if x==760:
            util.click_pos(self.hwnd,x,y)
            util.sleep(1000)
            for i in range(0,7):
                util.click_pos(self.hwnd,109+i*177,245)
                util.sleep(300)
            for i in range(0, 7):
                util.click_pos(self.hwnd, 109 + i * 177, 422)
                util.sleep(300)
            util.sleep(1000)
            util.click_pos(self.hwnd,1176,685)
            util.sleep(1000)
            util.click_pos(self.hwnd,781,540)
            util.sleep(1000)
            util.click_pos(self.hwnd, 516, 456)

    def end(self):
        util.screen_shot(self.hwnd,self.name)
        x,y=util.get_location('temp\\' + self.name + '\\screenshot.png', 'meiri.png')
        if (x == 1220):
            return 1
        else:
            return 0