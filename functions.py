import math
import matplotlib.pyplot as plt


def func_(x, y, b):
    return x*b - b*y


def exactive(b, a, h, t_max):
    result = []
    for x in range(1, t_max+1, h):
        result.append(a*(1 - math.exp(-b * x)))
    return result


def rungecutt(b, h, a, t_max):
    y = 0
    res = []
    for x in range(a, t_max, h):
        k1 = h*func_(x, y, b)
        k2 = h*func_(x + h/2, y + k1/2, b)
        k3 = h*func_(x + h/2, y - k2/2, b)
        k4 = h*func_(x + h, y - k3, b)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
        res.append(y)
    return res


def euler(h, b, a, t_max):
    res_e = []
    y = 0
    for x in range(a, t_max, h):
        y = y + h*func_(x, y, b)
        res_e.append(y)
    return res_e


def graph_draw(k, j, s, a, t_max, h):
    fig = plt.figure()
    graph = fig.add_subplot()
    graph.set_title('GOKU')
    plt.grid()
    graph.set_xlabel('t')
    graph.set_ylabel('m(t)')
    i = 0
    for t in range(a, t_max, h):
        plt.scatter(t, k[i])
        plt.scatter(t, j[i])
        plt.scatter(t, s[i])
        i = i + 1
    plt.show()
    return graph





