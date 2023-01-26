import mysql.connector
import cv2
import face_recognition
from copy import  deepcopy
import numpy as np
import io
from PIL import  Image
import datetime
from Key_verification import *
dbms = mysql.connector.connect(
    host='localhost',
    user='root',
    password='karan',
    database='training'
    )
mycur = dbms.cursor()

def Validator():

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

    s = 'select * from auth'
    mycur.execute(s)
    result = mycur.fetchall()
    dataframe = cv2.cvtColor(dataframe,cv2.COLOR_BGR2RGB)
    encodeimg = face_recognition.face_encodings(dataframe)[0]

    for row in result:
        img = row[5]   #face_recognition.load_image_file(row[3])
        image = Image.open(io.BytesIO(img))
        im_arr = np.array(image)
        #print(a_ar)

        renimg2 = cv2.cvtColor(im_arr,cv2.COLOR_BGR2RGB)
        encodeimg2 = face_recognition.face_encodings(renimg2)[0]
        rs = face_recognition.compare_faces([encodeimg],encodeimg2)
        if(rs[0]==True):
            print("User name : {} {}".format(row[1],row[2]))
            print("FACE ID authetication complete ")
            ps = input("Enter password : ")
            if ps == row[3]:
                print('PASSWORD authetication complete ')
                ph = key_identifier()
                if ph == row[4]:
                    print('PHYSCIAL KEY authentication complete ')
                    print('Authentication complete ')
                    print("WELCOME {} {} ".format(row[1],row[2]))
                    file = open('D:/Project final/Logs.txt','a')
                    s = ('{} {} logged in at {}'.format(row[1],row[2],datetime.datetime.now()))
                    file.write('\n')
                    file.write(s)
                    file.close()
                else:
                    break
            else:
                break
            exit(0)
    print("ACCESS DENIED ")
    print("Aborting process")


#calling function
#Validator()

