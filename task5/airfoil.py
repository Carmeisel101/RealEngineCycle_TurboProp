import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

z_dir = '../task3/z.csv'
camber = pd.read_csv(z_dir)
camber = camber['z'].to_numpy()

def dyc_over_dx( x, m, p, c ):
    return np.where((x>=0)&(x<=(c*p)),
                    ((2.0 * m) / np.power(p,2)) * (p - x / c),
                    ((2.0 * m ) / np.power(1-p,2)) * (p - x / c ))

def thickness( x, t, c ):
    term1 =  0.2969 * (np.sqrt(x/c))
    term2 = -0.1260 * (x/c)
    term3 = -0.3516 * np.power(x/c,2)
    term4 =  0.2843 * np.power(x/c,3)
    term5 = -0.1015 * np.power(x/c,4)
    return 5 * t * c * (term1 + term2 + term3 + term4 + term5)

def naca4(x, m, p, t, c=1):
    dyc_dx = dyc_over_dx(x, m, p, c)
    th = np.arctan(dyc_dx)
    yt = thickness(x, t, c)
    yc = camber
    x1 = x - yt*np.sin(th)
    y1 = yc + yt*np.cos(th)
    x2 = x + yt*np.sin(th)
    y2 = yc - yt*np.cos(th)

    return (x1, y1), (x2, y2)



#naca4425
m = 0.04
p = 0.4
t = 0.25
c = 1.0

x = np.linspace(0,1,100)
list_x= []
list_y = []
n = 0
for item in naca4(x, m, p, t, c):
    if n ==0:
        reverted_x = item[0][::-1]
        reverted_y = item[1][::-1]
        for i in range(len(reverted_x)):
            list_x.append(reverted_x[i])
            list_y.append(reverted_y[i])
            n += 1



    else:
        for i in range(len(reverted_x)):
            list_x.append(item[0][i])
            list_y.append(item[1][i])


# for item in naca4(x, m, p, t, c):
#     plt.plot(item[0], item[1], 'b')

values = pd.DataFrame({'x': list_x, 'y': list_y})
values.to_csv('airfoil2.csv', index=False)
print(values)


#
# plt.plot(x, camber, '.')
# plt.axis('equal')
# plt.xlim((-0.05, 1.05))
# # figure.set_size_inches(16,16,forward=True)
# plt.show()