from sympy import symbols, simplify, lcm, latex

x1, y1, z1, x2, y2, z2, z3, u, v = symbols("x1 y1 z1 x2 y2 z2 z3 u v")

lam = (y2 / z2 - y1 / z1) / (x2 / z2 - x1 / z1)
v_expr = x2 * z1 - x1 * z2
u_expr = y2 * z1 - y1 * z2
x3_expr = simplify((lam**2 - x1 / z1 - x2 / z2) * z3).subs([(v_expr, v), (u_expr, u)])
y3_expr = simplify((lam * (x1 / z1 - x3_expr / z3) - y1 / z1) * z3).subs(
    [(v_expr, v), (u_expr, u)]
)

print("\\begin{align}")
print("u &=", latex(u_expr), "\\\\")
print("v &=", latex(v_expr), "\\\\")
print("x_3 &=", latex(x3_expr.normal()), "\\\\")
print("y_3 &=", latex(y3_expr.normal()), "\\\\")
print("\\end{align}")
x3_denom = x3_expr.as_numer_denom()[1]
y3_denom = y3_expr.as_numer_denom()[1]

z3_expr = lcm(x3_denom, y3_denom)
print()
print("\\begin{align}")
print("u &=", latex(u_expr), "\\\\")
print("v &=", latex(v_expr), "\\\\")
print("x_3 &=", latex(x3_expr.subs(z3, z3_expr)), "\\\\")
print("y_3 &=", latex(y3_expr.subs(z3, z3_expr)), "\\\\")
print("z_3 &=", latex(z3_expr), "\\\\")
print("\\end{align}")
