import pandas as pd
from algorithms.algorithms import parameters

bisect = pd.read_csv('./tables/bisection.csv')
newton = pd.read_csv('./tables/newton.csv')
secant = pd.read_csv('./tables/secant.csv')

f, fp, a, b, root = parameters()

def rel_error(x, root):
    return abs(x - root) / abs(root)

bisect.insert(3, 'relerror', rel_error(bisect['x'], root))
newton.insert(3, 'relerror', rel_error(newton['x'], root))
secant.insert(3, 'relerror', rel_error(secant['x'], root))


for method in [bisect, newton, secant]:
    method['k'] = method['k'].astype(int)
    method['f'] = method['f'].map('{:.2e}'.format)
    method['relerror'] = method['relerror'].map('{:.2e}'.format)


bisect.to_csv('./tables/bisectionrel.csv', index=False)
newton.to_csv('./tables/newtonrel.csv', index=False)
secant.to_csv('./tables/secantrel.csv', index=False)
