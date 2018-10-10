import cv2
import win32api
import win32con
import win32gui
import win32ui
def sleep(time):
    win32api.Sleep(time)

def get_location(img1,img2):
    imgsr = cv2.imread(img1)
    imgtm = cv2.imread(img2)

    imgtmh1 = imgtm.shape[0]
    imgtmw1 = imgtm.shape[1]


    res = cv2.matchTemplate(imgsr, imgtm, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    img = cv2.rectangle(imgsr, max_loc, (max_loc[0] + imgtmw1, max_loc[1] + imgtmh1), (0, 0, 255), 2)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    x = (max_loc[0] + max_loc[0] + imgtmw1) // 2
    y = (max_loc[1] + max_loc[1] + imgtmh1) // 2
    return x,y

def find_window():
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

def click_pos(handle,x,y):
    tmp=win32api.MAKELONG(x,y)

    win32api.SendMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32api.Sleep(300)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    win32api.SendMessage(handle, win32con.WM_MOUSEMOVE, win32con.WM_MOUSEMOVE, tmp)
    return 1

def screen_shot(hwnd,name):
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
