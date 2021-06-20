#对后台窗口截图
import win32gui, win32ui, win32con
import cv2
import numpy
import pyautogui
import time
import random

def savePic(cls,name):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls,name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    ##方法三（第一部分）：opencv+numpy保存
    ###获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    ##方法三（第二部分）：opencv+numpy保存
    ###PrintWindow成功，保存到文件，显示到屏幕
    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    cv2.imwrite('current.jpg',im_opencv,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) #保存
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd, hWndDC)

def img(cls,name,path):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls,name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    ##方法三（第一部分）：opencv+numpy保存
    ###获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    ##方法三（第二部分）：opencv+numpy保存
    ###PrintWindow成功，保存到文件，显示到屏幕
    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    cv2.imwrite("im_opencv.jpg",im_opencv,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) #保存
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    template = cv2.imread(path)
    im_opencv = cv2.imread('./im_opencv.jpg')
    #im_opencv = cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    res = cv2.matchTemplate(im_opencv, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #H1 = cv2.calcHist([im_opencv], [1], None, [256], [0, 256])
    #H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)  #
    #H2 = cv2.calcHist([template], [1], None, [256], [0, 256])
    #H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)

    # 利用compareHist（）进行比较相似度
    #similarity = cv2.compareHist(H1, H2, 0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd, hWndDC)

    return max_val

def singleClick(path,single,cls,name,picName):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls,name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    ##方法三（第一部分）：opencv+numpy保存
    ###获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    ##方法三（第二部分）：opencv+numpy保存
    ###PrintWindow成功，保存到文件，显示到屏幕
    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    cv2.imwrite(picName,im_opencv,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) #保存
    current = cv2.imread(path)
    template = cv2.imread(single)
    #template = cv2.cvtColor(template, cv2.COLOR_BGRA2RGB)
    h, w, l = template.shape
    # 当前捕捉截图与模板匹配，找到再次出击按钮，模拟鼠标点击操作
    res = cv2.matchTemplate(current, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls, name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    x = left + ((top_left[0] + bottom_right[0]) / 2) + random.uniform(0.2,1.5)
    y = top + ((top_left[1] + bottom_right[1]) / 2) + random.uniform(0.2,1.5)
    pyautogui.click(x,y)

def getStep(cls,name,single):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls,name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    flag = True
    total = time.time()
    startTime = time.time()
    while(flag):
        similarity = img(cls,name)
        if(similarity > 0.7):
            total = time.time() - startTime
            time.sleep(5)
            singleClick('./again.jpg','./finish.jpg',cls,name,'again.jpg')
            flag = False
            print('间隔时间计算完成',total)
    return total

def turn(cls,name,single):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls,name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    flag = True
    while(flag):
        similarity = img(cls, name)
        if (similarity > 0.7):
            time.sleep(5)
            singleClick('./again.jpg','./finish.jpg',cls,name,'again.jpg')
            break

def click(cls,name):
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(cls, name)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    pyautogui.click(left + 300,bot - 100)
