import cv2
import face_recognition

def AdminVerify():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        try:
            faceloc = face_recognition.face_locations(frame)[0]
        except:
            faceloc = ()
        cv2.putText(frame, "Face Detected : ", (10, 30), font, 1, (0, 0, 0), 2)
        if (len(faceloc) != 0):
            cv2.putText(frame, "Yes", (270, 30), font, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No", (270, 30), font, 1, (0, 0, 255), 2)
        cv2.namedWindow("Face Detection")
        cv2.moveWindow("Face Detection", 400, 150)
        cv2.imshow("Face Detection", frame)
        cv2.setWindowProperty("Face Detection", cv2.WND_PROP_TOPMOST, 1)

        if len(faceloc) != 0:
            cv2.destroyAllWindows()
            break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    enimg = face_recognition.face_encodings(frame)[0]

    adimg = face_recognition.load_image_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Admin.jpg')
    adimg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    enad = face_recognition.face_encodings(adimg)[0]

    return (face_recognition.compare_faces([enimg],enad))
