
import win32
import time

while 1 == 1:
    flag = True
    win32.singleClick('./current.jpg', "./seven.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
    time.sleep(1)
    win32.singleClick('./current.jpg', "./start.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
    time.sleep(1)
    win32.singleClick('./current.jpg', "./start.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
    time.sleep(5)
    boss = True
    initial = 1
    while(boss):
        tempFlag = True
        while(tempFlag):
            onestargold = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./1stargold.jpg")
            onestarqing = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./1starqing.jpg")
            onestarzhong = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./1starzhong.jpg")
            twostarqing = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./2starqing.jpg")
            twostarzhong = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./2starzhong.jpg")
            path = "./1stargold.jpg"
            tu = '金子船'
            if(onestargold > 0.4):
                path = "./1stargold.jpg"
            elif(onestarqing > 0.4):
                path = "./1starqing.jpg"
                tu = '1星轻'
            elif(onestarzhong > 0.4):
                path = "./1starzhong.jpg"
                tu = '1星重'
            elif(twostarqing > 0.4):
                path = "./2starqing.jpg"
                tu = '2星轻'
            elif (twostarzhong > 0.4):
                path = "./2starzhong.jpg"
                tu = '2星重'
            wei = True
            while wei:
                tuo = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./info.jpg")
                if tuo > 0.8:
                    time.sleep(1)
                    win32.singleClick('./current.jpg', "./sure.jpg", "Qt5QWindowIcon",
                                      "碧蓝航线 - MuMu模拟器", 'current.jpg')
                else:
                    wei = False
            win32.singleClick('./current.jpg', path, "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
            print('选择了{}'.format(tu))
            temp = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chu.jpg")
            if (temp > 0.8):
                print('到达图准备出击')
                flag = True
                win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                while (flag):
                    max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                    if (max > 0.85):
                        print('出击成功')
                        initial = initial + 1
                        time.sleep(1)
                        win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                        time.sleep(3)
                        win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                        confirmFlag = True
                        while(confirmFlag):
                            srFlag = True
                            while (srFlag):
                                sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                if (sr > 0.8):
                                    time.sleep(1)
                                    win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                else:
                                    srFlag = False
                            time.sleep(2)
                            con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                            if(con > 0.9):
                                win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器",
                                                  'current.jpg')
                                time.sleep(5)
                                iboss = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./boss.jpg")
                                if (initial == 6):
                                    boss = False
                                    tempFlag = False
                                if (iboss > 0.95):
                                    tempFlag = False
                                    boss = False
                                confirmFlag = False
                                flag = False
            danger = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./guibi.jpg")
            if (danger > 0.95):
                win32.singleClick('./current.jpg', './guibi.jpg', "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                print('规避成功')
                time.sleep(3)
                chu = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chu.jpg")
                if (chu > 0.95):
                    print('规避失败，过图')
                    win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                    dangerFlag = True
                    while (dangerFlag):
                        max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                        if (max > 0.85):
                            time.sleep(1)
                            win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                            time.sleep(3)
                            win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                            confirmFlag = True
                            while (confirmFlag):
                                srFlag = True
                                while (srFlag):
                                    sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                    if (sr > 0.8):
                                        time.sleep(1)
                                        win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                    else:
                                        srFlag = False
                                time.sleep(2)
                                con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                                if (con > 0.9):
                                    win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon",
                                                      "碧蓝航线 - MuMu模拟器",
                                                      'current.jpg')
                                    time.sleep(5)
                                    iboss = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./boss.jpg")
                                    if (iboss > 0.95):
                                        tempFlag = False
                                        boss = False
                                    if (initial == 6):
                                        boss = False
                                        tempFlag = False
                                    confirmFlag = False
                                    dangerFlag = False
    time.sleep(5)
    wen = True
    while(wen):
        number = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./wenhao.jpg")
        if(number < 0.6):
            print('物资采集完成')
            wei = True
            while (wei):
                tuo = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./info.jpg")
                if (tuo > 0.8):
                    time.sleep(1)
                    win32.singleClick('./current.jpg', "./sure.jpg", "Qt5QWindowIcon",
                                      "碧蓝航线 - MuMu模拟器", 'current.jpg')
                else:
                    wei = False
            win32.singleClick('./current.jpg', "./boss.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
            print('boss图')
            temp = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chuji.jpg")
            if (temp > 0.8):
                print('到达boss')
                tflag = True
                win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器",
                                  'current.jpg')
                while (tflag):
                    max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                    if (max > 0.85):
                        print('boss出击成功')
                        time.sleep(1)
                        win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                        time.sleep(3)
                        win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                        confirmFlag = True
                        while (confirmFlag):
                            srFlag = True
                            while (srFlag):
                                sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                if (sr > 0.8):
                                    time.sleep(1)
                                    win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                else:
                                    srFlag = False
                            time.sleep(2)
                            con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                            if (con > 0.9):
                                win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon",
                                                  "碧蓝航线 - MuMu模拟器",
                                                  'current.jpg')
                                time.sleep(5)
                                confirmFlag = False
                                tflag = False
                                wenFlag = False
                                wen = False
        else:
            wenFlag = True
            while(wenFlag):
                danger = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./guibi.jpg")
                if (danger > 0.95):
                    win32.singleClick('./current.jpg', './guibi.jpg', "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                    print('规避成功')
                    time.sleep(3)
                    chu = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chu.jpg")
                    if (chu > 0.95):
                        print('规避失败，过图')
                        win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器",
                                          'current.jpg')
                        dangerFlag = True
                        while (dangerFlag):
                            max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                            if (max > 0.85):
                                time.sleep(1)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                time.sleep(3)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                confirmFlag = True
                                while (confirmFlag):
                                    srFlag = True
                                    while (srFlag):
                                        sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                        if (sr > 0.8):
                                            time.sleep(1)
                                            win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                        else:
                                            srFlag = False
                                    time.sleep(2)
                                    con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                                    if (con > 0.9):
                                        win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon",
                                                          "碧蓝航线 - MuMu模拟器",
                                                          'current.jpg')
                                        time.sleep(5)
                                        iboss = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./boss.jpg")
                                        if (iboss > 0.95):
                                            tempFlag = False
                                            boss = False
                                        confirmFlag = False
                                        dangerFlag = False
                win32.singleClick('./current.jpg', './wenhao.jpg', "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                error = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./error.jpg")
                if (error > 0.6):
                    wei = True
                    while (wei):
                        tuo = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./info.jpg")
                        if (tuo > 0.8):
                            time.sleep(1)
                            win32.singleClick('./current.jpg', "./sure.jpg", "Qt5QWindowIcon",
                                              "碧蓝航线 - MuMu模拟器", 'current.jpg')
                        else:
                            wei = False
                    win32.singleClick('./current.jpg', "./boss.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                    print('boss图')
                    temp = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chu.jpg")
                    if (temp > 0.8):
                        print('到达boss')
                        tflag = True
                        win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器",
                                          'current.jpg')
                        while (tflag):
                            max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                            if (max > 0.85):
                                print('boss出击成功')
                                time.sleep(1)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                time.sleep(3)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                confirmFlag = True
                                while (confirmFlag):
                                    srFlag = True
                                    while (srFlag):
                                        sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                        if (sr > 0.8):
                                            time.sleep(1)
                                            win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                        else:
                                            srFlag = False
                                    time.sleep(2)
                                    con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                                    if (con > 0.9):
                                        win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon",
                                                          "碧蓝航线 - MuMu模拟器",
                                                          'current.jpg')
                                        time.sleep(5)
                                        confirmFlag = False
                                        tflag = False
                                        wenFlag = False
                                        wen = False
                time.sleep(2)
                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                test = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./wenhao.jpg")
                if (test < 0.6):
                    win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                    time.sleep(1)
                    wei = True
                    while (wei):
                        tuo = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./info.jpg")
                        if (tuo > 0.8):
                            time.sleep(1)
                            win32.singleClick('./current.jpg', "./sure.jpg", "Qt5QWindowIcon",
                                              "碧蓝航线 - MuMu模拟器", 'current.jpg')
                        else:
                            wei = False
                    win32.singleClick('./current.jpg', "./boss.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", 'current.jpg')
                    print('boss图')
                    temp = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./chu.jpg")
                    if (temp > 0.8):
                        print('到达boss')
                        tflag = True
                        win32.singleClick('./current.jpg', "./chu.jpg", "Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器",
                                          'current.jpg')
                        while (tflag):
                            max = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./win.jpg")
                            if (max > 0.8):
                                print('boss出击成功')
                                time.sleep(1)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                time.sleep(3)
                                win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                confirmFlag = True
                                while (confirmFlag):
                                    srFlag = True
                                    while (srFlag):
                                        sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
                                        if (sr > 0.8):
                                            time.sleep(1)
                                            win32.click("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器")
                                        else:
                                            srFlag = False
                                    time.sleep(2)
                                    con = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./confirm.jpg")
                                    if (con > 0.9):
                                        win32.singleClick('./current.jpg', "./confirm.jpg", "Qt5QWindowIcon",
                                                          "碧蓝航线 - MuMu模拟器",
                                                          'current.jpg')
                                        time.sleep(5)
                                        confirmFlag = False
                                        tflag = False
                                        wenFlag = False
                                        wen = False
    time.sleep(5)


