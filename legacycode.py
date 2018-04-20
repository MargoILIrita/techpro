#derivative of function
def derivative(x, y):
    if x == -1 :
        raise ValueError("Function doesn't exist")
    return y/(1+x) - 0.5*y**2

#computing y for third
def third(x,y, h):
    fi0 = h*derivative(x,y)
    fi1 = h*derivative(x+h/2, y+fi0/2)
    fi2 = h*derivative(x+h, y-fi0+2*fi1)
    return y + 1/6*(fi0 + 4*fi1+ fi2)


#computing y for forth
def forth(x, y, h):
    fi0 = h * derivative(x, y)
    fi1 = h * derivative(x + h/2, y + fi0 / 2)
    fi2 = h * derivative(x + h/2, y + fi1/2)
    fi3 = h * derivative(x+h, y + fi2)
    return y + 1/6*(fi0 +2*fi1 + 2*fi2 + fi3)



#input:
#end - (float) end of range
#countsteps - (int) count of steps
#output [x,y]
#x - (list of float)
#y - (list of float)
def thirdfordraw(end, countsteps):
    x = [0, ]
    y3 = [1, ]
    h = round(end/countsteps,0)
    for i in range(countsteps):
        y3.append(third(x[i], y3[i], h))
        x.append(x[i]+h)
    return (x,y3)

#input:
#end - (float) end of range
#countsteps - (int) count of steps
#output [x,y]
#x - (list of float)
#y - (list of float)
def forthfordraw(end, countsteps):
    x = [0, ]
    y4 = [1, ]
    h = round(end / countsteps, 0)
    for i in range(countsteps):
        y4.append(forth(x[i], y4[i], h))
        x.append(x[i] + h)
    return (x, y4)


