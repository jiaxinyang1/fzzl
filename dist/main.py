import cv2
import win32api
import win32con
import win32gui
import win32ui
from PIL import ImageGrab
def getloaction(img1,img2):
    imgsr = cv2.imread(img1)
    imgtm = cv2.imread(img2)

    imgtmh1 = imgtm.shape[0]
    imgtmw1 = imgtm.shape[1]


    res = cv2.matchTemplate(imgsr, imgtm, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    img = cv2.rectangle(imgsr, max_loc, (max_loc[0] + imgtmw1, max_loc[1] + imgtmh1), (0, 0, 255), 2)
    x = (max_loc[0] + max_loc[0] + imgtmw1) // 2
    y = (max_loc[1] + max_loc[1] + imgtmh1) // 2
    return (x,y)


def findwindow():
    name = input("请输入模拟器的序列")
    classname = "Qt5QWindowIcon"
    firstname = "夜神模拟器"
    lastname = "-Android4.4.2"
    if (name == '0'):
        windowname = firstname
    else:
        windowname = firstname + name + lastname

    hwnd=win32gui.FindWindow(classname,windowname)
    hwndchildlist= []
    hwnd_get=0
    win32gui.EnumChildWindows(hwnd, lambda hwnd,param:param.append(hwnd),hwndchildlist)
    for hwnd_ in hwndchildlist:
        windowname_=win32gui.GetWindowText(hwnd_)
        classname_=win32gui.GetClassName(hwnd_)

        if(windowname_ =="ScreenBoardClassWindow"  ):
            hwnd_get=hwnd_


    return hwnd_get,name


def clickpos(handle,x,y):
    tmp=win32api.MAKELONG(x,y)

    win32api.SendMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32api.Sleep(300)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    win32api.SendMessage(handle, win32con.WM_MOUSEMOVE, win32con.WM_MOUSEMOVE, tmp)
    return 1



def screenshot(hwnd,name):
    win32api.Sleep(500)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)

    img_dc =mfcDC
    mem_dc =saveDC
    mem_dc.BitBlt((0, 0), (w, h), img_dc, (0, 0), win32con.SRCCOPY)

    saveBitMap.SaveBitmapFile(mem_dc, 'temp\\'+name+'\\screenshot.png')
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    return 1


def begin(hwnd,name,select):

    if(select=='2'):
        #4-4
        clickpos(hwnd, 1040, 411)
    else:
        #3-4
        clickpos(hwnd, 1047, 229)
    win32api.Sleep(1000)
    screenshot(hwnd,name)
    x, y = getloaction('temp\\'+name+'\\screenshot.png', "selectterm.png")
    while(x<1000):
        clickpos(hwnd, 1047, 229)
        win32api.Sleep(1000)
        screenshot(hwnd,name)
        x, y = getloaction('temp\\'+name+'\\screenshot.png', "selectterm.png")


    clickpos(hwnd, 1001, 571)
    win32api.Sleep(1000)
    clickpos(hwnd, 999, 571)
    win32api.Sleep(1000)
    clickpos(hwnd, 1169, 669)


def attack(hwnd,name):
    screenshot(hwnd,name)
    # 战斗
    x,y=getloaction('temp\\'+name+'\\screenshot.png',"zhandouclick.png")
    if(x>1000 and y>400):
        win32api.Sleep(800)
        clickpos(hwnd,x,y)
        win32api.Sleep(1000)
        clickpos(hwnd, 1194, 172)


    else:
        clickpos(hwnd,516,456)


def home(hwnd,name):
    screenshot(hwnd,name)
    x,y =getloaction('temp\\'+name+'\\screenshot.png',"meiri.png")
    if(x==1220):
        return 1
    else:
        return 0

if __name__ == '__main__':

    hwnd,name = findwindow()
    g=input("请选择要刷的图: 1:3-4,2:4-4")
    i=0
    while (1):
        begin(hwnd,name,g)
        while (1):
            attack(hwnd,name)
            if (home(hwnd,name) == 1):
                i += 1
                print("第", i, "轮战斗结束")
                break












