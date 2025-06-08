f = lambda x: x**3 + 6*x**2 - 19*x - 84
df = lambda x: 3*x**2 + 12*x - 19

xs = 3  # nilai sebenarnya
x0 = 1  # tembakan Initial 

def newton_raphson(x):
    return x - f(x)/df(x)

def error_true(xs, x_current):
    return abs((xs - x_current) / xs) * 100

def error_approximate(x_current, x_prev):
    return abs((x_current - x_prev) / x_current) * 100

for i in range(1, 4):
    x1 = newton_raphson(x0)
    Et = error_true(xs, x1)
    Ea = error_approximate(x1, x0) if i > 1 else None
    
    print(f"iteration {i:02d} :")
    print(f"x_i: {x1:.2f}")
    print(f"ET (Error True): {Et:.2f}%")
    if Ea is not None:
        print(f"EA (Error Approx): {Ea:.2f}%")
    else:
        print(f"EA (Error Approx): -")  #iterasi pertama tidak memiliki eror aproximate 
    print()
    
    x0 = x1
