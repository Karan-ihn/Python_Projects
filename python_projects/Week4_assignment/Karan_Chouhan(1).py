import numpy as np
import matplotlib.pyplot as mplt
import scipy.signal as ss
import random

# main program for obatining the data to plot
total_outcomes_pairs = {3:0, 4:0, 5:0, 6:0, 7:0, 8:0,
                        9:0, 10:0, 11:0, 12:0, 13:0,
                        14:0, 15:0, 16:0, 17:0, 18:0}
dice1 = [i for i in range(1,7)]
dice2 = [i for i in range(1,7)]
dice3 = [i for i in range(1,7)]
for roll in range(1000):
    random.shuffle(dice1)
    random.shuffle(dice2)
    random.shuffle(dice3)
    if dice1[0]+dice2[0]+dice3[0] in total_outcomes_pairs.keys():
        total_outcomes_pairs[dice1[0]+dice2[0]+dice3[0]]+=1

# dataset for plotting the curve and the bar graph
x = np.array(list(total_outcomes_pairs.keys()))
y = np.array(list(total_outcomes_pairs.values()))/1000

Y_data = ss.savgol_filter(y,15,6)  #smoothening the data for obtaining smooth curve

# Curve plotting
mplt.plot(x,Y_data,'r')
mplt.plot(x,y,'bo',label='actual data')

mplt.xlabel('Sum of the numbers on 3 dice')
mplt.ylabel('Probability of the respective Sum')

mplt.title('Probability Distribution Curve for Sum of the numbers on 3 dice')
mplt.legend()
mplt.show()

# bar graph plotting
mplt.bar(x,y,tick_label=x,width=0.6,color=['red','blue','green','yellow','violet'])
mplt.xlabel('Sum of the three dice')
mplt.ylabel('probabilities of the sum on the three dice')
mplt.title('Bar-graph of probabilities of Sum of numbers on 3 dice on a different plot.')
mplt.show()