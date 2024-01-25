# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:50:09 2021

@author: Moon
"""
#import
import pandas as pd
from random import randint
from pyomo.environ import *
import random
from pyomo.opt import SolverFactory, SolverStatus, TerminationCondition

#import from preprocessed data and preprocess for pyomo

df=pd.read_csv('Dictionary.csv')
dfINT=df[['DriverID','Cluster','Time[Increments of 15]']]
dfINT.rename(columns={'Time[Increments of 15]':'Time'},inplace=True)

# take 100 samples
samplesize=475 # SS=158,304,465==>50,100,150UniqueCars
dfINT=dfINT.head(samplesize)

# remove duplicated if any
dfINT=dfINT.drop_duplicates()

driverID=list(dfINT['DriverID'])
clusterSeq=range(0,20)
locationID=[]
for i in clusterSeq:
    locationID.append(i)#list(dfINT['Cluster'])
time15th=range(0,96)

def listUnique(lst):
    return list(set(lst))

driverIDUnique=listUnique(driverID)

locationIDUnique=listUnique(locationID)
time15thUnique=listUnique(time15th) 

locTime=[]
for i in locationIDUnique:
    for j in time15thUnique:
        locTime.append((i,j)) # Size = 20*96
#locTime=list(zip(locationIDUnique,time15thUnique))



# Create dict of mean price per minute for (location,time)
priceLocTime=pd.read_csv('price_data.csv')


# remove outliers from price Loc
import numpy as np
def find_outliers(x):
    Q1=np.percentile(x,25)
    Q3=np.percentile(x,75)
    IQR=Q3-Q1
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    outlier_ind=list(x.index[(x<lower)|(x>upper)])
    outlier_value=list(x[outlier_ind])
    return outlier_ind,outlier_value

# find_outliers(priceLocTime['PricePerMinute'])[1] ==> print the outlier values
priceLocTime=priceLocTime.drop(find_outliers(priceLocTime['PricePerMinute'])[0],axis=0)


temp1=pd.DataFrame(locTime,columns=["Node","Time"])
temp2=priceLocTime.groupby(['Node','Time'])['PricePerMinute'].mean()
temp2 = temp2.to_frame(name="MeanPricePerMinute").reset_index()
priceLocTime=temp1.merge(temp2,how="left",left_on=['Node','Time'],right_on=['Node','Time'])
priceLocTime['MeanPricePerMinute'].fillna(priceLocTime['MeanPricePerMinute'].mean(),inplace=True)

priceLocTimeD={}
for i in range(0,len(priceLocTime)):
    priceLocTimeD[priceLocTime['Node'][i],priceLocTime['Time'][i]]=priceLocTime['MeanPricePerMinute'][i] #comment out for dynamic VOT
    #priceLocTimeD[priceLocTime['Node'][i],priceLocTime['Time'][i]]=1.02 # avg VOT

# rough
# location = list(priceLocTime['Node'])
# time = list(priceLocTime['Time'][i])
# price = list(priceLocTime['MeanPricePerMinute'])
# import csv
# with open("priceLocTimeD","w") as f:
#     write = csv.writer(f, delimiter =",")
#     for i in zip(location, time, price):
#         write.writerow(i)

# export csv
# priceLocTimeD = pd.DataFrame(priceLocTimeD, index = list(range(0,len(priceLocTimeD)))) # https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi
# priceLocTimeD.to_csv("priceLocTimeD.csv")

# =============================================================================
# listkeysPriceLocTimeD=list(priceLocTimeD.keys())
# import numpy as np
# for i in range(0,len(priceLocTime)):
#     if np.isnan(priceLocTimeD[listkeysPriceLocTimeD[i]]):
#         priceLocTimeD[listkeysPriceLocTimeD[i]]=0
# =============================================================================
        
# Create distance dict
distance={}
distanceDf=pd.read_csv(r'Node_Distance.csv')
for i in range(0,len(distanceDf)):
    distance[distanceDf['Orgin Node'][i],distanceDf['Destination Node'][i]]=distanceDf['Distance'][i]

#export
# location1 = list(distanceDf['Orgin Node'])
# location2 = list(distanceDf['Destination Node'])
# distance = list(distanceDf['Distance'])
# import csv
# with open("distanceBetLocation","w") as f:
#     write = csv.writer(f, delimiter =",")
#     for i in zip(location1, location2, distance):
#         write.writerow(i)



# Create feasibility dict  
allCombList=[]
for i in driverIDUnique:
    for n in locationIDUnique:
        for t in time15thUnique:
            allCombList.append((i,n,t))

allCombDf=pd.DataFrame(allCombList,columns=["DriverID","Cluster","Time"])

dfINT.insert(3,"Feasible",[1]*len(dfINT))
allCombDfMerged=pd.merge(allCombDf,dfINT,how="left",left_on=['DriverID','Cluster','Time'],
                                right_on=['DriverID','Cluster','Time'])

allCombDfMerged['Feasible']=allCombDfMerged['Feasible'].fillna(0)

driverIDLocTime=list(zip(allCombDfMerged.DriverID,allCombDfMerged.Cluster,allCombDfMerged.Time))          
feasibilityDriverLocTime=dict(zip(driverIDLocTime,list(allCombDfMerged['Feasible'])))
feasibilittList = list(allCombDfMerged['Feasible'])
#export data
# import csv
# with open("feasibility3","w") as f:  # https://stackoverflow.com/questions/41135810/how-to-output-different-lists-to-different-column-python
#     write = csv.writer(f, delimiter =",")
#     for i in zip(driverIDLocTime,feasibilittList):
#         #write.writerow(driverIDLocTime[i])
#         write.writerow(i)
# with open("feasibilityID","w") as f:  # https://stackoverflow.com/questions/41135810/how-to-output-different-lists-to-different-column-python
#     write = csv.writer(f, delimiter =",")
#     for i in ziplistUnique(allCombDfMerged['DriverID'])):
#         #write.writerow(driverIDLocTime[i])
#         write.writerow(i)        
    

# Dictionary for speed
speed={}

for n in locationIDUnique:
    for m in locationIDUnique:
        for t in time15thUnique:
            speed[n,m,t]=round(random.uniform(10,30),2)


# export
# import csv
# location1 = list(list(speed.keys())[i][0] for i in range(0, len(speed)))
# location2 = list(list(speed.keys())[i][1] for i in range(0, len(speed)))
# time = list(list(speed.keys())[i][2] for i in range(0, len(speed)))
# speedVal = list(speed.values())      
# with open("speed2LocTime","w") as f:
#     write = csv.writer(f, delimiter = ",")
#     for i in zip(location1, location2, time, speedVal):
#         write.writerow(i)


# Dictionary for charging cost
unitChargingCost={}
for n in locationIDUnique:
    for t in time15thUnique:
       #unitChargingCost[n,t]=3.2
       unitChargingCost[n,t] = round(random.uniform(.10, .16),2)*20  # 20kwh*0.16/kwh => 3.2$
       # Curious: 2022 models https://insideevs.com/reviews/344001/compare-evs/

# follwoing porion added on 01/04/2022; previous cost ==> unitChargingCost
dfChargingDemand=pd.read_csv("final_output.csv")

for x in range(len(dfChargingDemand)): # Loop converts time to timeslot of 15 minutes
    time = dfChargingDemand.iloc[x]['Time']
    time = str(time)
    H,M,S = time.split(':')
    H = int(H)
    M = int(M)
    S = int(S)
    dfChargingDemand['Time'][x] = H*4 + int(M/15)


chargingDemand={}
for i in driverIDUnique:
    for t in time15thUnique:
        chargingDemand[i,t]=0
        
for i in driverIDUnique:
    for t in time15thUnique:
        for counter in range(len(dfChargingDemand)):
            if (i == dfChargingDemand['DriverID'][counter] and t == dfChargingDemand['Time'][counter]):
                chargingDemand[i,t]=dfChargingDemand['ChargeKwhNeeded'][counter]
           
                
            
        

# export 
# location = list(list(cost.keys())[i][0] for i in range(0,len(cost)))
# time = list(list(cost.keys())[i][1] for i in range(0,len(cost)))
# price = list(cost.values())
# import csv
# with open("cost","w") as f:
#     write = csv.writer(f, delimiter =",")
#     for i in zip(location, time, price):
#         write.writerow(i)


#creation of a concrete model
model=ConcreteModel()

#define sets
model.i=Set(initialize=driverIDUnique,doc="Drivers' ID, i")
model.n=Set(initialize=locationIDUnique,doc="Cluster, n")
model.t=Set(initialize=time15thUnique,doc="15th minutes charge needed, t")
model.m=Set(initialize=locationIDUnique,doc="Cluster, m")


#define parameters
model.w_nt=Param(model.n,model.t,initialize=priceLocTimeD,doc='timevalue for (location,time)')
model.w_mt=Param(model.m,model.t,initialize=priceLocTimeD,doc='timevalue for (location,time)')
model.N=Param(initialize=20,doc="max number of charging station")
model.aStartLoc=Param(model.i,model.m,model.t,initialize=feasibilityDriverLocTime,doc="feasibility of CS at that location n  and time t")

model.d=Param(model.n,model.m,initialize=distance,doc="distance between cluster")
model.chargeSpeedL2_7p7=Param(initialize=7.7,doc="Level 2 7.7kW unitChargingCost2500$, daily cost in 5 yrs = 1.37$ for dvlp and eqp each")
model.chargeSpeedDC50=Param(initialize=50,doc="DCFC 50kW cost 20000$, daily cost in 5 yrs = 3.84$ for dvlp and eqp each")
model.chargeSpeedDC150=Param(initialize=150,doc="DCFC 150kW cost 75600$, daily cost in 5 yrs = 14.5$ for dvlp and eqp each")

model.v=Param(model.n,model.m,model.t,initialize=speed,doc="speed at t from n to m distance")
model.c=Param(model.n,model.t,initialize=unitChargingCost,doc="charging cost at location n at timem t")
model.t_c=Param(initialize=(20/model.chargeSpeedDC50)*60,doc="to charge 20kWh with 50kW charger time required in minutes")
model.c_eqp=Param(initialize=3.84,doc="DC charging station plug equipment installation cost") # i.e., for DC50: 20000$/(365*5yrs)=10.96*.35=3.84$/day
model.c_dvlp=Param(initialize=3.84,doc="DC charging station development cost")
model.s_max=Param(initialize=10,doc="maximum number of charging station")
model.e = Param(model.i,model.t,initialize=chargingDemand,doc="charging needed in kwh")
#define variable
model.x=Var(model.i,model.n,model.t,within=Binary,doc='if driver i charges EV\
            at that lcoation n and time t')           
model.y_n=Var(model.n,within=Binary,doc='if the location has vacant charging station')
model.z=Var(model.i,model.n,model.m,model.t,within=Binary,doc='charging relocation variable')
model.s=Var(model.n,within=NonNegativeIntegers,doc="# of charging plugs")



                                  
def chargingStationVacancyRule(model,i,n,t):
    return model.x[i,n,t]<= model.y_n[n]
model.chargingStationVacancy=Constraint(model.i,model.n,model.t,rule=chargingStationVacancyRule,doc="a\
                            driver only able to charge where chraging station is vacant")
                                           
def maxStationRule(model):
    return sum(model.y_n[n] for n in model.n) <= model.N              
model.maxStation=Constraint(rule=maxStationRule,doc="maximum number of station")

def relocationOnceInDayRule(model,i):
    return sum(model.z[i,n,m,t] for n in model.n for m in model.m for t in model.t)==1
model.relocationOnceInDay=Constraint(model.i,rule=relocationOnceInDayRule,doc="assumption:only one successful relocation is allowed")


def relocationRequirementCheckRule(model,i,n,m,t):
    #return sum(model.z[i,n,m,t] for m in model.m) <=model.aStartLoc[i,n,t]
    return model.z[i,n,m,t] <=model.aStartLoc[i,n,t]
model.relocationRequirementCheck=Constraint(model.i,model.n,model.m,model.t,rule=relocationRequirementCheckRule,doc="if initial location is feasible\
                                            then target to relocate, otherwise not")


def relocationTimeCostRule(model,i,n,m,t):
    if t>=0 and t<=95-(round((model.d[n,m]/model.v[n,m,t])*4)): 
        #if  (round(model.d[n,m]/model.v[n,m,t]*4))>=1: # when distance 0 at time 0 x[i,0,-1] appearcs which not avaialbale
        return model.z[i,n,m,t]<=model.x[i,m,(t+(round(model.d[n,m]/model.v[n,m,t]*4)))]
        #else:
            #return model.z[i,n,m,t]<=model.x[i,m,t]
    elif t>95-(round((model.d[n,m]/model.v[n,m,t])*4)):
        return model.z[i,n,m,t]==0
model.relocationTimeCost=Constraint(model.i,model.n,model.m,model.t,rule=relocationTimeCostRule,doc="address relocation time and relation between x and z")
 
def plugInstallationLimitRule(model,n):
    return model.s[n] <= model.s_max*model.y_n[n]
model.plugInstallationLimit=Constraint(model.n,rule=plugInstallationLimitRule,doc="# of plug cannot exceed budget for that station")


def countPlugRule(model,n,t):
    return model.s[n] >= sum(model.x[i,n,t] for i in model.i)
model.countPlug=Constraint(model.n,model.t,rule=countPlugRule,doc="at a particular time and location total charging demand is numbe of plug")


#define objective function
def objectiveRule(model):
    
    exp1=sum(model.c[n,t]*model.e[i,t]*model.x[i,n,t] for i in model.i for n in model.n\
               for t in model.t)
    exp2=sum((model.t_c+(model.d[n,m]/model.v[n,m,t]))*model.z[i,n,m,t]*model.w_nt[n,t] for i in model.i for n in model.n for m in model.m\
             for t in model.t)
    exp3=sum(model.c_eqp*model.s[n] for n in model.n)
    exp4=sum(model.c_dvlp*model.y_n[n] for n in model.n)
    return exp1+exp2+exp3+exp4
        
model.objective=Objective(rule=objectiveRule,sense=minimize,doc="objective function")


    


solvername='cplex'
#solverpath_exe='C:/Users/md894973/2021_charging_infrastructure_ridesourcing_VOT/2021_charging_infrastructure_ridesourcing_VOT/src/winglpk-4.65/glpk-4.65/w64/glpsol' 
solver=SolverFactory(solvername)
import time
t1=time.perf_counter()
results=solver.solve(model) # tee =True gives the progress
t2=time.perf_counter()
elapsed_time=t2-t1
results.write()

# elapsed_time
# # Find Development cost i.e., cs cost
# dvlpCost=sum(model.c_dvlp.value*model.y_n[n].value for n in model.n)
# print(f'Development cost = {dvlpCost}')

# # Find equipment cost i.e., plug cost 
# equipCost=sum(model.c_eqp.value*model.s[n].value for n in model.n)
# print(f'Equipment cost = {equipCost}')

# # Charging cost
# chargeCost=sum(model.c[n,t]*model.x[i,n,t].value for i in model.i for n in model.n\
#                for t in model.t)
# print(f'Charging cost = {chargeCost}')

# # VOT cost
# votCost=sum((model.t_c+(model.d[n,m]/model.v[n,m,t]))*model.z[i,n,m,t].value*model.w_nt[n,t] for i in model.i for n in model.n for m in model.m\
#              for t in model.t)
# print(f'VOT cost = {votCost}')

# OptimalCS
for i in model.n:
    print(f'{i} : {model.y_n[i].value}')
for i in model.n:
    print(f'{i} : {model.s[i].value}')    
# Solver status
# results=solver.solve(model,tee=True)


# Check any x[i,n,t] grterthan 0 value
count=0
for i in model.i:
    for n in model.n:
        for t in model.t:
            if model.x[i,n,t].value==1:
                #print((i,n,t))
                print(f'{(i,n,t)}')
                count+=1


# Check any z[i,n,m,t] grterthan 0 value
count=0
for i in model.i:
    for n in model.n:
         for m in model.m:
            for t in model.t:
                if model.z[i,n,m,t].value==1:
                    print(f'{(i,n,m,t)} ')
                    count+=1
                    
for i in model.n:
    print(model.y_n[i].value)
    
for i in model.n:
    print(model.s[i].value)



# write charging info and price
import csv
filename='chargingL2InfoN'+str(model.N.value)+'Sample'+str(samplesize)
with open(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\%s.csv'%filename,mode='w') as csv_file:
    count=0
    sumPrice=0
    fieldnames=['i','m','t']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for i in model.i:
        for m in model.m:
            for t in model.t:
                if model.x[i,m,t].value==1:
                    writer.writerow({'i':i,'m':m,'t':t})
                    sumPrice+=priceLocTimeD[m,t]
                    count+=1

# Total cost
filename='totalCostL2N'+str(model.N.value)+'Sample'+str(samplesize)
with open(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\%s.txt'%filename,mode='w') as txt_file:
    txt_file.write('Total cost: '+ str(model.objective.value())+"\n"+"Elapsed time: "+str(elapsed_time))
                           
filename='#usedClusterL2N'+str(model.N.value)+'Sample'+str(samplesize)
with open(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\%s.txt'%filename,mode='w') as txt_file:
    usedClusterNo=0
    for i in range(0,20): # 20 is optimized cluster number
        usedClusterNo+=model.y_n[i].value
    txt_file.write('Total used cluster '+ str(usedClusterNo))

# write relocation info and price
import csv
filename='relocationInfoL2N'+str(model.N.value)+'Sample'+str(samplesize)
with open(r'C:\Users\Moon\OneDrive - Knights - University of Central Florida\2021_TRBCSAPRideAustin\2021trbrideaustincsa\%s.csv'%filename,mode='w') as csv_file:
    count=0
    sumPrice=0
    fieldnames=['i','n','m','t']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for i in model.i:
        for n in model.n:
            for m in model.m:
                for t in model.t:
                    if model.z[i,n,m,t].value==1:
                        writer.writerow({'i':i,'n':n,'m':m,'t':t})
                        sumPrice+=priceLocTimeD[m,t]
                        if (n!=m):
                            count+=1

# # To check why infeasible
# from pyomo.util.infeasible import log_infeasible_constraints

# SolverFactory('cplex').solve(model)

# log_infeasible_constraints(model)
