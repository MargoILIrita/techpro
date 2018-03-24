import math
import matplotlib.pyplot as mtp

#функция для которой всё строится
def function(x):
   return math.sin(2*x)/(x**5 + x + 1)



def funct(x, y):
    return y/(1+x) - 0.5*y**2


def third(x,y):
    fi0 = 0.1*funct(x,y)
    fi1 = 0.1*funct(x+0.1/2, y+fi0/2)
    fi2 = 0.1*funct(x+0.1, y-fi0+2*fi1)
    return y + 1/6*(fi0 + 4*fi1+ fi2)


def forth(x,y):
    fi0 = 0.1 * funct(x, y)
    fi1 = 0.1 * funct(x + 0.05, y + fi0 / 2)
    fi2 = 0.1 * funct(x + 0.05, y + fi1/2)
    fi3 = 0.1*funct(x+0.1, y + fi2)
    return y + 1/6*(fi0 +2*fi1 + 2*fi2 + fi3)



x =[0 ,]
y3 = [1 ,]
y4 = [1,]


for i in range(3):
    print("Значение Y{0}".format(i+1))
    y3.append(third(x[i], y3[i]))
    y4.append(forth(x[i], y4[i]))
    print("Метод Рунге-Кутта 3 порядка {0}".format(round(y3[i+1],5)))
    print("Метод Рунге-Кутта 4 порядка {0}".format(round(y4[i+1],5)))
    x.append(x[i]+0.1)


leg1, leg2 = mtp.plot(x,y3, x, y4,)
mtp.legend((leg1, leg2), ("Рунге-Кутта 3 порядка", "Рунге-Кутта 4 порядка"))
mtp.grid()
mtp.show()
