from sympy import symbols, simplify, lcm, latex

x1, y1, z1, z3, a, w = symbols("x1 y1 z1 z3 a w")

lam = (3 * (x1 / z1) * (x1 / z1) + a) / (2 * y1 / z1)
w_expr = 3 * x1 * x1 + a * z1 * z1
x3_expr = simplify((lam**2 - 2 * x1 / z1) * z3).subs(w_expr, w)
y3_expr = simplify((lam * (x1 / z1 - x3_expr / z3) - y1 / z1) * z3).subs(w_expr, w)

x3_denom = x3_expr.as_numer_denom()[1]
y3_denom = y3_expr.as_numer_denom()[1]

z3_expr = lcm(x3_denom, y3_denom)
print("\\begin{align}")
print("w &=", latex(w_expr), "\\\\")
print("x_3 &=", latex(x3_expr.subs(z3, z3_expr)), "\\\\")
print("y_3 &=", latex(y3_expr.subs(z3, z3_expr)), "\\\\")
print("z_3 &=", latex(z3_expr), "\\\\")
print("\\end{align}")
