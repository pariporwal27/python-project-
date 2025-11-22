wo=0
wx=0
gp=0
def start():
    print("~~~~~WELCOME TO THE TIC TAC TOE GAME~~~~~")
    print()
    def board(b):
        print("  "*15,"-" * 20) 
        for i in b:
            print("  "*15,"| "," | ".join(i),"| ")
            print("  "*15,"-" * 20)
    b=[["   ","   ","   "],["   ","   ","   "],["   ","   ","   "]]
    board(b)
    cp='X'
    con=True
    count=0
    box=9
    return b , cp , con , count , box ,board
def ttt():
    global gp
    global wo
    global wx
    global gp
    global con
    global cp
    global count
    global box
    gp+=1
    while con==True :
        box-=1
        if cp=='X':
            m=input( "Player X enter your move (row and column: 11 to 33) : ")
        else:
            m=input( "Player O enter your move (row and column: 11 to 33) : ")   
        l=[m[0],m[1]]
        r=int(l[0])
        c=int(l[1])
        if  1>r or r>3 or c>3 or 1>c:
            print("Invalid input. Please enter numbers between 1 and 3.")
            box+=1
            continue 
        if b[r-1][c-1]!="   ":
            print("This spot is already taken. Try again.")
            box+=1
            continue
        b[r-1][c-1]=cp.upper()
        board(b)
        for i in range(3):
            if b[i][0]==b[i][1]==b[i][2]==cp:
                print("player {} wins!".format(cp))
                if cp=='X':
                    wx+=1
                else:
                    wo+=1
                con=False
            if b[0][i]==b[1][i]==b[2][i]==cp:
                print("player {} wins!".format(cp))
                if cp=='X':
                    wx+=1
                else:
                    wo+=1
                con=False
        if b[0][0]==b[1][1]==b[2][2]==cp:
            print("player {} wins!".format(cp))
            if cp=='X':
                    wx+=1
            else:
                    wo+=1
            con=False
        if b[0][2]==b[1][1]==b[2][0]==cp:
            print("player {} wins!".format(cp))
            if cp=='X':
                    wx+=1
            else:
                    wo+=1
            con=False
        if box==0:
            for i in range(3):
                for j in range(3):
                    if b[i][j]!="   ":
                        count+=1
            if count==9:
                print("it's a draw ")
                con=False
        if cp=='X':
            cp='O'
        else:
            cp='X'
(b , cp , con , count , box , board )=start()
ttt()
while True :
    ch=input("do you want to play again?  (y/n)")
    if ch=="y":
        (b , cp , con , count , box , board )=start()
        ttt()
    else :
        print()
        print("~~~~~~~~~~Scoreboard~~~~~~~~~~")
        print("Total times game played : ",gp)
        print(" X win  : " ,wx)
        print(" O win  : " ,wo)
        break 