import mysql.connector as a
con=a.connect(host="localhost",user="root",password="12345",database="bank")
import os
from getpass import getpass
def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMNT  SYSTEM")
    print("\t\t\t\t**********************")
    print("\t\t\tCREATED BY :DIVYANSHU VARSHNEY 12th PCM")
    print("\t\t\t\t    HARSH RAGHAV 12th PCM")
    print("\t\t\t\t    JIGYANSHU RAJ GAUTAM 12th PCM")
    input()
    os.system("cls")
def password():
    y=getpass("\t\t\t\tPLEASE ENTER USERNAME:")
    x=getpass("\t\t\t\tPLEASE ENTER PASSWORD:")
    os.system("cls")
    if x =="Divyanshu"and y=="12345678":
        os.system("cls")
        print("\t\t\t\tWELCOME TO THE SYSTEM")
    else:
        print("\t\t\t\tNOT A AUTHORISED USER")
        input()
        Sys.exit(1)
    input()
    os.system("cls")
    
def openAcc():
    n=input("Enter Name:")
    ac=input("Enter Account No.:")
    db=input("Enter D.O.B (DD/MM/YYYY):")
    p=input("Enter Phone No.:")
    ad=input("Enter Address:")
    ob=int(input("Enter Opening Balance:"))
    data1=(n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    os.system("cls")
    print("Data Enter Successfully")
    input()
    os.system("cls")
    main()

def depositAmount():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No.:")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    os.system("cls")
    print("Account Updated Successfully")
    input()
    os.system("cls")
    main()

def witham():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No.")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    os.system("cls")
    print("Account Updated Successfully")
    input()
    os.system("cls")
    main()

def balance():
    ac=input("Enter Account No.:")
    a="select balance from amount where acno =%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    os.system("cls")
    print("Balance For Account:",ac,"is",myresult[0])
    input()
    os.system("cls")
    main()

def dispacc():
    f=0
    ac=input("Enter Account No.:")
    a="select * from account where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchall()
    for i in myresult:
        if i[1]==ac:
            print(i,end=" ")
            input()
            os.system("cls")
            main()
            f=1
            break
    if f==0:
        os.system("cls")
        print("Account Not Found")
        input()
        os.system("cls")
        main()
    
def disacc():
    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM account")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x,end=" ")
        input()
    os.system("cls")
    main()

def closeac():
    ac=input("Enter Account No.:")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    os.system("cls")
    print("Account closed successfully")
    input()
    os.system("cls")
    main()

def main():
    print("""
MAIN MENU
1.OPEN NEW ACCOUNT
2.DEPOSIT AMOUNT
3.WITHDRAW AMOUNT
4.BALANCE ENQUIRY
5.DISPLAY ACCOUNT DETAILS
6.DISPLAY All ACCOUNT DETAILS
7.CLOSE AN ACCOUNT
8.EXIT
""")
    choice=input("Enter Task No.:")
    os.system("cls")
    while True:
        if(choice=='1'):
            openAcc()
        elif(choice=='2'):
            depositAmount()
        elif(choice=='3'):
            witham()
        elif(choice=='4'):
            balance()
        elif(choice=='5'):
            dispacc()
        elif(choice=='6'):
            disacc()
        elif(choice=='7'):
            closeac()
        elif(choice=='8'):
            print("\tTHANKS FOR USING BANK MANAGEMENT SYSTEM")
            input()
            break
        else :
            print("INVALID CHOICE")
            main()
intro()
password()
main()            
input()


        
            
            
    

    


