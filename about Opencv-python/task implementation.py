import cv2 as cv

filename = '1.jpg'
img_original = cv.imread(filename)
img_rgb = cv.cvtColor(img_original, cv.COLOR_BGR2RGB)
img_lab = cv.cvtColor(img_rgb, cv.COLOR_BGR2Lab)
cv.imshow('RGB', img_rgb)
cv.waitKey(0)
cv.imshow('LAB', img_lab)
cv.waitKey(0)
im_gray = cv.imread("1.jpg", cv.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv.threshold(im_gray, 128, 255, cv.THRESH_OTSU)
cv.imshow('gray', im_gray)
cv.waitKey(0)
cv.imshow('Binary', im_bw)
cv.waitKey(0)


im = cv.imread("1.jpg")
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im, contours, 270, (30, 100, 0), 10)
cv.imshow('Contours', im)

cv.drawContours(im, contours, 270, (255, 0, 255), 10)
cv.imshow('Contours', im)


cv.waitKey(0)
S = []
for i in range(300):
    x = []
    cnt = contours[i]
    x.append(cv.contourArea(cnt))
    x.append(i)
    i =+ 1
    S.append(x)
S.sort()
print(S)


image = cv.imread("1.jpg")
b, g, r = cv.split(image)

cv.imshow('Blue', b)
cv.waitKey(0)
cv.imshow('Green', g)
cv.waitKey(0)
cv.imshow('Red', r)
cv.waitKey(0)