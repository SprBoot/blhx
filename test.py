import cv2 as cv
from matplotlib import pyplot as plt
import win32
# 图像和模板读取
img = cv.imread('./current.jpg')
template = cv.imread('./2starqing.jpg')
h, w, l = template.shape
# 模板匹配
res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
# 返回图像中最匹配的位置，确定左上角的坐标，并将匹配位置绘制在图像上
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# 使用平方差时最小值为最佳匹配位置
print(max_val)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
# 图像显示
plt.imshow(img[:, :, ::-1])
plt.title("result"), plt.xticks([]), plt.yticks([])
plt.show()
sr = win32.img("Qt5QWindowIcon", "碧蓝航线 - MuMu模拟器", "./sr.jpg")
print(sr)
