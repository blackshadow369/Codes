import cv2
import face_recognition
from copy import  deepcopy

def imagecapture(value,fname,lname):

    cam = cv2.VideoCapture(0)
    while True:
        ret,frame = cam.read()
        dataframe = deepcopy(frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        try:
            faceloc = face_recognition.face_locations(frame)[0]
        except:
            faceloc = ()
        cv2.putText(frame, "Face Detected : ", (10, 30), font, 1, (0, 0, 0), 2)
        if(len(faceloc)!=0):
            cv2.putText(frame, "Yes", (270, 30), font, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No", (270, 30), font, 1, (0, 0, 255), 2)
        cv2.namedWindow("Face Detection")
        cv2.moveWindow("Face Detection",400,150)
        cv2.imshow("Face Detection", frame)
        cv2.setWindowProperty("Face Detection",cv2.WND_PROP_TOPMOST,1)


        k = cv2.waitKey(1)   # holds screen
        if len(faceloc)!=0 and  k%256 == 32:
            frame = deepcopy(dataframe)
            cv2.putText(frame, "   SPACE to submit || ESC to retake ", (0, 450), font, 1, (255, 255, 255), 2)
            cv2.namedWindow("Final Request")
            cv2.moveWindow("Final Request",400,150)
            cv2.imshow("Final Request",frame)
            cv2.destroyWindow("Face Detection")


            tester = cv2.waitKey(0)
            if(tester%256==32):
                img = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{}_{}_{}.jpeg".format(fname,lname,value)
                cv2.imwrite(img, dataframe)
                break
            else:
                print("Photo was not good. Taking again")
                cv2.destroyWindow("Final Request")
                continue
    print("FACE ID CREATED ")
    cam.release()
    cv2.destroyAllWindows()


