import math
import matplotlib.pyplot as mtp


def function(x):
   return math.sin(2*x)/(x**5 + x + 1)


def trap():
    result = (function(0) + function(1))/2
    x = 0.03
    while( x < 1):
        result+= function(x)
        x+=0.03
    result*=0.03
    return result


def gomer():
    result = function(0) + function(1)
    temp = 0
    x=0.05
    while(x < 1):
        temp+=4*function(x)
        x+=0.1
    result+=temp
    temp = 0
    x=0.1
    while(x < 1):
        temp+= 2*function(x)
        x+=0.1
    result+=temp
    result*=1/60
    return result


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


def forecast(x,y):
    return y + 0.01* funct(x,y)


def correct(x,y):
    return y + 0.1*funct(x,y)+ 0.5*(funct(x+0.01, forecast(x,y))-funct(x,y))


print("Метод трапеции {0}".format(round(trap(),5)))
print("Метод Симпсона {0}".format(round(gomer(),5)))

x =[0 ,]
y3 = [1 ,]
y4 = [1,]
yf = [1,]
yw = [1,]


for i in range(3):
    print("Значение Y{0}".format(i+1))
    y3.append(third(x[i], y3[i]))
    y4.append(forth(x[i], y4[i]))
    yf.append(forecast(x[i],yf[i]))
    yw.append(correct(x[i], yw[i]))
    print("Метод прогноза-коррекции {0}".format(round(yw[i+1],5)))
    print("Метод Рунге-Кутта 3 порядка {0}".format(round(y3[i+1],5)))
    print("Метод Рунге-Кутта 4 порядка {0}".format(round(y4[i+1],5)))
    #print("Прогноз {0}".format(round(forecast(x[i],yf[i]),5)))
    #print("Коррекция {0}".format(round(yw[i+1],5)))
    x.append(x[i]+0.1)


leg1, leg2, leg3 = mtp.plot(x,y3, x, y4, x, yw)
mtp.legend((leg1, leg2, leg3), ("Рунге-Кутта 3 порядка", "Рунге-Кутта 4 порядка", "Метод прогноза-коррекции"))
mtp.grid()
mtp.show()
