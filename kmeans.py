# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

__author__ = "xiaojie"

"""
聚类算法
"""

if __name__ == "__main__":
    
    n = 300
    c = 3
    cols = 2
    t = np.arange(n)
    np.random.shuffle(t)
    x = np.zeros((n, cols), dtype="float64")
    x[:n / 3, 0] = np.random.randn(1, n / 3) - 2
    x[n / 3:2 * n / 3, 0] = np.random.randn(1, n / 3)
    x[2 * n / 3: n, 0] = np.random.randn(1, n / 3) + 2

    x[:n / 3, 1] = np.random.randn(1, n / 3)
    x[n / 3:2 * n / 3, 1] = np.random.randn(1, n / 3) + 4
    x[2 * n / 3: n, 1] = np.random.randn(1, n / 3)
    m = x[t[0:c]]
    x2 = np.sum(np.square(x), axis=1)

    s0 = np.zeros((3, 1), dtype="float64")
    d = np.zeros((n, 1), dtype="float64")
    y = np.zeros((n, 1), dtype="float64")
    for i in range(n):
        d[i] = np.inf
        y[i] = np.inf

    for it in range(1000):
        m2 = np.sum(np.square(m), axis=1)
        f1 = np.zeros((c, n), dtype="float64")
        for i in range(c):
            f1[i] = m2[i]

        f2 = np.zeros((3, 300), dtype="float64")
        for i in range(c):
            f2[i] = x2

        f3 = 2 * np.dot(m, x.T)
        f = f1 + f2 - f3
        for i in range(n):
            f4 = f[:,i]
            index = -1
            minNum = np.inf
            for j in range(c):
                if f4[j] < minNum:
                    minNum = f4[j]
                    index = j
            if minNum < d[i]:
                d[i] = minNum
                y[i] = index

        s = np.zeros((3, 1), dtype="float64")
        for i in range(c):        
            m[i] = np.mean(x[np.where(y == i)[0]], axis=0)
            s[i] = np.mean(d[np.where(y == i)[0]], axis=0)
        if np.linalg.norm(s - s0, 2) < 0.001:
            print 'loop %s times, break' %it
            break
        s0 = s.copy()

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr'] 
    for i in xrange(n):  
        markIndex = int(y[i, 0]) 
        plt.plot(x[i, 0], x[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(c): 
        plt.plot(m[i, 0], m[i, 1], mark[i], markersize = 12)
    plt.show() 