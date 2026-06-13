import cv2

#read image
img = cv2.imread('colorcolor.jpg')

#resize the image pic size,(image,size)
#another writting way:(image,(0,0),fx=,X,fy=Y) such as (img,(0,0),fx=0.5,fy=0.5),which mean cut a half size,fx is weigh, fy = heigh
img = cv2.resize(img,(300,400))

#show image, ('windows name', pic)
cv2.imshow('img', img)

#waiting time for picture,2000 means 2 second and after that it will close
# if put 0 means forever until you manually close it or type some character from keyboards
cv2.waitKey(0)

