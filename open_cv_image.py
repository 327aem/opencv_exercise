#3강 이미지 불러오기, 5강 이미지 대칭 ,#10강 색 변환, #14강 가장자리 검출
#15강 HSV 공간 및 색상 추출, 16강 배열 병합

import cv2

image = cv2.imread("/Users/jun/image/tomato.jpeg",cv2.IMREAD_ANYCOLOR)
dst = cv2.flip(image,0) #이미지 flip

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2),90,1) #회전 필터 matrix 생성 (중삼점, 각도, 확대 비율)
dst2 = cv2.warpAffine(image,matrix,(width,height)) #마지막 -> 출력이미지의 size

# 색변환
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# 색반전
dst4 = cv2.bitwise_not(image) #이미지 비트에 not연산


#가장자리 검출
canny = cv2.Canny(image,100,120) #하위 임계값, 상위 임계값 -> 상위 임계값을 넘어가면 가장자리로 파악


#HSV
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)

#색상 추출
h=cv2.inRange(h,8,20) #h속 8~20까지 범위 추출
orange = cv2.bitwise_and(hsv,hsv,mask=h) #mask영역에서 src1,src2 영역이 같은 영역만 and
orange = cv2.cvtColor(orange,cv2.COLOR_HSV2BGR)


#범위 배열 병합
# red의 색상은 두가지 범위가 있음, 두가지 범위 모두를 검출하기 위해 두 마스크를 합쳐야함
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0) #1.0 -> 가중치 / 0.0 -> 추가 합

red = cv2.bitwise_and(hsv,hsv,mask=added_red)
red = cv2.cvtColor(red,cv2.COLOR_HSV2BGR)
# cv2.imshow("Moon",image)
# cv2.imshow("dst",dst)
cv2.imshow("red",red)
cv2.waitKey()
cv2.destroyAllWindows()
