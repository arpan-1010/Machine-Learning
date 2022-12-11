#multiple linear regression
###########################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#take values for x1, x2 & y
x1 = [52.80, 57.60, 68.64, 72.00, 72.96, 77.76, 86.40, 87.36, 86.40, 84.00, 93.60, 94.08, 87.84, 91.20, 72.00]
x2 = [37.50, 37.50, 41.25, 45.00, 56.25, 67.50, 67.50, 71.25, 67.50, 71.25, 93.75, 101.25, 108.75, 93.75, 90.00]
y = [12.00, 13.00, 14.25, 18.75, 22.50, 27.00, 28.50, 32.25, 33.00, 36.75, 37.50, 39.00, 40.50, 30.75, 26.25]
print("Income(x1)-million per capital list is: ", x1)
print("\nPopulation(x2)-million per people list is: ", x2)
print("\nRice consumption(y) -million tons list is: ",y)
ch = int(input("\nDo you want to insert any extra value for Weight(x)?\nIf yes press 1 otherwise press 0:"))

bo, b1, b2 = 0, 0, 0
Y_PRED = []
b1x1_b2x2 = []
X1i_lst = []
X2i_lst = []

n = 0
for i in x1:
    n += 1
#print(n)

def b0_b1_b2():
    b1 = ((Sum_yix1i * Sum_x2i_sqr) - (Sum_yix2i * Sum_x1ix2i)) / ((Sum_x1i_sqr * Sum_x2i_sqr) - (Sum_x1ix2i ** 2))
    print("\nThe value of the second regression coefficient(b1) is = ", b1)
    b2 = ((Sum_yix2i * Sum_x1i_sqr) - (Sum_yix1i * Sum_x1ix2i)) / ((Sum_x1i_sqr * Sum_x2i_sqr) - (Sum_x1ix2i ** 2))
    print("The value of the third regression coefficient(b2) is = ", b2)
    b0 = ((Sum_y / n) - b1*(Sum_x1 / n) - b2*(Sum_x2 / n))
    print("The value of the first regression coefficient(b0) is = {}\n".format(b0))
    print("------------------------------------------------------------------------------------")
    #calculate the values for y_pred by putting the values of b0, b1 & b2
    for i in X1i:
        X1i_lst.append(b1 * i)
    #print(X1_lst)
    for i in X2i:
        X2i_lst.append(b2 * i)
    #print(X2_lst)
    ar = np.array(X1i_lst)
    ar1 = np.array(X2i_lst)
    for i in (ar + ar1):
        b1x1_b2x2.append(i)
    B1X1_B2X2 = np.array(b1x1_b2x2)
    for i in (b0 + B1X1_B2X2):
        Y_PRED.append(i)
    #print(Y_PRED)

if ch==0:
    Sum_y = 0
    for i in y:
        Sum_y = Sum_y +i
    #print(Sum_y)
    Yi = []
    for i in y:
        Yi.append(i - (Sum_y / n))
    #print(Yi)
    Sum_x1 = 0
    for i in x1:
        Sum_x1 = Sum_x1 + i
    #print(Sum_x1)
    Sum_x2 = 0
    for i in x2:
        Sum_x2 = Sum_x2 + i
    #print(Sum_x2)
    X1i = []
    for i in x1:
        X1i.append(i - (Sum_x1 / n))
    #print(X1i)
    X2i = []
    for i in x2:
        X2i.append(i - (Sum_x2 / n))
    #print(X2i)
    Y_i_sqr = []
    for i in y:
        Y_i_sqr.append(i * i)
    #print(Y_i_sqr)
    X1i_sqr = []
    for i in X1i:
        X1i_sqr.append(i * i)
    #print(X1i_sqr)
    X2i_sqr = []
    for i in X2i:
        X2i_sqr.append(i * i)
    #print(X2i_sqr)
    arr1 = np.array(Yi)
    arr2 = np.array(X1i)
    YiX1i = []
    for i in (arr1 * arr2):
        YiX1i.append(i)
    #print(YiX1i)
    arr3 = np.array(X2i)
    YiX2i = []
    for i in (arr1 * arr3):
        YiX2i.append(i)
    #print(YiX2i)
    X1iX2i = []
    for i in (arr2 * arr3):
        X1iX2i.append(i)
    #print(X1iX2i)
    Sum_yi = 0
    for i in Yi:
        Sum_yi = Sum_yi + i
    #print(Sum_yi)
    Sum_x1i = 0
    for i in X1i:
        Sum_x1i = Sum_x1i + i
    #print(Sum_x1i)
    Sum_x2i = 0
    for i in X2i:
        Sum_x2i = Sum_x2i + i
    #print(Sum_x2i)
    Sum_yi_sqr = 0
    for i in Y_i_sqr:
        Sum_yi_sqr += i
    #print(Sum_yi_sqr)
    Sum_x1i_sqr = 0
    for i in X1i_sqr:
        Sum_x1i_sqr += i
    #print(Sum_x1i_sqr)
    Sum_x2i_sqr = 0
    for i in X2i_sqr:
        Sum_x2i_sqr += i
    #print(Sum_x2i_sqr)
    Sum_yix1i = 0
    for i in YiX1i:
        Sum_yix1i += i
    #print(Sum_yix1i)
    Sum_yix2i = 0
    for i in YiX2i:
        Sum_yix2i += i
    #print(Sum_yix2i)
    Sum_x1ix2i = 0
    for i in X1iX2i:
        Sum_x1ix2i += i
    #print(Sum_x1ix2i)
        
    #calculate the values of b0, b1, b2
    b0_b1_b2()
    #displaying all the data in tabular format
    print("The table will be:\n")
    sr = pd.Series(x1)
    #print(sr)
    sr1 = pd.Series(x2)
    #print(sr1)
    sr2 = pd.Series(Y_PRED)
    d1 = {"Income": sr, "Population": sr1, "sPredicted value of rice consumption(y)": sr2}
    df1 = pd.concat(d1, axis=1)
    print(df1)
    """#plotting data in graph
    plt.title("The graph will be like:")
    #plt.xlabel("Predicted value of y")
    #plt.ylabel("Actual value of y")
    plt.scatter(y, Y_PRED)
    plt.plot(y, Y_PRED)
    plt.show()"""
else:
    Sum_y = 0
    for i in y:
        Sum_y = Sum_y +i
    #print(Sum_y)
    Yi = []
    for i in y:
        Yi.append(i - (Sum_y / n))
    #print(Yi)
    Sum_x1 = 0
    for i in x1:
        Sum_x1 = Sum_x1 + i
    #print(Sum_x1)
    Sum_x2 = 0
    for i in x2:
        Sum_x2 = Sum_x2 + i
    #print(Sum_x2)
    X1i = []
    for i in x1:
        X1i.append(i - (Sum_x1 / n))
    #print(X1i)
    X2i = []
    for i in x2:
        X2i.append(i - (Sum_x2 / n))
    #print(X2i)
    Y_i_sqr = []
    for i in y:
        Y_i_sqr.append(i * i)
    #print(Y_i_sqr)
    X1i_sqr = []
    for i in X1i:
        X1i_sqr.append(i * i)
    #print(X1i_sqr)
    X2i_sqr = []
    for i in X2i:
        X2i_sqr.append(i * i)
    #print(X2i_sqr)
    arr1 = np.array(Yi)
    arr2 = np.array(X1i)
    YiX1i = []
    for i in (arr1 * arr2):
        YiX1i.append(i)
    #print(YiX1i)
    arr3 = np.array(X2i)
    YiX2i = []
    for i in (arr1 * arr3):
        YiX2i.append(i)
    #print(YiX2i)
    X1iX2i = []
    for i in (arr2 * arr3):
        X1iX2i.append(i)
    #print(X1iX2i)
    Sum_yi = 0
    for i in Yi:
        Sum_yi = Sum_yi + i
    #print(Sum_yi)
    Sum_x1i = 0
    for i in X1i:
        Sum_x1i = Sum_x1i + i
    #print(Sum_x1i)
    Sum_x2i = 0
    for i in X2i:
        Sum_x2i = Sum_x2i + i
    #print(Sum_x2i)
    Sum_yi_sqr = 0
    for i in Y_i_sqr:
        Sum_yi_sqr += i
    #print(Sum_yi_sqr)
    Sum_x1i_sqr = 0
    for i in X1i_sqr:
        Sum_x1i_sqr += i
    #print(Sum_x1i_sqr)
    Sum_x2i_sqr = 0
    for i in X2i_sqr:
        Sum_x2i_sqr += i
    #print(Sum_x2i_sqr)
    Sum_yix1i = 0
    for i in YiX1i:
        Sum_yix1i += i
    #print(Sum_yix1i)
    Sum_yix2i = 0
    for i in YiX2i:
        Sum_yix2i += i
    #print(Sum_yix2i)
    Sum_x1ix2i = 0
    for i in X1iX2i:
        Sum_x1ix2i += i
    #print(Sum_x1ix2i)
    I = float(input("Enter the value of income(x1) : "))
    P = float(input("Enter the value of population(x2) : "))
    #calculate the values of b0, b1, b2
    b1 = ((Sum_yix1i * Sum_x2i_sqr) - (Sum_yix2i * Sum_x1ix2i)) / ((Sum_x1i_sqr * Sum_x2i_sqr) - (Sum_x1ix2i ** 2))
    print("\nThe value of the second regression coefficient(b1) is = ", b1)
    b2 = ((Sum_yix2i * Sum_x1i_sqr) - (Sum_yix1i * Sum_x1ix2i)) / ((Sum_x1i_sqr * Sum_x2i_sqr) - (Sum_x1ix2i ** 2))
    print("The value of the third regression coefficient(b2) is = ", b2)
    b0 = ((Sum_y / n) - b1*(Sum_x1 / n) - b2*(Sum_x2 / n))
    print("The value of the first regression coefficient(b0) is = {}\n".format(b0))
    print("The predicted value of rice consumption(y) for the inputted values {} and {} will be : {}".format(I, P, (b0 + (b1 * I) + (b2 * P))))
