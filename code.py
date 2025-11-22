from prettytable import PrettyTable 
print("welcome to PET A CAT <3 CAFE , hope you have a good day")
print()
o=int(input("""options: 
1. reservation
2. menu and bill
3. adoapt a buddy
4.donation for pet care
Enter your choice: """))
y=input("are you a new customer? ")
name=input("enter name : ")
contact=int(input("enter contact : "))
id_no = int(input("input id :"))
bill=[]
def func1():
    da=input ("enter date for event : ")
    t=input("enter time")
    g=int(input("enter no. of people : "))
    de=input("decoratation requirement ? (yes/no) : ")
    if de.lower()=="yes":
        th=input("enter theme : ")
    print("reservation done successfully , thanks!")
    print('visit again!!!!')
    
def func2():
    con="true"
    fields1=['id' , 'name' , 'price' ]
    while con=="true" :
        ci=int(input("""select your food mood :
1.Cakes
2.Milkshakes 
3.Ice cream
enter choice : """))
        if  ci ==1:
            rec1=[]
            table1=PrettyTable()
            table1.field_names = fields1
            c=open("cake.txt","r")
            for i in range(4):
                row=c.readline()
                row = row.split(",")
                row.pop()
                rec1.append(row)
            table1.add_rows(rec1)
            print(table1)
            od=int(input("enter item id :"))
            item=rec1[od-1]
            bill.append(item)
            
        if  ci ==2:
            rec2=[]
            table2=PrettyTable()
            table2.field_names = fields1
            c=open("mil.txt","r")
            for i in range(4):
                row=c.readline()
                row = row.split(",")
                row.pop()
                rec2.append(row)
            table2.add_rows(rec2)
            print(table2)
            od=int(input("enter item no : "))
            item=rec2[od-1]
            bill.append(item)
        if  ci ==3:
            rec3=[]
            table3=PrettyTable()
            table3.field_names = fields1
            c=open("ice.txt","r")
            for i in range(4):
                row=c.readline()
                row = row.split(",")
                row.pop()
                rec3.append(row)
            table3.add_rows(rec3)
            print(table3)
            od=int(input("enter item id : "))
            item=rec3[od-1]
            bill.append(item)
        mo=input("got more item to pick?(yes/no) : ")
        if mo=="no" :
            con="false"
    print()
    print("******************************************************************")
    print ("bill")
    print()
    print("customer id : " , id_no )
    print("name : " ,name )
    print("contact : ",contact )     
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
                    print("discount : 15%: total prize",t)
    else :
        e=0.05*t
        t-=e
        print("discount : 5%: total prize =",t)
    print("visit again!!!") 
   

def func3():
    print("BUDDIES LOADING.....  " )
    f=open('data.txt','r')
    fields=['name' , 'breed' , 'age' ]
    table=PrettyTable()
    table.field_names = fields
    rec=[]
    for i in range(4):
        row=f.readline()
        row = row.split(",")
        row.pop()
        rec.append(row)
    table.add_rows(rec)
    print(table)
    print()
    ch=input( "ready to pick your buddy ? [y/n] : ")
    if ch=="y":
        name=input("enter name of pet slected :")
        rec2=[]
        f.seek(0)
        for i in range(4):
            row=f.readline()
            row = row.split(",")
            if row[0]!=name:
                row=str(row)
                rec2.append(row)
            g=open("data.txt","a")
            g.writelines(rec2)
            g.flush()
        print("Congratulations!!")
    else:
        print("it's ohk! maybe some other day ")
def func4():
    amount=int(input("enter amount for donation : "))
    name=input("enter name : ")
    date= input("enter date" )
    h=open("donation.txt","a")
    dd=[name,amount,date]
    dd=str(dd)
    h.writelines(dd)
    h.flush()
    print("thanks for the donation!! , have a nice day")


if o==1:
    func1()
if o==2:
    func2()
if o==3:
    func3()
if o==4:
    func4()