import math

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
