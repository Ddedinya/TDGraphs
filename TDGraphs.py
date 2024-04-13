import re
import numpy as np
from sympy import symbols, lambdify
import plotly.graph_objects as go

# Определяем x и y
x, y = symbols('x y')
# Просим пользователя ввести формулу
print(f'''Пожалуйста, введите формулу по следующему шаблону: ax+by. 
Используйте sqrt(ax) для извлечения корня, 
log(ax) для визуализации логарифмической функции, 
sin(ax), cos(ax), tan(ax), asin(ax), acos(ax), и atan(ax) для визуализации тригонометрических функций.''')
formula = input()
# Преобразовываем формулу, чтобы она соответствовала синтаксису языка, если то требуется
formula = re.sub(r'(\d+)x', r'\1*x', formula)
formula = re.sub(r'(\d+)y', r'\1*y', formula)
formula = formula.replace('^', '**')
# Обрабатываем формулу
f = lambdify((x, y), formula, {"numpy": np, "asin": np.arcsin, "acos": np.arccos, 
                               "atan": np.arctan, "sin": np.sin, "cos": np.cos, 
                               "tan": np.tan, "sqrt": np.sqrt, "log": np.log})
# Генерируем значения x и у
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
x, y = np.meshgrid(x, y)
# Вычисляем значение z
z = f(x, y)
# Создаём 3D-график
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
# Устанавливаем названия осей
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'))
# Показываем график
fig.show()