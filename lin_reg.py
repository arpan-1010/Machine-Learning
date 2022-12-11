#normal linear regression
#########################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#take values for x & y,here Weight(pound) = x and Height(inch) = y
x = [140, 155, 159, 179, 192, 200, 212, 219, 145, 234]
y = [60, 62, 67, 70, 71, 72, 75, 80, 68, 70]
print("Your Weight(x) value list is:", x)
print("Your Height(y) value lost is:", y)
ch = int(input("Do you want to insert any extra value for Weight(x)?\nIf yes press 1 otherwise press 0:"))

bo, b1, B0, B1, B_NEW_0, B_NEW_1 = 0, 0, 0, 0, 0, 0
Y_PRED = []
Y_i_PRED = []
Y_i_PRED_NEW = []
n = 0
for i in x:
    n = n + 1
x_min = x[0]
x_max = x[1]
for i in x:
    if i < x_min:
        x_min = i
#print(x_min)
for i in x:
    if i > x_max:
        x_max = i
#print(x_max)

def b0_b1():
    b0, b1 = 0, 0
    b0 = ((SUM_Y * SUM_X_sqr) - (SUM_X * SUM_XY)) / ((n * SUM_X_sqr) - (SUM_X) ** 2)
    print("\nThe value of the first regression coefficient(b0) is =", b0)
    b1 = ((n * SUM_XY) - (SUM_X * SUM_Y)) / ((n * SUM_X_sqr) - (SUM_X) ** 2)
    print("The value of the second regression coefficient(b1) is = {}\n".format(b1))
    print("------------------------------------------------------------------------------------")
    for i in x:
        Y_PRED.append(b0 + (b1 * i))
    # print("Your predicted value list for given y is:", Y_PRED)

def b0_b1_minMax():
    B0, B1 = 0, 0
    B0 = ((SUM_Y * SUM_Xi_sqr) - (SUM_Xi * SUM_XiY)) / ((n * SUM_Xi_sqr) - (SUM_Xi) ** 2)
    print("\nThe current value of the first regression coefficient after min_max normalization b0 is =", B0)
    B1 = ((n * SUM_XiY) - (SUM_Xi * SUM_Y)) / ((n * SUM_Xi_sqr) - (SUM_Xi) ** 2)
    print("The current value of the second regression coefficient after min_max normalization b1 is = {}\n".format(B1))
    for i in X_i:
        Y_i_PRED.append(B0 + (B1 * i))
    #print("Your predicted value list for given y is:", Y_i_PRED)

def b0_b1_Standard():
    B_NEW_0, B_NEW_1 = 0, 0
    B_NEW_0 = ((SUM_Y * SUM_Xi_sqr_NEW) - (SUM_X_NEW * SUM_XiY_NEW)) / ((n * SUM_Xi_sqr_NEW) - (SUM_X_NEW) ** 2)
    print("\nThe current value of the first regression coefficient after standardization b0 is =", B_NEW_0)
    B_NEW_1 = ((n * SUM_XiY_NEW) - (SUM_X_NEW * SUM_Y)) / ((n * SUM_Xi_sqr_NEW) - (SUM_X_NEW) ** 2)
    print("The current value of the second regression coefficient after standardization b1 is = ", B_NEW_1)
    for i in NEW_X:
        Y_i_PRED_NEW.append(B_NEW_0 + (B_NEW_1 * i))
    #print("Your predicted value list for given y is:", Y_i_PRED_NEW)

if ch == 0:
    SUM_X = 0
    for i in x:
        SUM_X = SUM_X + i
    #print(n)
    #print(SUM_X)
    SUM_Y = 0
    for i in y:
        SUM_Y = SUM_Y + i
    # print(SUM_Y)
    SUM_X_sqr = 0
    for i in x:
        SUM_X_sqr = SUM_X_sqr + (i * i)
    #print(SUM_X_sqr)
    arr1 = np.array(x)
    arr2 = np.array(y)
    SUM_XY = 0
    for i in (arr1 * arr2):
        SUM_XY = SUM_XY + i
    #print(SUM_XY)
    #calculate the values of b0,b1 without normalization
    b0_b1()
    #displaying all the data in tabular format
    print("Before normalization the table will be like:\n")
    sr = pd.Series(x)
    #print(sr)
    sr1 = pd.Series(y)
    #print(sr1)
    sr2 = pd.Series(Y_PRED)
    #print(sr2)
    d1 = {"Weight": sr, "Height": sr1, "Predicted value of Height(y)": sr2}
    df1 = pd.concat(d1, axis=1)
    print(df1)
    print("------------------------------------------------------------------------------------")
    choice = int(input("Do you want to normalize the model?\nPress 1 for yes and 0 for no:"))
    print("------------------------------------------------------------------------------------")

    #normaliztion process....
    #min-max normalization
    X_i = []
    if choice == 1:
        for i in x:
            X_i.append((i - x_min) / (x_max - x_min))
        #print("Your current value of Weight(x) list is: ", X_i)
        SUM_Xi = 0
        for i in X_i:
            SUM_Xi = SUM_Xi + i
        #print(SUM_Xi)
        SUM_Xi_sqr = 0
        for i in X_i:
            SUM_Xi_sqr = SUM_Xi_sqr + (i * i)
        #print(SUM_Xi_sqr)
        arr3 = np.array(X_i)
        SUM_XiY = 0
        for i in (arr3 * arr2):
            SUM_XiY = SUM_XiY + i
        #print(SUM_XiY)
        #calculate the values of b0 & b1 with min_max normalization
        b0_b1_minMax()
        #check the efficiency
        n_minMax = 0
        for i in y:
            for j in Y_i_PRED:
                if (int(i) == int(j)):
                    n_minMax = n_minMax + 1
        #print(ni)
        sr = pd.Series(x)
        #print(sr)
        sr1 = pd.Series(y)
        #print(sr1)
        sr3 = pd.Series(Y_i_PRED)
        #print(sr3)
        d2 = {"Weight": sr, "Height": sr1, "Predicted value of Height(y)": sr3}
        df1 = pd.concat(d2, axis=1)
        print("After min_max normalization the table will be like:\n")
        print(df1)
        print("-------------------------------------------------------------------------------------")
        #standardization process
        u = SUM_X / 7
        #print(u)
        SUM_X_U = 0
        for i in x:
            SUM_X_U = SUM_X_U + ((i - u) ** 2)
        #print(SUM_X_U)
        SIG = ((SUM_X_U / 6) ** 0.5)
        #print(SIG)
        NEW_X = []
        for i in x:
            NEW_X.append((i - u) / SIG)
        #print("Now your new Weight(x) value list is:", NEW_X)
        SUM_X_NEW = 0
        for i in NEW_X:
            SUM_X_NEW = SUM_X_NEW + i
        #print(SUM_X_NEW)
        SUM_Xi_sqr_NEW = 0
        for i in NEW_X:
            SUM_Xi_sqr_NEW = SUM_Xi_sqr_NEW + (i * i)
        #print(SUM_Xi_sqr)
        arr4 = np.array(NEW_X)
        SUM_XiY_NEW = 0
        for i in (arr4 * arr2):
            SUM_XiY_NEW = SUM_XiY_NEW + i
        #print(SUM_XiY)
        #calculate the values of b0 & b1 with standardization
        b0_b1_Standard()
        #check the efficiency
        ni_new = 0
        for i in y:
            for j in Y_i_PRED_NEW:
                if int(i) == int(j):
                    ni_new = ni_new + 1
        #print(ni)
        sr = pd.Series(x)
        #print(sr)
        sr1 = pd.Series(y)
        #print(sr1)
        sr4 = pd.Series(Y_i_PRED_NEW)
        #print(sr4)
        d3 = {"Weight" : sr, "Height" : sr1, "Predicted value of Height(y)" : sr4}
        df3 = pd.concat(d3, axis=1)
        print("\nAfter standardization process the table will be like:\n")
        print(df3)
        print("-------------------------------------------------------------------------------------")
        
        #plotting data in graph
        plt.title("The graph will be like:")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.scatter(x, y, color = "m",marker = "o", s = 30)
        plt.plot(x, Y_PRED, color = "g")
        plt.show()       
else:
    SUM_X = 0
    for i in x:
        SUM_X = SUM_X + i
    #print(SUM_X)
    SUM_Y = 0
    for i in y:
        SUM_Y = SUM_Y + i
    #print(SUM_Y)
    SUM_X_sqr = 0
    for i in x:
        SUM_X_sqr = SUM_X_sqr + (i * i)
    #print(SUM_X_sqr)
    import numpy as np
    arr1 = np.array(x)
    arr2 = np.array(y)
    SUM_XY = 0
    for i in (arr1 * arr2):
        SUM_XY = SUM_XY + i
    #print(SUM_XY)

    A = float(input("Please enter the Weight(x) value:"))
    #calculate the values of b0, b1
    b0 = ((SUM_Y * SUM_X_sqr) - (SUM_X * SUM_XY)) / ((7 * SUM_X_sqr) - SUM_X ** 2)
    print("\nThe value of the first regression coefficient(b0) is =", b0)
    b1 = ((7 * SUM_XY) - (SUM_X * SUM_Y)) / ((7 * SUM_X_sqr) - SUM_X ** 2)
    print("The value of the second regression coefficient(b1) is = ", b1)
    print("The predicted Height(y) for the inputted value {} is = {} ".format(A, (b0 + (b1 * A))))
