import math
import matplotlib.pyplot as mtp


def funct(x, y):
    return y/(1+x) - 0.5*y**2


def third(x,y, h):
    fi0 = h*funct(x,y)
    fi1 = h*funct(x+0.1/2, y+fi0/2)
    fi2 = h*funct(x+0.1, y-fi0+2*fi1)
    return y + 1/6*(fi0 + 4*fi1+ fi2)


def forth(x, y, h):
    fi0 = h * funct(x, y)
    fi1 = h * funct(x + 0.05, y + fi0 / 2)
    fi2 = h * funct(x + 0.05, y + fi1/2)
    fi3 = h * funct(x+0.1, y + fi2)
    return y + 1/6*(fi0 +2*fi1 + 2*fi2 + fi3)


x =[0 ,]
y3 = [1 ,]
y4 = [1,]


def thirdfordraw(range, countsteps):
    h = round(range/countsteps,0)
    for i in range(countsteps):
        y3.append(third(x[i], y3[i], h))
        x.append(x[i]+h)

#y4.append(forth(x[i], y4[i]))
#print("Метод Рунге-Кутта 3 порядка {0}".format(round(y3[i+1],5)))
#print("Метод Рунге-Кутта 4 порядка {0}".format(round(y4[i+1],5)))

