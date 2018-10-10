import util
import PlotChart
import Location
import Sakura
def process(chart):
    i = 0
    while True:
        chart.begin()
        while True:
            chart.attack()
            if chart.end() == 1:
                i += 1
                print("第", i, "轮战斗结束")
                break

if __name__ == '__main__':
    hwnd, name = util.find_window()
    g = input('请输入要刷的图序号:\n'
              '1:3-4\n'
              '2:4-4\n'
              '3:活动图3-10\n'
              '4:活动图3-1')

    if g == '1':
        pos = Location.Location.three_four
        chart = PlotChart.Plot(hwnd, name, pos.value)

    elif g == '2':
        pos = Location.Location.four_four
        chart = PlotChart.Plot(hwnd, name, pos.value)
    elif g == '3':
        pos = Location.Location.Sakura_three_ten
        chart = Sakura.Sakura(hwnd, name, pos.value)
    elif g=='4':
        pos = Location.Location.Sakura_three_one
        chart = Sakura.Sakura(hwnd, name, pos.value)

    process(chart)


















