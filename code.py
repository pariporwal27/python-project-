import mysql.connector as ms
from prettytable import  PrettyTable 
c=ms.connect(host='localhost',user='root',password='your_new_password' ,database='catcafe')
print("welcome to PET A CAT <3 CAFE , hope you have a great day !")
print()
cob=c.cursor()
bill=[]
o=int(input("""options: 
1. reservation
2. menu and bill
3. adopt a buddy
4. donation for pet care
Enter your choice: """))
y=input("are you a new customer? (yes/no) : ")
if y=='yes':
    name=input("enter name : ")
    contact=int(input("enter contact : "))
    id_no = int(input("input id : "))
    cob.execute("insert into customer values ( '{}','{}',{}) ".format(name,contact,id_no))
    c.commit()
else :
    id_no = int(input("input id : "))
def func1():
    da=input ("enter date for event : ")
    t=input("enter time : ")
    g=int(input("enter no. of people : "))
    de=input("decoratation requirement ? (yes/no) : ")
    if de.lower()=="yes":
        th=input("enter theme : ")
        cob.execute("insert into decor values ('{}' ,'{}',{},'{}')".format(da,t,g,th))
    else:
        cob.execute("insert into decor values ('{}' ,'{}',{},'none')".format(da,t,g))
    print("reservation done successfully , thanks!")
    print('visit again!!!!')
    c.commit()
    
def func2():
    con="true"
    fields1=['id' , 'name' , 'price' ]
    while con=="true" :
        ci=int(input("""select your food mood :
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
            od=int(input("enter item no : "))
            item=t2[od-1]
            bill.append(item)
        if  ci ==3:
            cob.execute("select * from cake ")
            t3=cob.fetchall()
            table3=PrettyTable()
            table3.field_names = fields1
            table3.add_rows(t3)
            print(table3)
            od=int(input("enter item id : "))
            item=t3[od-1]
            bill.append(item)
        mo=input("got more item to pick?(yes/no) : ")
        if mo=="no" :
            con="false"
    print()
    print("****************************************************************")
    print ("bill")
    print()
    cob.execute("select * from customer where id={}".format(id_no))
    l=cob.fetchall()
    print("customer id : " , l[0][2] )
    print("name : " ,l[0][0] )
    print("contact : ",l[0][1] )     
    tableb=PrettyTable()
    tableb.field_names = fields1
    tableb.add_rows(bill)
    print(tableb)
    t=0
    for i in  range(len(bill)):
                    c=int(bill[i][2])   
                    t+=c     
    print("total : ",t)
    if t>500 :
                    e=0.15*t
                    t-=e
                    print("discount : 15%  ")
                    print("total prize",t)
    else :
        e=0.05*t
        t-=e
        print("discount : 5% ")
        print("total prize =",t)
    print("visit again!!!") 
   

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
    ch=input( "ready to pick your buddy ? [yes/no] : ")
    if ch=="yes":
        name=input("enter name of pet slected :")
        for i in d:
            if i[0]==name:
                cob.execute("delete from data where name='{}'".format(i[0]))
                c.commit()
        print("Congratulations!!")
    else:
        print("it's ohk! maybe some other day ")
def func4():
    amount=int(input("enter amount for donation : "))
    name=input("enter name : ")
    date= input("enter date : " )
    cob.execute("insert into donation values ('{}', '{}', {})".format(name, date, amount))
    c.commit()
    print("thanks for the donation!! , have a nice day !")


if o==1:
    func1()
if o==2:
    func2()
if o==3:
    func3()
if o==4:
    func4() 
