from graphics import *
 
def main():
 
    #Create a graphics window with labels on the left edge.
    win = GraphWin("Investment Growth Chart", 600, 460)
    win.setBackground("white")
    win.setCoords(-1.75,-9000,11.5,15400)
 
    #introduction
    Text(Point(4.0, 14000),"Future Value Calculator").draw(win)
 
    #principal input
    Text(Point(1.0, -4000), "Input Starting Principal").draw(win)
    inputP = Entry(Point(3,-4000),6)
    inputP.setText("0")
    inputP.draw(win)
 
    #intrest input
    Text(Point(6, -4000), "Input Interest Rate (0.05 eg)").draw(win)
    inputQ = Entry(Point(8.2,-4000),6)
    inputQ.setText("0")
    inputQ.draw(win)
 
    #create calc button
    button = Rectangle(Point(2,-6000),Point(8,-8000))
    button.setFill("red")
    button.draw(win)
    buttontxt = Text(Point(5,-7200),"Calculate:")
    buttontxt.draw(win)
    win.getMouse()
 
    #recieve input
    p = eval(inputP.getText())
    q = eval(inputQ.getText())
 
    #labels
    Text(Point(-1,0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
 
    # the first years
    bar = Rectangle(Point(0,0),Point(1,p))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
 
    for i in range(1,11): #count 1-10
        p = p*(1+q)
        bar= Rectangle(Point(i,0),Point(i+1,p))
        bar.setFill('Green')
        bar.setWidth(2)
        bar.draw(win)
 
    buttontxt.setText('Quit.')
 
    win.getMouse() # pause for click in window
    win.close()
 
main()
