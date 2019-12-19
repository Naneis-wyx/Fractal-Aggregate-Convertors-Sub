from tkinter import *
import tkinter as tk
import math
from decimal import Decimal
from tkinter import ttk
import tkinter.messagebox
import statistics




root = tk.Tk()
title = root.title("Fractal-Aggregate-Convertors-Sub")
#Instruction1 sr=subroutin
Instrcutsr1=tk.Label(root, text="Please choose default gas and \u03C3 or Input other data").grid(row=0,column=0,columnspan=6)
Airchoice=['Air            0.36X10\u207b\u00B9\u2078','N\u2082             0.43X10\u207b\u00B9\u2078','O\u2082             0.40X10\u207b\u00B9\u2078','He            0.21X10\u207b\u00B9\u2078','CO\u2082          0.52X10\u207b\u00B9\u2078','Ne            0.24X10\u207b\u00B9\u2078','Input']
choiceAirVar=tk.StringVar()
choiceAirVar.set(Airchoice[0])
AirBox=ttk.Combobox(root,textvariable=choiceAirVar,values=Airchoice).grid(row=1,column=0)
AirEntry=tk.Entry(root)
AirEntry.grid(row=1,column=1)
labAirunit=tk.Label(root,text="X10\u207b\u00B9\u2078m\u00b2").grid(row=1,column=2,sticky=W)

#Instruction2 
Instructsr2= tk.Label(root, text="Please choose default temperature or input data").grid(row=2,column=0,columnspan=6)
#temperature
tempEntry=tk.Entry(root)
tempEntry.grid(row=3,column=1,sticky=W)
tempunit=['default=298.15K','\u00b0C','\u00b0F',' K']
choicetempVar=tk.StringVar()
choicetempVar.set(tempunit[0])
Tempunit=ttk.Combobox(root,textvariable=choicetempVar,values=tempunit).grid(row=3,column=0)

#Instruction3
Instructsr3=tk.Label(root, text="Step1:Please choose default Pressure or input data").grid(row=4,column=0,columnspan=6)
Presschoice=['101325 Pa','Input']
choicePressVar=tk.StringVar()
choicePressVar.set(Presschoice[0])
PressBox=ttk.Combobox(root,textvariable=choicePressVar,values=Presschoice).grid(row=5,column=0)
PressEntry=tk.Entry(root)
PressEntry.grid(row=5,column=1,sticky=W)
labAirunit=tk.Label(root,text="Pa").grid(row=5,column=2,sticky=W)

#Calculate Subroutin1
def Calculatesub1():
     global lamda
     #detect air
     if(choiceAirVar.get())==Airchoice[0]:
          sigma = 0.36*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[1]:
          sigma = 0.43*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[2]:
          sigma = 0.40*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[3]:
          sigma = 0.21*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[4]:
          sigma = 0.52*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[5]:
          sigma = 0.24*pow(10,-18)
     if(choiceAirVar.get())==Airchoice[6]:
          sigma = float(AirEntry.get())*pow(10,-18)

     #detect pressure
     if(choicePressVar.get())==Presschoice[0]:
          P = 101325
     if(choicePressVar.get())==Presschoice[1]:
          P = float(PressEntry.get())

     #detect temperature
     if(choicetempVar.get())==tempunit[0]:
          T = 298.15
     if(choicetempVar.get())==tempunit[1]:
          T = float(tempEntry.get()) + 273.15
     if(choicetempVar.get())==tempunit[2]:
          T = float(tempEntry.get())*9/5+273.15
     if(choicetempVar.get())==tempunit[3]:
          T = float(tempEntry.get())
     #Set Kb
     Kb=1.38064852*pow(10,-23)
     #calculate lamda
     lamda=(Kb*T)/(pow(2,1/2)*P*sigma)*pow(10,9)  
     print('\u03C3:',sigma,'Pressure',P,'Temperature',T,'\u03BB',lamda)    
button=tk.Button(root,text="Calculate \u03bb",command=Calculatesub1).grid(row=6,sticky = "nsew")

#----------------------------------------------------------------------------------------

Instruct= tk.Label(root, text="Step2: Please import 2 of 3 in SIZE, GRAM, DENSITY ").grid(row=7,column=0,columnspan=4)


#lab part
#Particle size
labsize=tk.Label(root,text="Particle electrical mobility size(Dp)").grid(row=8,sticky=W)
sizeEntry=tk.Entry(root)
sizeEntry.grid(row=8,column=1,sticky = W)

sizeunit=['m','mm','\u03BCm','nm']
choicesizeVar=tk.StringVar()
choicesizeVar.set(sizeunit[0])
sunit=ttk.Combobox(root,textvariable=choicesizeVar,values=sizeunit).grid(row=8,column=2)




#Particle mass
labmass=tk.Label(root,text="Particle absolute mass(m)").grid(row=9,sticky=W)
massEntry=tk.Entry(root)
massEntry.grid(row=9,column=1,sticky = W)

massunit=['kg','g','ng','fg']
choicemassVar=tk.StringVar()
choicemassVar.set(massunit[0])
munit=ttk.Combobox(root,textvariable=choicemassVar,values=massunit).grid(row=9,column=2)



#Particle
labdensity=tk.Label(root,text="Particle effective density(\u03C1eff)").grid(row=10,sticky=W)
densityEntry=tk.Entry(root)
densityEntry.grid(row=10,column=1,sticky = W)


denunit=['g/cm\u00B3','kg/m\u00B3']
choicedenVar=tk.StringVar()
choicedenVar.set(denunit[0])
sunit=ttk.Combobox(root,textvariable=choicedenVar,values=denunit).grid(row=10,column=2)


 
def calculation1():
     global mass
     global density
     global size
     
     if len(sizeEntry.get()) == 0:
          mass=float(massEntry.get())
          #convert unit
          if(choicemassVar.get())=='kg':
               mass=mass*1000
          if(choicemassVar.get())=='g':
               mass=mass
          if(choicemassVar.get())=='ng':
               mass=mass*pow(10,-9)
          if(choicemassVar.get())=='fg':
               mass=mass*pow(10,-15)
               
          
          density=float(densityEntry.get())
          if(choicedenVar.get())=='g/cm\u00B3':
               density=density
          if(choicedenVar.get())=='kg/m\u00B3':
               density=density*1000
               
          temp = mass/density/math.pi*6
          size = pow(temp,1.0/3)
          alg='size=(mass/density/math.pi*6)^1/3'

     if len(massEntry.get()) == 0:
          
          size=float(sizeEntry.get())
          if(choicesizeVar.get())=='m':
               size=size*100
          if(choicesizeVar.get())=='mm':
               size=size*0.1
          if(choicesizeVar.get())=='\u03BCm':
               size=size*pow(10,-4)
          if(choicesizeVar.get())=='nm':
               size=size*pow(10,-7)
               
          density=float(densityEntry.get())
          if(choicedenVar.get())=='g/cm\u00B3':
               density=density
          if(choicedenVar.get())=='kg/m\u00B3':
               density=density*1000
          temp = pow(size,3)
          mass = density * math.pi/6*temp
          alg='mass = density * math.pi/6*temp'

     if len(densityEntry.get()) == 0:
          size=float(sizeEntry.get())
          if(choicesizeVar.get())=='m':
               size=size*100
          if(choicesizeVar.get())=='mm':
               size=size*0.1
          if(choicesizeVar.get())=='\u03BCm':
               size=size*pow(10,-4)
          if(choicesizeVar.get())=='nm':
               size=size*pow(10,-7)
               
          mass=float(massEntry.get())
          if(choicemassVar.get())=='kg':
               mass=mass*1000
          if(choicemassVar.get())=='g':
               mass=mass
          if(choicemassVar.get())=='ng':
               mass=mass*pow(10,-9)
          if(choicemassVar.get())=='fg':
               mass=mass*pow(10,-15)
               
          temp = pow(size,3)
          density = mass*6/temp/math.pi
          
          alg='density = mass*6/temp/math.pi'

               
     Result = ("density:",density,"mass:",mass,"size:",size)
     tk.messagebox.showinfo("Result",Result)
     
     
     
     
button=tk.Button(root,text="Calculate",command=calculation1).grid(row=11,column=0,sticky = "nsew")
#---------------------------------------------------------------------------------------
labDiameter=tk.Label(root,text="Step3:Primary Particle diameter and Diameter").grid(row=12,columnspan=6)
PPdiameter=['15 nm','20 nm','25 nm','30 nm','35 nm','User Define']
choicePPVar=tk.StringVar()
choicePPVar.set(PPdiameter[0])
PP=ttk.Combobox(root,textvariable=choicePPVar,values=PPdiameter).grid(row=13,column=0)
PPEntry=tk.Entry(root)
PPEntry.grid(row=13,column=1,sticky=W)
UnitDiameter=tk.Label(root,text="nm").grid(row=13,column=2,sticky=W)


labdensity2=tk.Label(root,text="Density").grid(row=14)
density2=['1.78 g/cm\u00B3','User Define']
choiceden2Var=tk.StringVar()
choiceden2Var.set(density2[0])
Densitybox=ttk.Combobox(root,textvariable=choiceden2Var,values=density2).grid(row=14,column=0)
Density2Entry=tk.Entry(root).grid(row=14,column=1,sticky = W)
UnitDiameter=tk.Label(root,text="g/cm\u00B3").grid(row=14,column=2,sticky=W)

def calculation2():
     global dve1
     global dve2
     global N
     global kundsen_Dp
     global kundsen_Dve1
     global kundsen_Dve2

     

     
     if(choicePPVar.get())==PPdiameter[0]:
          dpp=15*pow(10,-7)
     if(choicePPVar.get())==PPdiameter[1]:
          dpp=20*pow(10,-7)
     if(choicePPVar.get())==PPdiameter[2]:
          dpp=25*pow(10,-7)
     if(choicePPVar.get())==PPdiameter[3]:
          dpp=30*pow(10,-7)
     if(choicePPVar.get())==PPdiameter[4]:
          dpp=35*pow(10,-7)
     if(choicePPVar.get())==PPdiameter[5]:
          dpp=float(PPEntry.get())*pow(10,-7)

     if(choiceden2Var.get())==density2[0]:
          PriDiameter = 1.78
     if(choiceden2Var.get())==density2[1]:
          PriDiameter = float(Density2Entry.get())
     
     
     mpp=PriDiameter*pow(dpp,3)*math.pi/6
     N=mass/mpp
     temp=6*mass/math.pi/PriDiameter
     dve1=pow(temp,1/3)*pow(10,7)
     
     dve2=dpp*pow(N,1/3)*pow(10,7)
     
     size1=size*pow(10,7)
     kundsen_Dp=2*lamda/size1
     kundsen_Dve1=2*lamda/dve1
     kundsen_Dve2=2*lamda/dve2
     print('mpp:',mpp,'N:',N,'dve1',dve1,'dve2',dve2,'mass',mass,'Kundp',kundsen_Dp,'KunDve1',kundsen_Dve1,'KunDve2',kundsen_Dve2)

def show_regine():
     if(kundsen_Dp < 0.1):
          dp_regine= 'Continuum regine'
     if(kundsen_Dp >= 0.1 and kundsen_Dp <= 10):
          dp_regine = 'transitional regine'
     if(kundsen_Dp > 10):
          dp_regine = 'free-molecular regine'

     if(kundsen_Dve1 < 0.1):
          dve1_regine= 'Continuum regine'
     if(kundsen_Dve1 >= 0.1 and kundsen_Dve1 <= 10):
          dve1_regine = 'transitional regine'
     if(kundsen_Dve1 > 10):
          dve1_regine = 'free-molecular regine'

     if(kundsen_Dve2 < 0.1):
          dve2_regine= 'Continuum regine'
     if(kundsen_Dve2 >= 0.1 and kundsen_Dve2 <= 10):
          dve2_regine = 'transitional regine'
     if(kundsen_Dve2 > 10):
          dve2_regine = 'free-molecular regine'
          
     print('Dp:',dp_regine,'Dve1',dve1_regine,'Dve2:',dve2_regine,'dve1 from function:(6*m/pi/pho)^(1/3),dve2 from function: dpp*N^(1/3)')
     

button=tk.Button(root,text="Show the regine",command=show_regine).grid(row=15,column=1,sticky = "nsew")
button=tk.Button(root,text="Calculate",command=calculation2).grid(row=15,column=0,sticky = "nsew")
#---------------------------------------------------------------------------------------
#Subroutine3
Instructsr4=tk.Label(root, text="Step4:Please choose default Input or user define").grid(row=16,column=0,columnspan=6)
Alphachoice=['\u03B1: 1.142,\u03B2: 0.588,\u03B3: 0.999 - Solid','\u03B1: 1.207,\u03B2: 0.440,\u03B3: 0.596 - oil',' Input \u03B1,\u03B2,\u03B3']
choiceAlphaVar=tk.StringVar()
choiceAlphaVar.set(Alphachoice[0])
AlphaBox=ttk.Combobox(root,textvariable=choiceAlphaVar,values=Alphachoice,width=24).grid(row=17,column=0,rowspan=3)
AlphaEntry=tk.Entry(root)
AlphaEntry.grid(row=17,column=1,sticky=W)
labAlpha=tk.Label(root,text="\u03B1").grid(row=17,column=2,sticky=W)

BetaEntry=tk.Entry(root)
BetaEntry.grid(row=18,column=1,sticky=W)
labBeta=tk.Label(root,text="\u03B2").grid(row=18,column=2,sticky=W)

GammaEntry=tk.Entry(root)
GammaEntry.grid(row=19,column=1,sticky=W)
labDelta=tk.Label(root,text="\u03B3").grid(row=19,column=2,sticky=W)

def Calculation_Subroutin3():
     global Cc_Dp
     global Cc_Dve1
     global Cc_Dve2
     #Detect alpha,beta,gamma
     if (choiceAlphaVar.get())==Alphachoice[0]:
          alpha = 1.142
          beta = 0.558
          gamma = 0.999
     if (choiceAlphaVar.get())==Alphachoice[1]:
          alpha = 1.207
          beta = 0.440
          gamma = 0.596
     if(choiceAirVar.get())==Airchoice[2]:
          alpha=float(AlphaEntry.get())
          beta=float(BetaEntry.get())
          gamma=float(GammaEntry.get())
          
     
     
     temp_Dp=alpha+beta*math.exp(-gamma/kundsen_Dp)
     temp_Dve1=alpha+beta*math.exp(-gamma/kundsen_Dve1)
     temp_Dve2=alpha+beta*math.exp(-gamma/kundsen_Dve2)
     
     Cc_Dp=1+kundsen_Dp*temp_Dp
     Cc_Dve1=1+kundsen_Dve1*temp_Dve1
     Cc_Dve2=1+kundsen_Dve2*temp_Dve2
     print('Cc_Dp',Cc_Dp,'Cc_Dve1',Cc_Dve1,'Cc_Dve2',Cc_Dve2)


     
def cal_Factor():
     chi_dve1 = size/Cc_Dp*Cc_Dve1/dve1
     chi_dve2 = size/Cc_Dp*Cc_Dve2/dve2

     if(N<60):
          chi1=pow(N,0.11)
     if(N>=60):
          chi1=0.6*pow(N,0.24)

      
     
     chi2=pow(0.802*(N-1)+1,1/2)/pow(N,1/3)
     
     print('\u03C7(dve1):',chi_dve1,'\u03C7(dve2):',chi_dve2,'\u03C7 1:',chi1,'\u03C7 2',chi2)
     
button=tk.Button(root,text="Calculate Cunningham Slip Correction Factor",command=Calculation_Subroutin3).grid(row=20,column=0,sticky = "nsew")
button=tk.Button(root,text="Calculate Dynamic Shape",command=cal_Factor).grid(row=20,column=1,sticky = "nsew")

mass_s=[]
Dp_s=[]
mass_logy=[]
size_logx=[]
def save():
     global mass_s
     global Dp_s
     global mass_logy
     global size_logx
     
     mass_s.append(mass)
     Dp_s.append(size)
     mass_logy.append(math.log(mass,2))
     size_logx.append(math.log(size,2))


     for x in range(len(mass_s)):
          print(mass_logy[x],size_logx[x],'\n')

def calculate_Df():
     global mass_s
     global Dp_s
     global mass_logy
     global size_logx
     
     Df = 0
     if (len(mass_s) == 1):
          Df=2.2
     if (len(mass_s) == 2):
          x = mass_s[0]/mass_s[1]
          y = Dp_s[0]/Dp_s[1]
          Df=math.log(x,y)

     if (len(mass_s) >= 3):
          average_y= statistics.mean(mass_logy)
          average_x= statistics.mean(size_logx)
          sum_temp1 = 0
          sum_temp2 = 0
          sum_temp3 = 0
          
          

          
          for i in range(len(mass_s)):
               sum_temp1 += (mass_logy[i]-average_y)*(size_logx[i]-average_x)
               sum_temp2 += pow(size_logx[i]-average_x,2)
               sum_temp3 += pow(mass_logy[i]-average_y,2)

               


          print(sum_temp1, sum_temp2, sum_temp3)

          slope=sum_temp1/sum_temp2
          Regress_SS = pow(sum_temp1,2)/sum_temp2
          Total_SS = sum_temp3
          Rsqure = Regress_SS/Total_SS
          Df = slope
          if Regress_SS < 0.7:
               print('The adjusted R² of our model is: ',Total_SS,'with the R²: ',Regress_SS,'which indicates the linear regression explains',Total_SS*100,'% of the variance in the data, which',100-Total_SS*100,'% unexplained variable.')
               
            
                   
                    
     print(Df)
     
def Cleanstore(): #for calculation multi
     global mass_s
     global Dp_s
     global mass_logy
     global size_logx
     
     if (len(mass_s) == 0):
          tk.messagebox.showinfo("Warning","There are no element in the store")
     else:
          mass_s=mass_s[:-1]
          Dp_s=Dp_s[:-1]
          mass_logy=mass_logy[:-1]
          size_logx=size_logx[:-1]
          return mass_s,Dp_s,mass_logy,size_logx
          
          

          
button=tk.Button(root,text="save the current mass and dp",command=save).grid(row=11,column=1,sticky = "nsew")
button=tk.Button(root,text="calculate Df",command=calculate_Df).grid(row=11,column=2,sticky = "nsew")
button=tk.Button(root,text="Clean last input",command=Cleanstore).grid(row=11,column=3,sticky = "nsew")




root.mainloop()
