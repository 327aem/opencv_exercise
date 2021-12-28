#4강 비디오 출력, 20강 비디오 캡쳐 및 녹화
import datetime
import cv2

capture = cv2.VideoCapture("/Users/jun/video/permission_to_dance_ex.mp4")
# while cv2.waitKey(33)<0:
#     if capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT):
#         capture.set(cv2.CAP_PROP_POS_FRAMES,0)
#     ret,frame = capture.read()
#     cv2.imshow("video",frame)

#동영상 화면 캡처 및 녹화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT):
       capture.set(cv2.CAP_PROP_POS_FRAMES,0)
    ret,frame = capture.read()
    cv2.imshow("video",frame)
    
    now = datetime.datetime.now().strftime("%d_%H-%M-%s")
    key = cv2.waitKey(33)
    
    if key == 27: #esc
        break
    elif key == 26: #ctl+z
        print("캡처")
        cv2.imwrite("/Users/jun/image/"+str(now)+".jpeg",frame)
    elif key == 24: #ctl+x
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("/Users/jun/video/" + str(now) + ".mp4", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 3: #ctl+c
        print("녹화 중지")
        record = False
        video.release()
    if record == True: 
        print("녹화중..")
        video.write(frame)


capture.release()
cv2.destroyAllWindows()