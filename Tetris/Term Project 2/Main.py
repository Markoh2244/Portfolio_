import random
from cmu_112_graphics import *
def appStarted(app):
    app.test=True
def mousePressed(app,event):
    if event.x>75 and event.x<200 and event.y>200 and event.y<250 and app.test==True:
        app.test=False
        import Minesweeper0
        

    elif event.x>275 and event.x<400 and event.y>200 and event.y<250 and app.test==True:
        app.test=False
        import Minesweeper1

    elif event.x>475 and event.x<600 and event.y>200 and event.y<250 and app.test==True:
        app.test=False
        import Minesweeper2


    
def createBoard(app,canvas):
    canvas.create_text(350, 100, text='Please select a level from below:',fill='black', font="Helvetica 30 bold")


    canvas.create_rectangle(75,200,200,250,fill='gray')
    canvas.create_text(140, 225, text='Easy',fill='green', font="Helvetica 30 bold")

    canvas.create_rectangle(275,200,400,250,fill='gray')
    canvas.create_text(339, 225, text='Medium',fill='yellow', font="Helvetica 30 bold")

    canvas.create_rectangle(475,200,600,250,fill='gray')
    canvas.create_text(535, 225, text='Hard',fill='red', font="Helvetica 30 bold")


def redrawAll(app,canvas):
    createBoard(app,canvas)
runApp(width=700,height=450)