from algorithms.algorithms import parameters
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f_fp():
    f, fp, a, b, root = parameters()

    margin = 0.5 * (b - a)

    # Plot f and fprime on a, b
    x1 = np.linspace(a - margin, a, 1000)
    x2 = np.linspace(a, b, 1000)
    x3 = np.linspace(b, b + margin, 1000)

    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)

    yp1 = fp(x1)
    yp2 = fp(x2)
    yp3 = fp(x3)

    plt.plot(x1, y1, color='blue', ls='dotted')
    plt.plot(x2, y2, color='blue', label='f')
    plt.plot(x3, y3, color='blue', ls='dotted')

    plt.plot(x1, yp1, color='red', ls='dotted')
    plt.plot(x2, yp2, color='red', label="f'")
    plt.plot(x3, yp3, color='red', ls='dotted')  

    plt.title('f and fprime on [a,b]')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.savefig('./plots/ffp.png')
    plt.savefig('./plots/svg/ffp.svg')
    plt.close()

def f_full():
    f, fp, a, b, root = parameters()
    
    x = np.linspace(-5, 10, 1000)
    y = f(x)
    
    plt.grid()
    plt.scatter(root, f(root), color='red', label='root')
    plt.plot(x, y, color='blue', label='f')
    plt.plot(x, x*0, color='black', ls='dotted')
    plt.legend()
    plt.savefig('./plots/ffull.png')
    plt.savefig('./plots/svg/ffull.svg')
    plt.close()

def rel_error(df, name):
    plt.axhline(y=(np.finfo(float).eps), color='r',
                linestyle=':', label="Machine Epsilon: 2.220446049250313e-16")
    plt.scatter(df['k'], df['relerror'], color='blue', label='rel_error')
    plt.plot(df['k'], df['relerror'], color='blue')
    plt.yscale('symlog', linthresh=np.finfo(float).eps)
    plt.xlabel('k: Number of iterations')
    plt.ylabel('Relative Error')
    plt.title(f'Relative Errors, {name} method')
    plt.savefig(f'./plots/{name}rel.png')
    plt.close()

f_fp()
f_full()

bisect = pd.read_csv('./tables/bisectionrel.csv')
newton = pd.read_csv('./tables/newtonrel.csv')
secant = pd.read_csv('./tables/secantrel.csv')

rel_error(bisect, "bisection") 
rel_error(newton, "newton")
rel_error(secant, "secant")