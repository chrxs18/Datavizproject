# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:10:25 2020

@author: Utilisateur
"""

# Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ['PROJ_LIB'] ='/opt/anaconda3/lib/python3.7/site-packages/mpl_toolkits/basemap/data/'

from mpl_toolkits.basemap import Basemap


# Set the dimension of the figure
my_dpi=100
plt.figure(figsize=(2600/my_dpi, 1800/my_dpi), dpi=my_dpi)

# read the data
file=r"/Users/LN/Desktop/Projet_r/data.xlsx"
sheet="data" 
xl=pd.ExcelFile(file)
data=xl.parse(sheet)
data.head()


# Make the background map
m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")
 
# prepare a color for each point depending on the continent.
data['labels_enc'] = pd.factorize(data['Continent'])[0]
 
# Add a point per position
m.scatter(data['longitude'], data['latitude'], s=data['Nb_migrant']/10000, alpha=0.4, c=data['labels_enc'], cmap="Set1")
 
# data source informations
plt.text( -170, -58,'Where migrate the most between 2015 and 2019  #Data from the UN migration database / Plot realized with Python and the Basemap library', ha='left', va='bottom', size=7, color='#555555' )
plt.text( 170, 58,'Migration stocks in the world between 2015 and 2019', ha='right', va='bottom', size=7, color='#555555' )
plt.show()

# Save as png
plt.savefig('project.jpeg')
