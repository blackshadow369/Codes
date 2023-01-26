import mysql.connector
from Image_taker import *
from Adminverification import AdminVerify
from Password_creator import password_maker
from Key_creation import key_maker
dbms = mysql.connector.connect(
    host='localhost',
    user='root',
    password='karan',
    database='training'
    )
mycur = dbms.cursor()
def new_user(v):
    mycur = dbms.cursor()
    res = AdminVerify()
    if res[0]==False:
        print("Acsess denied.")
        print("Aborting Procedure.")
    passwd = input("Enter Admin password :")
    if passwd!="Karan12345":
        print("Access denied.")
        print("Aborting Procedure.")
        exit(0)
    print('WELCOME ADMIN')
    print('Enter the details of new user ')
    f_name = input("Enter your firstname : ")
    l_name = input("Enter your lastname : ")
    imagecapture(v,f_name,l_name)
    ps = password_maker()
    ph = key_maker(ps)
    img = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{}_{}_{}.jpeg".format(f_name,l_name,v)
    with open(img,'rb') as file:
        binary_data = file.read()
    s = '''insert into auth(Id,firstName,lastName,Password,HashKey,Img) value (%s,%s,%s,%s,%s,%s)'''
    values = (v,f_name,l_name,ps,ph,binary_data)
    #print(s)
    mycur.execute(s,values)
    dbms.commit()
    file.close()



def uid():
    mycur = dbms.cursor()
    s = 'select max(Id) from auth'
    mycur.execute(s)
    result = mycur.fetchall()
    try:
        value = int(result[0][0])
    except:
        value = 0
    new_user((value+1))
    dbms.commit()
    dbms.close()



