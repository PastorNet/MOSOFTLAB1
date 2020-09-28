

from input import a, b, h, t_max
from functions import exactive, rungecutt, euler, graph_draw


result_exactive = exactive(b, a, h, t_max)
result_cutt = rungecutt(b, h, a, t_max)
result_euler = euler(h, b, a, t_max)
graph_draw(result_exactive, result_cutt, result_euler, a, t_max, h)


