#KNN Algorithm
##############

import pandas as pd
import numpy as np

x1 = [5.3, 5.1, 7.2, 5.4, 5.1, 5.4, 7.4, 6.1, 7.3, 6.0, 5.8, 6.3, 5.1, 6.3, 5.5]
x2 = [3.7, 3.8, 3.0, 3.4, 3.3, 3.9, 2.8, 2.8, 2.9, 2.7, 2.8, 2.3, 2.5, 2.5, 2.4]
cls = ['Setosa', 'Verscicolor', 'Virginica', 'Setosa', 'Verscicolor', 'Setosa', 'Virginica', 'Verscicolor', 'Virginica', 'Verscicolor', 'Virginica', 'Setosa', 'Verscicolor', ' Virginica', 'Verscicolor']

#taking input from user
y1 = float(input("Enter the first point: "))
y2 = float(input("Enter the second point: "))

#finding distance from user input data and given x1 & x2 data & converting list into dataframe
d = []
for i in range(len(x1)):
           d.append((((y2 - y1)**2) + ((x2[i] - x1[i])**2))**0.5)
#print(d)
sr = pd.Series(x1)
sr1 = pd.Series(x2)
sr2 = pd.Series(d)
sr3 = pd.Series(cls)
d_set = {'X1':sr, 'X2':sr1, "Distance":sr2, "Class":sr3,}
d_set1 = pd.concat(d_set, axis = 1)
print("\nAfter finding distance from the above two points the table will be:\n")
print(d_set1)
print("--------------------------------------------------------------------------")

#printing dataframe in sorted manner
dset = {'X1':sr, 'X2':sr1, "Distance":sr2, "Class":sr3,}
dset1 = pd.concat(dset, axis=1)
dset2 = dset1.sort_values(by = ["Distance"])
print("\nAfter sorting the table will be:\n")
print(dset2)
print("--------------------------------------------------------------------------")

#assuming k value and finding the frequency of classes
k = int(input("Enter the k value:"))
CLS = []
for i in dset2.loc[:,"Class"]:
    CLS.append(i)
#print(CLS)
CLS1 = CLS[:k]
#print(CLS1)

#finding frequency of classes
n, n1, n2, = 0, 0, 0
for i in CLS1:
    if i == "Setosa":
        n += 1
    elif i== "Verscicolor":
        n1 += 1
    elif i== "Virginica":
        n2 += 1
    else:
        exit()
#print(n,n1,n2)
if (n != n1) and (n != n2):
    if (n > n1) and (n > n2):
        print("The nearest neighbour class is Setosa")
    elif (n1 > n) and (n1 > n2):
        print("The nearest neighbour class is Verscicolor")
    else:
        print("The nearest neighbour is Virginica")
elif (n == n1) or (n == n2):
    print("Neighbour classes having  same frequecy")
    if (n == n1):
        print("The nearest neighbour classes are Setosa and Verscicolor")
    elif (n1 == n2):
        print("The nearest neighbour classes are Verscicolor and Virginica")
    elif (n == n2):
        print("The nearest neighbour classes are Setosa and Virginica")
    else:
        print("Invalid input")
else:
    print("Invalid input")
