

from input import  a, b, h
from functions import exactive, rungecutt, euler, graph_draw


result_exactive = exactive(b, a)
result_cutt = rungecutt(b, h, b)
result_euler = euler(h, b)
graph_draw(result_exactive, result_cutt, result_euler)


