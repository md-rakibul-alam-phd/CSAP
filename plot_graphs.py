# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:29:01 2021

@author: md894973
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\summaryResults2.csv')

# SA:charger type 

VOTCostpV=[df['VOTCost/veh'][i] for i in range(1,4)]
devCostpV=[df['DvlpCost(cent)/veh'][i] for i in range(1,4)]
eqpCostpV=[df['EqipCost/veh'][i] for i in range(1,4)]
chargerType=["Level 2","DCFC-50","DCFC-150"]
# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(10,10))
# make a plot
ax.plot(chargerType, VOTCostpV,label="VOT cost", color="red",marker="o")
# set x-axis label
ax.set_xlabel("Charger type",fontsize=20)
# set y-axis label
ax.set_ylabel("VOT cost ($/EV)",fontsize=20)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(chargerType, devCostpV,label="Development cost",color="blue",marker="^")
ax2.plot(chargerType, eqpCostpV,label="Equipment cost",color="green",marker="s")
ax2.set_ylabel("Development and equipment cost (cent/EV)",fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax2.tick_params(axis='both',which='major',labelsize=20)
#ax.legend(fontsize=20)
#ax2.legend(fontsize=20,loc=0)

# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0,fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costCharger.png')


# SA:fleet size cost/EV

VOTCostpV=[df['VOTCost/veh'][i] for i in range(4,7)]
devCostpV=[df['DvlpCost(cent)/veh'][i] for i in range(4,7)]
eqpCostpV=[df['EqipCost/veh'][i] for i in range(4,7)]
fleetSize=["50","100","150"]
# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(10,10))
# make a plot
ax.set_ylim(0,30)

ax.plot(fleetSize, VOTCostpV,label="VOT cost", color="red",marker="o")
# set x-axis label
ax.set_xlabel("Fleet size",fontsize=20)
# set y-axis label
ax.set_ylabel("VOT cost ($/EV)",fontsize=20)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
ax2.set_ylim(0,30)
# make a plot with different y-axis using second axis object
ax2.plot(fleetSize, devCostpV,label="Development cost",color="blue",marker="^")
ax2.plot(fleetSize, eqpCostpV,label="Equipment cost",color="green",marker="s")
ax2.set_ylabel("Development and equipment cost (cent/EV)",fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax2.tick_params(axis='both',which='major',labelsize=20)
#ax.legend(fontsize=20)
#ax2.legend(fontsize=20,loc=0)

# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0,fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costFleetSize.png')

 

# SA:fleet size total cost

VOTCost=[df['VOTCost'][i] for i in range(4,7)]
devCost=[df['DevelopmentCost'][i] for i in range(4,7)]
eqpCost=[df['EquipmentCost'][i] for i in range(4,7)]
fleetSize=["50","100","150"]
# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(10,10))
# make a plot


ax.plot(fleetSize, VOTCost,label="VOT cost", color="red",marker="o")
# set x-axis label
ax.set_xlabel("Fleet size",fontsize=20)
# set y-axis label
ax.set_ylabel("VOT cost ($)",fontsize=20)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()

# make a plot with different y-axis using second axis object
ax2.plot(fleetSize, devCost,label="Development cost",color="blue",marker="^")
ax2.plot(fleetSize, eqpCost,label="Equipment cost",color="green",marker="s")
ax2.set_ylabel("Development and equipment cost ($)",fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax2.tick_params(axis='both',which='major',labelsize=20)
#ax.legend(fontsize=20)
#ax2.legend(fontsize=20,loc=0)

# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0,fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\totalcostFleetSize.png')


# Government incentive

VOTCostpV=[df['VOTCost/veh'][i] for i in range(7,10)]
devCostpV=[df['DvlpCost(cent)/veh'][i] for i in range(7,10)]
eqpCostpV=[df['EqipCost/veh'][i] for i in range(7,10)]
incentive=[df['Rebate'][i] for i in range(7,10)]
# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(8,8))
# make a plot
#ax.set_ylim(0,30)

ax.plot(incentive, VOTCostpV,label="VOT cost", color="red",marker="o")
# set x-axis label
ax.set_xlabel("Incentive",fontsize=20)
# set y-axis label
ax.set_ylabel("VOT cost ($/EV)",fontsize=20)
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
ax2.set_ylim(0,30)
# make a plot with different y-axis using second axis object
ax2.plot(incentive, devCostpV,label="Development cost",color="blue",marker="^")
ax2.plot(incentive, eqpCostpV,label="Equipment cost",color="green",marker="s")
ax2.set_ylabel("Development and equipment cost (cent/EV)",fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax2.tick_params(axis='both',which='major',labelsize=20)
#ax.legend(fontsize=20)
#ax2.legend(fontsize=20,loc=0)

# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0,fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costincentive.png')


# The following codes were to develop visualization for initial draft of the paper.

#-----------------------------------------------------------------------------
# Count the frequency of each cluster
df=pd.read_csv(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\Dictionary.csv')
df['Cluster']=df['Cluster'].astype(str)
countPCluster=df['Cluster'].value_counts()
countPClusterDf=countPCluster.to_frame().reset_index()

#import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(10,10))
ax.bar(countPClusterDf['index'],countPClusterDf['Cluster'])
ax.set_xlabel('Cluster ID',fontsize=20)
ax.set_ylabel('Frequency of feasibility for charging',fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\freqFeasibilitypClusterBar.png')
#-----------------------------------------------------------------------------

# Plotting cost per fleet line plot DC fast charging
dfDC=pd.read_csv(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\summaryResults.csv')
samplesizeGroupObj=dfDC.groupby('SampleSize')
group100=samplesizeGroupObj.get_group(100)
group100['MaximumClusterNo']=group100['MaximumClusterNo'].astype(str)
group200=samplesizeGroupObj.get_group(200)
group200['MaximumClusterNo']=group200['MaximumClusterNo'].astype(str)
group300=samplesizeGroupObj.get_group(300)
group300['MaximumClusterNo']=group300['MaximumClusterNo'].astype(str)

fig,ax=plt.subplots(figsize=(10,10))
ax.set_ylim(24.25,25.75)
ax.plot(group100['MaximumClusterNo'],group100['TotalCost($)PerVehicle'],label='Fleet size = 31',linewidth=3,marker='^',markersize=8)
ax.plot(group200['MaximumClusterNo'],group200['TotalCost($)PerVehicle'],label='Fleet size = 65',linewidth=3,marker='^',markersize=8)
ax.plot(group300['MaximumClusterNo'],group300['TotalCost($)PerVehicle'],label='Fleet size = 99',linewidth=3,marker='^',markersize=8)
ax.set_xlabel('Maximum limit of charging stations in model',fontsize=20)
ax.set_ylabel('Total cost per vehicle ($/EV)',fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax.legend(fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costpFleet.png')

# Plotting cost per fleet line plot L2 charging
dfL2=pd.read_csv(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\summaryResultsL2.csv')
samplesizeGroupObj=dfL2.groupby('SampleSize')
group100=samplesizeGroupObj.get_group(100)
group100['MaximumClusterNo']=group100['MaximumClusterNo'].astype(str)
group200=samplesizeGroupObj.get_group(200)
group200['MaximumClusterNo']=group200['MaximumClusterNo'].astype(str)
group300=samplesizeGroupObj.get_group(300)
group300['MaximumClusterNo']=group300['MaximumClusterNo'].astype(str)

fig,ax=plt.subplots(figsize=(10,10))
ax.set_ylim(143,149)
ax.plot(group100['MaximumClusterNo'],group100['TotalCost($)PerVehicle'],label='Fleet size = 31',linewidth=3,marker='^',markersize=8)
ax.plot(group200['MaximumClusterNo'],group200['TotalCost($)PerVehicle'],label='Fleet size = 65',linewidth=3,marker='^',markersize=8)
ax.plot(group300['MaximumClusterNo'],group300['TotalCost($)PerVehicle'],label='Fleet size = 99',linewidth=3,marker='^',markersize=8)
ax.set_xlabel('Maximum limit of charging stations in model',fontsize=20)
ax.set_ylabel('Total cost per vehicle ($/EV)',fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax.legend(fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costpFleet.png')

# Comaprison of cost for DC and L2
fig,ax=plt.subplots(figsize=(10,10))
labels=['6','15']
x=np.arange(len(labels))
width=.25 # width of the bars
ax.bar(x-width/2, group100['TotalCost($)PerVehicle'],width,label='DC fast charging')
ax.bar(x+width/2,group100['TotalCost($)PerVehicle DC'],width, label='Level 2 charging')
ax.set_xlabel('Optimal allocation of charging station',fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Average of total cost ($/EV)',fontsize=20)
ax.tick_params(axis='both',which='major',labelsize=20)
ax.legend(fontsize=20)
plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\dcVsL2Cost.png')

















# =============================================================================
# fig,ax=plt.subplots(figsize=(10,10))
# ax.set_ylim(2,12)
# ax.plot(group100['MaximumClusterNo'],group100['RelocationCostPerVehicle'],label='Fleet size = 31')
# ax.plot(group200['MaximumClusterNo'],group200['RelocationCostPerVehicle'],label='Fleet size = 65')
# ax.plot(group300['MaximumClusterNo'],group300['RelocationCostPerVehicle'],label='Fleet size = 99')
# ax.set_xlabel('Number of allocated charging stations',fontsize=20)
# ax.set_ylabel('VOT cost from relocation (cent/minute/EV)',fontsize=20)
# ax.tick_params(axis='both',which='major',labelsize=20)
# ax.legend(fontsize=20)
# plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\relocationVOTpFleet.png')
# 
# =============================================================================




# =============================================================================
# # Increasing rate of allocated cluster for different fleet size
# 
# fleetSize=[31]*6
# fleetSize.extend([65]*6)
# fleetSize.extend([99]*6)
# maxCS=[6,9,12,15,18,20]*3
# allocateCS=[6,9,12,12,12,12,6,9,12,15,15,15,6,9,12,15,18,20]
# 
# dfMaxVsAllocated=pd.DataFrame({'fleetSize':fleetSize,'maxCS':maxCS,'allocatedCS':allocateCS})
# 
# 
# temp=dfMaxVsAllocated.groupby('fleetSize')
# maxAllo36Fleet=temp.get_group(31)
# maxAllo65Fleet=temp.get_group(65)
# maxAllo99Fleet=temp.get_group(99)
# 
# fig,ax=plt.subplots(figsize=(10,10))
# #ax.set_ylim(24,26)
# ax.plot(maxAllo36Fleet['maxCS'],maxAllo36Fleet['allocatedCS'],label='Fleet size = 31',linewidth=2,marker='^',markersize=6)
# ax.plot(maxAllo65Fleet['maxCS'],maxAllo65Fleet['allocatedCS'],label='Fleet size = 65',linewidth=2,marker='^',markersize=6)
# ax.plot(maxAllo99Fleet['maxCS'],maxAllo99Fleet['allocatedCS'],label='Fleet size = 99',linewidth=2,marker='^',markersize=6)
# ax.set_xlabel('Maximum limit of charging stations in model',fontsize=20)
# ax.set_ylabel('Allocated number of charging stations',fontsize=20)
# ax.tick_params(axis='both',which='major',labelsize=20)
# ax.legend(fontsize=20)
# plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\maxVsAllocated.png')
# #-----------------------------------------------------------------------------------------------------------------
# 
# =============================================================================
# =============================================================================
# # Count for relocation from
# relocatedFromN20S300=[]
# ODN20S300Df=pd.read_csv(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\relocationInfoPriceN20Sample300.csv')
# #ODN20S300=pd.pivot_table(ODN20S300Df,index=['n'],columns=['m'],values=['i'],aggfunc='count')
# for i in range(0,len(ODN20S300Df)):
#     if ODN20S300Df['n'][i]!=ODN20S300Df['m'][i]:
#         ODN20S300Df.at[i, 'From']=ODN20S300Df['n'][i]
# 
# tempSeries=ODN20S300Df['From'].value_counts() 
# tempFrame=tempSeries.to_frame().reset_index()
# tempFrame.rename(columns={'index':'From','From':'Count'},inplace=True)# from: charging station, index:count
# tempFrame['From']=tempFrame['From'].astype(int) 
# tempFrame['From']=tempFrame['From'].astype(str)      
# 
# fig,ax=plt.subplots(figsize=(10,10))
# #ax.set_ylim(25,30)
# ax.bar(tempFrame['From'],tempFrame['Count'])
# ax.set_xlabel('Charging station ID',fontsize=20)
# ax.set_ylabel('Frequency of relocation from charging station',fontsize=20)
# ax.tick_params(axis='both',which='major',labelsize=20)
# plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\frequencyRelocationFromN20S300.png')
# #--------------------------------------------------------------------------------------------------------------------
# 
# # Plot stakedbar for cost
# 
# labels1 = list(group100['MaximumClusterNo'].astype(str))
# chargingVOT1 = list(group100['ChargingCost(cent)PerVehicle'])
# relocationVOT1 = list(group100['RelocationCostPerVehicle'])
# 
# 
# labels2 = list(group200['MaximumClusterNo'].astype(str))
# chargingVOT2 = list(group200['ChargingCost(cent)PerVehicle'])
# relocationVOT2 = list(group200['RelocationCostPerVehicle'])
# 
# 
# labels3 = list(group300['MaximumClusterNo'].astype(str))
# chargingVOT3 = list(group300['ChargingCost(cent)PerVehicle'])
# relocationVOT3 = list(group300['RelocationCostPerVehicle'])
#     
#     
#     
# #import matplotlib.pyplot as plt
# 
# 
# width = 0.5      # the width of the bars: can also be len(x) sequence
# 
# fig, (ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3,figsize=(20,10))
# 
# ax1.bar(labels1, chargingVOT1, width,  label='Charge')
# ax1.bar(labels1, relocationVOT1, width,  bottom=chargingVOT1,
#        label='Relocation')
# ax1.tick_params(axis='both',which='major',labelsize=20)
# ax1.set_ylabel('VOT cost (cent/minute/vehicle)',fontsize=20)
# ax1.set_xlabel('Fleet size = 31',fontsize=20)
# ax1.legend(loc=1,fontsize=15)
# 
# ax2.bar(labels2, chargingVOT2, width,  label='Charge')
# ax2.bar(labels2, relocationVOT2, width,  bottom=chargingVOT2,
#        label='Relocation')
# ax2.tick_params(axis='both',which='major',labelsize=20)
# #ax2.set_ylabel('VOT cost (cent/minute/vehicle)',fontsize=20)
# ax2.set_xlabel('Fleet size = 65',fontsize=20)
# ax2.legend(loc=1,fontsize=15)
# 
# ax3.bar(labels3, chargingVOT3, width,  label='Charge')
# ax3.bar(labels3, relocationVOT3, width,  bottom=chargingVOT3,
#        label='Relocation')
# ax3.tick_params(axis='both',which='major',labelsize=20)
# #ax3.set_ylabel('VOT cost (cent/minute/vehicle)',fontsize=20)
# ax3.set_xlabel('Fleet size = 99',fontsize=20)
# ax3.legend(loc=1,fontsize=15)
# 
# fig.suptitle("Number of allocated charging stations",fontsize=20,y=-.005)
# 
# plt.savefig(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\costStacked.png')
# 
# 
# =============================================================================
