#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

'''
最小二乘法回归
参考博客：http://blog.csdn.net/wangyangzhizhou/article/details/60133958
line 代数推导
matrixLine 矩阵推导
'''

def calcAB(x,y):
    n = len(x)
    sumX,sumY,sumXY,sumXX =0,0,0,0
    for i in range(0,n):
        sumX  += x[i]
        sumY  += y[i]
        sumXX += x[i]*x[i]
        sumXY += x[i]*y[i]
    a = (n*sumXY -sumX*sumY)/(n*sumXX -sumX*sumX)
    b = (sumXX*sumY - sumX*sumXY)/(n*sumXX-sumX*sumX)
    return a,b,

def line():
	xi = [1,2,3,4,5,6,7,8,9,10]
	yi = [10,11.5,12,13,14.5,15.5,16.8,17.3,18,18.7]
	a, b = calcAB(xi,yi)
	print("y = %10.5fx + %10.5f" %(a,b))
	x = np.linspace(0,10)
	y = a * x + b
	plt.plot(x,y)
	plt.scatter(xi,yi)
	plt.show()


def matrixLine():
	x = [1,2,3,4,5,6,7,8,9,10]
	y = [10,11.5,12,13,14.5,15.5,16.8,17.3,18,18.7]

	A = np.vstack([x,np.ones(len(x))]).T

	a, b = np.linalg.lstsq(A,y)[0]
	print("y = %10.5fx + %10.5f" %(a,b))
	x = np.array(x)
	y = np.array(y)

	plt.plot(x,y,'o',label='data',markersize=10)
	plt.plot(x,a*x+b,'r',label='line')
	plt.show()

if __name__ == '__main__':
	# line()
	matrixLine()
