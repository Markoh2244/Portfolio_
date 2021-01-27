

# Citations: #hw6, recurssion F18, backtracking S20
# import pygame
import random
from cmu_112_graphics import *
###################



# def isComplete(app,board):
#     store=[]
#     cols=len(board)
#     rows=len(board[0])
#     for t in (range(cols)):
#         for y in range(rows):
#             if board[t][y]=='red':
#                 store.append((t,y))
#     for i in app.locations:
#         if i not in store:
#             return False
# def isValid(board,row,col,move):
#     x,y=move
#     if ((row+x<0) or (len(board[row])>=col+y) or (len(board)>=row+x) or (0> col+y)):
#         return False
#     if board[row+x][col+y]=="bomb" :
#         return False
#     return True
# def isInBounds(board, row, col):
#     return (0 >= row and row < len(board) and col >= 0 and col < len(board[row]))

# def getNeighbors(board,row,col):
#     neighbors=set()
#     for i in range(-1,2,1):
#         for j in range(-1,2,1):
#             newrow= row+i
#             newcol= col+j
#             if newrow==row and newcol==col:
#                 continue
#             if isInBounds(board, newrow, newcol):
#                 neigbors.add(newrow,newcol)
#     return neighbors
# def getEquations(board,row,col):
#     equations=[]
#     for i in range(-1,2,1):
#         for j in range(-1,2,1):
#             newrow= row+i
#             newcol= col+j
#             if isInBounds(board, newrow, newcol):
#                 if board[newrow][newcol][0]=="black":
#                     equations.append(({(newrow,newcol)}, 1))
#                 else:
#                     equations.append(({(newrow,newcol)}, 0))
#                     equations.append((getNeighbors(board,newrow,newcol), 1))
#     return equations




# def makeMove(board, row,col, move):
#     x,y=move
#     newrow= row+x
#     newcol= col+y
#     equations= getEquations(board,newrow,newcol)
#     value=solveEquations(newrow,newcol,equations)
#     if value==None:
#         return None
#     board[newrow][newcol]=value
#     return board

# def solveEquations(row, col, equations):
#     assignments=dict()
#     multivar=[]

#     for (i,v) in equations:
#         if len(i)==1:
#             assignments[i]=v
#         else:
#             multivar.append((i,v))
#     for (i,v) in multivar:
#         anotherUnknown = False
#         if (row,col) in i:
#             for index in i:
#                 if index==(row,col):
#                     continue
#                 if assignments.get(index)==None:
#                     anotherUnknown = True
#                     break
#                 else:
#                     v-=assignments.get(index)
#             if not anotherUnknown:
#                 return v
        
#     return None




# def solveBoard(app,row,col,board):
#     if isComplete(app,board):
#         return board
#     for move in [(-1,0),(0,1),(1,0),(0,-1)]:
#         x,y=move
#         if isValid(board,row,col,move):
#             board = makeMove(board, row,col, move)
#             if board==None:
#                 return None
#             tmpSolution = solveBoard(row+x,col+y,board)
#             if tmpSolution != None:
#                 return tmpSolution
#     return None
    
def bombLocations():
    locations=[]
    x=0
    i=0
    while i<5 and x<1:
        a=random.randint(0,5)
        b=random.randint(0,5)
        if ((a,b)) not in locations:
            locations.append((a,b))
            i+=1
    x+=1
    return locations
    
def Dimensions():
    locations=bombLocations()
    rows=6
    cols=6
    cellSize=20
    margin=50
    return rows,cols,cellSize,margin,locations

def check(app,x,y):
    if x<0 or x>app.cols-1:
        return False
    if y<0 or y>app.rows-1:
        return False
    return True

def appStarted(app):
    app.welcome=True
    app.timer=0
    app.time=0
    app.score=5
    app.visited=[]
    app.count=0
    app.win=False
    app.found=[]
    app.color='gray'
    app.pressed=True
    app.x,app.y=0,0
    app.fill=''
    app.fill2=''
    app.lost=False
    app.rows,app.cols,app.cellSize,app.margin,app.locations = Dimensions()
    app.board=[]
    app.bboard=[]
    app.bottom1= app.margin+(app.cellSize*(app.rows+1))
    app.bottom2=app.margin+(app.cellSize*(app.rows+2))
    count=0
    for i in range(app.cols):
        app.bboard.append([])
        for x in range(app.rows):
            app.bboard[i].append(['white'])
    for i in app.locations:
        x,e=i
        app.bboard[x][e]=["black"]
    for i in range(app.cols):
        app.board.append([])
        for x in range(app.rows):
            app.board[i].append('gray')
    for t in (range(app.cols)):
        for y in range(app.rows):
            count=0
            if (t,y) not in (app.locations):
                if check(app,t-1,y) and app.bboard[t-1][y][0] =="black":
                    count+=1
                if check(app,t+1,y) and app.bboard[t+1][y][0] =="black":
                    count+=1
                if check(app,t-1,y+1) and app.bboard[t-1][y+1][0] =="black":
                    count+=1
                if check(app,t,y+1) and app.bboard[t][y+1][0] =="black":
                    count+=1
                if check(app,t+1,y+1) and app.bboard[t+1][y+1][0] =="black":
                    count+=1
                if check(app,t-1,y-1) and app.bboard[t-1][y-1][0] =="black":
                    count+=1
                if check(app,t,y-1) and app.bboard[t][y-1][0] =="black":
                    count+=1
                if check(app,t+1,y-1) and app.bboard[t+1][y-1][0] =="black": 
                    count+=1
            app.bboard[t][y].append(str(count))
def generateBoard(app):
    board=app.bboard
    while solveBoard(app,0,0,board)==None:
        app.locations=bombLocations()            
def getCell(app,x,y):
    row=(x-300)//app.cellSize
    col=(y-160)//app.cellSize
    return col,row

def checkAround(app,a,b):
    i,x=a,b 
    #switch to for i in directions for campactness later
    #fix letter scheme
    if (a,b) in app.visited:
        return False
    app.visited.append((a,b))
    if i+1<app.cols and app.bboard[a+1][b][1]=='0' and (i+1,b) not in app.visited  and  app.bboard[i+1][x][0]!='black':
        app.board[i+1][x]=''
        checkAround(app,i+1,x)
    if i-1>=0 and app.bboard[i-1][x][1]=='0' and (a-1,b) not in app.visited and app.bboard[i-1][x][0]!='black':
        app.board[i-1][x]=''
        checkAround(app,i-1,x)
    if i+1<app.cols and x+1<app.rows and app.bboard[a+1][b+1][0]=='0' and (i+1,b+1) not in app.visited and app.bboard[a+1][b+1][0]!='black' :
        app.board[i+1][x+1]=''
        checkAround(app,i+1,x+1)
    if x+1<app.rows and app.bboard[a][b+1][1]=='0' and (i,x+1) not in app.visited and app.bboard[a][b+1][0]!='black' :
        app.board[i][x+1]=''
        checkAround(app,i,x+1)
    if i-1>=0 and x+1<app.rows and app.bboard[a-1][b+1][1]=='0' and (i-1,b+1) not in app.visited and app.bboard[a-1][b+1][0]!='black':
        app.board[i-1][x+1]=''
        checkAround(app,i-1,x+1)
    if i-1>=0 and x-1>=0 and app.bboard[a-1][b-1][1]=='0' and (i-1,b-1) not in app.visited and app.bboard[a-1][b-1][0]!='black':
        app.board[i-1][x-1]=''
        checkAround(app,i-1,x-1)
    if i+1<app.cols and x-1>=0 and app.bboard[a+1][b-1][1]=='0' and (i+1,b-1) not in app.visited and app.bboard[a+1][b-1][0]!='black':
        app.board[i+1][x-1]=''
        checkAround(app,i+1,x-1)
    if x-1>=0 and app.bboard[a][b-1][1]=='0' and (i,b-1) not in app.visited and app.bboard[a][b-1][0]!='black' :
        app.board[i][x-1]=''
        checkAround(app,a,b-1)
    for j,k in app.visited:
        if app.bboard[j][k][1]=='0':
            for e,r in [(0,1),(0,-1),(1,0),(-1,0)]:
                if check(app,j+e,k+r) and app.bboard[j+e][k+r][0]!="black":
                    app.board[j+e][k+r]=''
    return False

def mousePressed(app,event):
    app.count=0
    app.x=event.x+300
    app.y=event.y+160
    a,b=getCell(app,event.x,event.y)

    if event.x<app.margin+app.cellSize and event.x>app.margin and event.y>400 and event.y<400 +app.cellSize:
        app.color='red'
    if event.x<(app.margin+2*app.cellSize) and event.x>app.margin +app.cellSize and event.y>400 and event.y<400+ app.cellSize:
        app.color='gray'
    
    if (event.x<420 and event.x>300 and event.y<280 and event.y>160) :
        if app.board[a][b]=='red':
            app.score+=1
            app.found.remove((a,b))
            app.board[a][b]='gray'
        elif app.pressed==True and app.bboard[a][b][1]=='0' and app.bboard[a][b][0]!='black':
            checkAround(app,a,b)
            app.board[a][b]=''
        elif app.pressed==True:
            return False
        elif app.bboard[a][b][0]!="black" and app.color=='gray':
            checkAround(app,a,b)
            app.board[a][b]=''
        elif app.color=='red' and app.board[a][b]!='' :
            app.board[a][b]='red'
            app.score-=1
            app.found.append((a,b))
        elif app.bboard[a][b][0]=="black" and app.pressed==False and app.color=='gray': 
            for a,b in app.locations:
                app.board[a][b]=''
            app.fill='red'
        if app.board[a][b]=='red' and app.bboard[a][b][0]!="black":
            app.found.append((a,b))
    for x in range(app.cols):
        for i in range(app.rows):
            if app.board[x][i]=='':
                app.pressed=False
    for i in app.found:
        if i in app.locations:
            app.count+=1

    if len(app.locations)== app.count:
        app.fill2='black'
        app.time=0
def timerFired(app):
    
    app.timer+=1
    if app.timer%6==0 and app.time<999 and app.fill!='red':
        app.time+=1

   


def createBoard(app,canvas):

    for x in range(app.cols):
        for i in range(app.rows):
            canvas.create_rectangle((i*app.cellSize)+300,(x*app.cellSize)+160,(i*app.cellSize)+app.cellSize+300,(x*app.cellSize)+app.cellSize+160,fill=app.bboard[x][i][0])
            if (x,i) not in (app.locations) and app.bboard[x][i][1] != '0':
                canvas.create_text((i*app.cellSize)+300 + (app.cellSize//2), (x*app.cellSize)+160 + (app.cellSize//2), text=app.bboard[x][i][1],fill="black", font="Helvetica 12 bold")
    for x in range(app.cols):
        for i in range(app.rows):
            canvas.create_rectangle((i*app.cellSize)+300,(x*app.cellSize)+160,(i*app.cellSize)+app.cellSize+300,(x*app.cellSize)+app.cellSize+160,fill=app.board[x][i])
    canvas.create_text(app.width//2.3+app.margin, app.height//3, text="YOU LOST",fill=app.fill, font="Helvetica 120 bold")
    canvas.create_text(app.width//2.3+app.margin, app.height//3, text="YOU WIN",fill=app.fill2, font="Helvetica 120 bold")

                                                                                              
    
    canvas.create_rectangle(590,10,650,40,fill='white')##########################################
    canvas.create_text(621, 25, text=str(app.score),fill='gray', font="Helvetica 30 bold")#######################

    canvas.create_rectangle(app.margin,10,app.margin+60,40,fill='white')##########################################
    canvas.create_text(80,25, text=str(app.time),fill='gray', font="Helvetica 30 bold")#######################


    canvas.create_rectangle(app.margin,400,app.margin+app.cellSize,400+app.cellSize,fill='red')
    
    canvas.create_rectangle(app.margin+app.cellSize,400,app.margin+2*app.cellSize,400+app.cellSize,fill='gray')

def redrawAll(app,canvas):
    createBoard(app,canvas)
runApp(width=700,height=450)


