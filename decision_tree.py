# decision tree
###############

import pandas as pd
import numpy as np

# reading dataset
dset = pd.read_csv("D:\\Codes\\ML\\Dataset\\dtree.csv")
print("The dataset is:")
print("---------------\n")
print(dset)
# finding decision column
print("\nSo, from the above dataset we can clearly see the decision column is Play Golf")
print("--------------------------------------------------------------------------------")
WETH = list(dset["Outlook"])
TEMP = list(dset["Temperature"])
HUMD = list(dset["Humidity"])
WIND = list(dset["Windy"])
P_GOLF = list(dset["Play Golf"])
n = 0
for i in P_GOLF:
    n += 1
# print(n)

# calculating entropy of decision column
c_t = 0
c_f = 0
for i in P_GOLF:
    if i == "Yes":
        c_t += 1
    else:
        c_f += 1
# print(c_t)
# print(c_f)
# E(Play GOlf)
E_playgolf = -(c_t / n * np.log2(c_t / n)) - (c_f / n * np.log2(c_f / n))
print("The Entropy of Decision column(Play Golf) will be:",E_playgolf)

# calculating the entropy of all classes w.r.t. decision column
# E(Play golf, Outlook)
c_s, c_o, c_r = 0, 0, 0
c_out_s_t1, c_out_s_f1, c_out_o_t1, c_out_o_f1, c_out_r_t1, c_out_r_f1 = 0, 0, 0, 0, 0, 0
for i in WETH:
    if(i == "Sunny"):
        c_s += 1
    elif(i == "Overcast"):
        c_o += 1
    else:
        c_r += 1
for (i, j) in zip(WETH, P_GOLF):
    if(i == "Sunny") and (j == "Yes"):
        c_out_s_t1 += 1
    elif(i == "Sunny") and (j == "No"):
        c_out_s_f1 += 1
    elif(i == "Overcast") and (j == "Yes"):
        c_out_o_t1 += 1
    elif(i == "Overcast") and (j == "No"):
        c_out_o_f1 += 1
    elif(i == "Rainy") and (j == "Yes"):
        c_out_r_t1 += 1
    elif(i == "Rainy") and (j == "No"):
        c_out_r_f1 += 1
    else:
        exit()
Entp_S = (-(c_out_s_t1/c_s * np.log2(c_out_s_t1/c_s)) - (c_out_s_f1/c_s * np.log2(c_out_s_f1/c_s)))
Entp_O = (-(c_out_o_t1/c_o * np.log2(c_out_o_t1/c_o)) - (c_out_o_f1/c_o * np.log2(c_out_o_f1/c_o)))
Entp_R = (-(c_out_r_t1/c_r * np.log2(c_out_r_t1/c_r)) - (c_out_r_f1/c_r * np.log2(c_out_r_f1/c_r)))
ENTP_PG_OL = ((c_s/n * Entp_S) + (c_o/n * Entp_O) + (c_r/n * Entp_R))
print("\nThe Entropy(Play Golf, Outlook) will be:",ENTP_PG_OL)

#E(Play Golf, Temperature)
c_h, c_m, c_c = 0, 0, 0
c_temp_h_t1, c_temp_h_f1, c_temp_m_t1, c_temp_m_f1, c_temp_c_t1, c_temp_c_f1 = 0, 0, 0, 0, 0, 0
for i in TEMP:
    if(i == "Hot"):
        c_h += 1
    elif(i == "Mild"):
        c_m += 1
    else:
        c_c += 1
for (i, j) in zip(TEMP, P_GOLF):
    if(i == "Hot") and (j == "Yes"):
        c_temp_h_t1 += 1
    elif(i == "Hot") and (j == "No"):
        c_temp_h_f1 += 1
    elif(i == "Mild") and (j == "Yes"):
        c_temp_m_t1 += 1
    elif(i == "Mild") and (j == "No"):
        c_temp_m_f1 += 1
    elif(i == "Cool") and (j == "Yes"):
        c_temp_c_t1 += 1
    elif(i == "Cool") and (j == "No"):
        c_temp_c_f1 += 1
    else:
        exit()
Entp_H = (-(c_temp_h_t1/c_h * np.log2(c_temp_h_t1/c_h)) - (c_temp_h_f1/c_h * np.log2(c_temp_h_f1/c_h)))
Entp_M = (-(c_temp_m_t1/c_m * np.log2(c_temp_m_t1/c_m)) - (c_temp_m_f1/c_m * np.log2(c_temp_m_f1/c_m)))
Entp_C = (-(c_temp_c_t1/c_c * np.log2(c_temp_c_t1/c_c)) - (c_temp_c_f1/c_c * np.log2(c_temp_c_f1/c_c)))
ENTP_PG_TP = ((c_h/n * Entp_H) + (c_m/n * Entp_M) + (c_c/n * Entp_C))
print("The Entropy(Play Golf, Temperature) will be:",ENTP_PG_TP)

#E(Play Golf, Humidity)
c_hg, c_n, = 0, 0
c_humd_h_t1, c_humd_h_f1, c_humd_n_t1, c_humd_n_f1 = 0, 0, 0, 0
for i in HUMD:
    if(i == "High"):
        c_hg += 1
    else:
        c_n += 1
for (i, j) in zip(HUMD, P_GOLF):
    if(i == "High") and (j == "Yes"):
        c_humd_h_t1 += 1
    elif(i == "High") and (j == "No"):
        c_humd_h_f1 += 1
    elif(i == "Normal") and (j == "Yes"):
        c_humd_n_t1 += 1
    elif(i == "Normal") and (j == "No"):
        c_humd_n_f1 += 1
    else:
        exit()
Entp_HG = (-(c_humd_h_t1/c_hg * np.log2(c_humd_h_t1/c_hg)) - (c_humd_h_f1/c_hg * np.log2(c_humd_h_f1/c_hg)))
Entp_N = (-(c_humd_n_t1/c_n * np.log2(c_humd_n_t1/c_n)) - (c_humd_n_f1/c_n * np.log2(c_humd_n_f1/c_n)))
ENTP_PG_HD = ((c_hg/n * Entp_HG) + (c_n/n * Entp_N))
print("The Entropy(Play Golf, Humidity) will be:",ENTP_PG_HD)

#E(Play Golf, Windy)
c_tr, c_fl, = 0, 0
c_wind_t_t1, c_wind_t_f1, c_wind_f_t1, c_wind_f_f1 = 0, 0, 0, 0
for i in WIND:
    if(i == "T"):
        c_tr += 1
    else:
        c_fl += 1
for (i, j) in zip(WIND, P_GOLF):
    if(i == "T") and (j == "Yes"):
        c_wind_t_t1 += 1
    elif(i == "T") and (j == "No"):
        c_wind_t_f1 += 1
    elif(i == "F") and (j == "Yes"):
        c_wind_f_t1 += 1
    elif(i == "F") and (j == "No"):
        c_wind_f_f1 += 1
    else:
        exit()
Entp_TR = (-(c_wind_t_t1/c_tr * np.log2(c_wind_t_t1/c_tr)) - (c_wind_f_f1/c_tr * np.log2(c_wind_f_f1/c_tr)))
Entp_FL = (-(c_wind_f_t1/c_fl * np.log2(c_wind_f_t1/c_fl)) - (c_wind_f_f1/c_fl * np.log2(c_wind_f_f1/c_fl)))
ENTP_PG_WD = ((c_tr/n * Entp_TR) + (c_fl/n * Entp_FL))
print("The Entropy(Play Golf, Windy) will be:",ENTP_PG_WD)
print("--------------------------------------------------------------------------------")

#calculating the information gain of all the classes
#Gain(Play Golf, Outlook)
GAIN_PG_OL = (E_playgolf - ENTP_PG_OL)
print("Thus, the Gain(Play Golf, Outlook) will be:",GAIN_PG_OL)
#Gain(Play Golf, Temperature)
GAIN_PG_TP = (E_playgolf - ENTP_PG_TP)
print("Thus, the Gain(Play Golf, Temperature) will be:",GAIN_PG_TP)
#Gain(Play Golf, Humidity)
GAIN_PG_HD = (E_playgolf - ENTP_PG_HD)
print("Thus, the Gain(Play Golf, Humidity) will be:",GAIN_PG_HD)
#Gain(Play Golf, Windy)
GAIN_PG_WD = (E_playgolf - ENTP_PG_WD)
print("Thus, the Gain(Play Golf, Windy) will be:",GAIN_PG_WD)
print("--------------------------------------------------------------------------------")

#finding the root node
if(GAIN_PG_OL > GAIN_PG_TP) and (GAIN_PG_OL > GAIN_PG_HD) and (GAIN_PG_OL > GAIN_PG_WD):
    print("The highest information gain is Outlook")
    print("So, the root node is Outlook")
elif(GAIN_PG_TP > GAIN_PG_OL) and (GAIN_PG_TP > GAIN_PG_HD) and (GAIN_PG_TP > GAIN_PG_WD):
    print("The highest information gain is Temperature") 
    print("So, the root node is Temperature")
elif(GAIN_PG_HD > GAIN_PG_OL) and (GAIN_PG_HD > GAIN_PG_TP) and (GAIN_PG_HD > GAIN_PG_WD):
    print("The highest information gain is Humidity") 
    print("So, the root node is Humidity")
else:
    print("The highest information gain is Windy") 
    print("So, the root node is Windy")
