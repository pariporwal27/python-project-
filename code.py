import mysql.connector as ms
from prettytable import  PrettyTable 
c=ms.connect(host='localhost',user='root',password='your_new_password' ,database='catcafe')
print("Welcome to PET A CAT <3 CAFE , Hope you have a great day !")
print()
cob=c.cursor()
bill=[]
o=int(input("""Options: 
1. Reservation
2. Menu and Bill
3. Adopt a buddy
4. Donation for pet care
Enter your choice: """))
y=input("Are you a new customer? (yes/no) : ")

if y.lower()=='yes':
    name=input("Enter name : ")
    contact=int(input("Enter contact : "))
    id_no = int(input("Input id : "))
    cob.execute("insert into customer values ( '{}','{}',{}) ".format(name,contact,id_no))
    c.commit()
else :
    id_no = int(input("Input id : "))
    
def func1():
    da=input ("Enter date for event : ")
    t=input("Enter time : ")
    g=int(input("Enter no. of people : "))
    de=input("Decoratation requirement ? (yes/no) : ")
    if de.lower()=="yes":
        th=input("Enter theme : ")
        cob.execute("insert into decor values ('{}' ,'{}',{},'{}')".format(da,t,g,th))
    else:
        cob.execute("insert into decor values ('{}' ,'{}',{},'none')".format(da,t,g))
    print("Reservation done successfully , thanks!")
    print('Visit again!!!!')
    c.commit()   
    
def func2():
    con="true"
    fields1=['id' , 'name' , 'price' ]
    while con=="true" :
        ci=int(input("""Select your food mood :
1.Cake
2.Milkshake 
3.Ice cream
enter choice : """))
        if  ci ==1:
            cob.execute("select * from cake ")
            t1=cob.fetchall()
            table1=PrettyTable()
            table1.field_names = fields1
            table1.add_rows(t1)
            print(table1)
            od=int(input("enter item id :"))
            item=t1[od-1]
            bill.append(item)    
        if  ci ==2:
            cob.execute("select * from cake ")
            t2=cob.fetchall()
            table2=PrettyTable()
            table2.field_names = fields1
            table2.add_rows(t2)
            print(table2)
            od=int(input("Enter item no : "))
            item=t2[od-1]
            bill.append(item)
        if  ci ==3:
            cob.execute("select * from cake ")
            t3=cob.fetchall()
            table3=PrettyTable()
            table3.field_names = fields1
            table3.add_rows(t3)
            print(table3)
            od=int(input("Enter item id : "))
            item=t3[od-1]
            bill.append(item)
        mo=input("Got more item to pick?(yes/no) : ")
        if mo.lower()=="no" :
            con="false"
            
    print()
    print("****************************************************************")
    print ("bill")
    print()
    cob.execute("select * from customer where id={}".format(id_no))
    l=cob.fetchall()
    print("Customer id : " , l[0][2] )
    print("Name : " ,l[0][0] )
    print("Contact : ",l[0][1] )     
    tableb=PrettyTable()
    tableb.field_names = fields1
    tableb.add_rows(bill)
    print(tableb)
    t=0
    for i in  range(len(bill)):
                    c=int(bill[i][2])   
                    t+=c     
    print("Total : ",t)
    if t>500 :
                    e=0.15*t
                    t-=e
                    print("Discount : 15%  ")
                    print("Total prize",t)
    else :
        e=0.05*t
        t-=e
        print("Discount : 5% ")
        print("Total prize =",t)
    print("Visit again!!!") 
   
def func3():
    print("BUDDIES LOADING.....  " )
    fields=['name' , 'breed' , 'age' ]
    table=PrettyTable()
    table.field_names = fields
    cob.execute("select * from data ")
    d=cob.fetchall()
    table.add_rows(d)
    print(table)
    print()
    ch=input( "Ready to pick your buddy ? [yes/no] : ")
    if ch=="yes":
        name=input("Enter name of pet slected :")
        for i in d:
            if i[0]==name:
                cob.execute("delete from data where name='{}'".format(i[0]))
                c.commit()
        print("Congratulations!!")
    else:
        print("It's ohk! maybe some other day ")
        
def func4():
    amount=int(input("Enter amount for donation : "))
    name=input("Enter name : ")
    date= input("Enter date : " )
    cob.execute("Insert into donation values ('{}', '{}', {})".format(name, date, amount))
    c.commit()
    print("Thanks for the donation!! , have a nice day !")


if o==1:
    func1()
if o==2:
    func2()
if o==3:
    func3()
if o==4:
    func4() 
