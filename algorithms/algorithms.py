import numpy as np
import pandas as pd

import IPython

def bisection_method(f, a, b, M, delta, epsilon):
    print("Bisection method")
    
    columns = ["k", "x", "f"]
    df = pd.DataFrame(columns=columns)

    u = f(a)
    v = f(b)
    e = b - a

    
    for k in range(M):
        e = e/2
        c = a + e
        w = f(c)
        
        if abs(e) < delta or abs(w) < epsilon:
            df.loc[k] = [k, c, w]
            print("Halt")
            print(f"abs(e) < delta: {abs(e) < delta}")
            print(f"abs(w) < epsilon: {abs(w) < epsilon}")
            df.to_csv('./tables/bisection.csv', index=False)
            return c
        
        if np.sign(w) != np.sign(u):
            b = c
            v = w
        
        else:
            a = c
            u = w
        
        df.loc[k] = [k, c, w]
    
    df.to_csv('./tables/bisection.csv', index=False)
    return c

def newtons_method(f, fprime, x_init, M, delta, epsilon):
    print("Newton's method")
    x0 = x_init
    v = f(x0)

    columns = ["k", "x", "f"]
    df = pd.DataFrame(columns=columns)

    df.loc[0] = [0, x0, v]
    
    if abs(v) < epsilon:
        print("Halt")
        print(f"abs(v) < epsilon: {abs(v) < epsilon}")
        df.to_csv('newton.csv', index=False)
        return x0

    for k in range(1, M):
        x1 = x0 - v / fprime(x0)
        v = f(x1)

        df.loc[k] = [k, x1, v]
        if abs(x1 - x0) < delta or abs(v) < epsilon:
            print("Halt")
            print(f"abs(x1 - x0) < delta: {abs(x1 - x0) < delta}")
            print(f"abs(v) < epsilon: {abs(v) < epsilon}")
            df.to_csv('./tables/newton.csv', index=False)
            return x1
        x0 = x1
    
    df.to_csv('./tables/newton.csv', index=False)
    return x1


def diff_quot(f, a, b):
    return (f(b) - f(a)) / (b - a)
    

def secant(f, x0, x1, M, delta, epsilon):
    print("Secant method")
    f0 = f(x0)
    f1 = f(x1)

    columns = ["k", "x", "f"]
    df = pd.DataFrame(columns=columns)

    df.loc[0] = [0, x0, f0]
    df.loc[1] = [1, x1, f1]

    f_k = f1
    f_km1 = f0
    
    x_k = x1
    x_km1 = x0
    
    for k in range(2, M+1):
        if abs(f_k) > abs(f_km1):
            x_k, x_km1 = x_km1, x_k
            f_k, f_km1 = f_km1, f_k
            

        x_kp1 = x_k - f_k / diff_quot(f, x_k, x_km1)
        f_kp1 = f(x_kp1)
        

        df.loc[k] = [k, x_kp1, f_kp1]

        dx = x_k - x_km1
        dy = f_k - f_km1

        x_km1 = x_k
        x_k = x_kp1

        f_km1 = f_k
        f_k = f_kp1

        dx = x_k - x_km1

        if abs(dx) < delta or abs(f_k) < epsilon:
            print("Halt")
            print(f"abs(dx) < delta: {abs(dx) < delta}")
            print(f"abs(f_k) < epsilon: {abs(f_k) < epsilon}")
            df.to_csv('./tables/secant.csv', index=False)
            return x_k
        
    df.to_csv('./tables/secant.csv', index=False)
    return x_k


def parameters():
    
    def f(x):
        return np.exp(-x) * np.sin(np.exp(x))
    
    def fprime(x):
        return -1 * np.exp(-x) * np.sin(np.exp(x)) + np.exp(-x) * np.cos(np.exp(x)) * np.exp(x)
    
    root = np.log(np.pi)
    a, b = 0.5, 1.2
    return f, fprime, a, b, root

if __name__ == "__main__":
    print("Machine epsilon: ", np.finfo(float).eps)

    print("f(x) = exp(-x) * sin(exp(x))")

    f, fp, a, b, root = parameters()

    epsilon = delta = np.finfo(float).eps

    print(f"bisection: {bisection_method(f, a, b, 1000, epsilon, delta)}\n")
    print(f"newton: {newtons_method(f, fp, a, 1000, epsilon, delta)}\n")
    print(f"pretty secant: {secant(f, a, b, 1000, epsilon, delta)}\n")

    print("Actual root: 1.1447")
    