# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

# Step 1: Preparation of your data
x=np.linspace(0,2,100)  # auto creation of a list containing 100 data
np.savetxt("myarray.txt",x,delimiter='')


#plt.plot(x,x,label='linear')
#plt.plot(x,x**2, label='Quadratic')
#plt.plot(x,x**3,label='cubic')

#plt.xlabel('x label')
#plt.ylabel('y label')

#plt.title("simple Plot")
#plt.legend()
#plt.show()

# Step 2: Create plot with the data created in Step 1.
fig,ax=plt.subplots(1,1)
ax.plot(x,x**2,label='Quadratic')

# Step 3: Customise plot, by giving it title, axis labels
ax.set(title='Quadratic Plotting',ylabel='Square of x',xlabel='X Value')    # Customising title, ylabel, and xlabel
ax.legend(loc='best')   #display the legend of y series

# Step 4: Save the plot to harddrive
plt.savefig('Square of x.png')

# Step 5: Show plot on screen
plt.show()

