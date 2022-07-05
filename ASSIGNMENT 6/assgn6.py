'''
Name : Allu Yaswanth
Roll No. : EE20B007
APL assignment 6
Date : 27 March 2022

'''
# Importing the required modules.
import pylab as pl
import scipy.signal as sp
import numpy as np

# Time response of spring with decay 0.5
p1_num = pl.poly1d([1,0.5]) #Defining numerator polynomial
p1_den = pl.polymul([1,1,2.5],[1,0,2.25]) #Defining denominator polynomial
S1 = sp.lti(p1_num,p1_den) 
t1,x1 = sp.impulse(S1,None,pl.linspace(0,50,500)) 

# The plot x(t) vs t for decay 0.5
pl.figure(0)
pl.plot(t1,x1)
pl.title("X(t) for decay 0.5")
pl.xlabel(r'$t\rightarrow$')
pl.ylabel(r'$x(t)\rightarrow$')
pl.grid(True)
pl.show()

# The plot x(t) vs t for decay 0.05
p2_num = pl.poly1d([1,0.05]) #Defining numerator polynomial
p2_den = pl.polymul([1,0.1,2.2525],[1,0,2.25]) #Defining denominator polynomial
S2 = sp.lti(p1_num,p2_den)
t2,x2 = sp.impulse(S2,None,pl.linspace(0,50,500))

# The plot x(t) vs t for decay 0.05
pl.figure(1)
pl.plot(t2,x2)
pl.title("X(t) for decay 0.05")
pl.xlabel(r'$t\rightarrow$')
pl.ylabel(r'$x(t)\rightarrow$')
pl.grid(True)
pl.show()

# Transfer function and responces by varying frequencies from 1.4 to 1.6
H = sp.lti([1],[1,0,2.25])

for OMEGA in np.arange(1.4, 1.6, 0.05):
    t3 = np.linspace(0, 50, 500)
    f = np.cos(OMEGA*t3)*np.exp(-0.05*t3)
    t3,x3,svec = sp.lsim(H,f,t3)
    
# The plot of x(t) for various frequencies vs time.
    pl.figure(2)
    pl.plot(t3,x3,label='w = ' + str(OMEGA))
    pl.title("x(t) for different frequencies ranged from 1.4 to 1.6")
    pl.xlabel(r'$t\rightarrow$')
    pl.ylabel(r'$x(t)\rightarrow$')
    pl.legend(loc = 'upper left')
    pl.grid(True)
pl.show()   

# The python code snippet for Q.4
t4 = pl.linspace(0,20,500)
X4 = sp.lti([1,0,2],[1,0,3,0])
Y4 = sp.lti([2],[1,0,3,0])	
t4,x4 = sp.impulse(X4,None,t4)
t4,y4 = sp.impulse(Y4,None,t4)

pl.figure(3)
pl.plot(t4,x4,label='x(t)')
pl.plot(t4,y4,label='y(t)')
pl.title("x(t) and y(t)")
pl.xlabel(r'$t\rightarrow$')
pl.ylabel(r'$functions\rightarrow$')
pl.legend(loc = 'upper right')
pl.grid(True)
pl.show()

#To find the Transfer Equation of two port network and plotting bode plots of magnitude and phase.
R = 100
L = 1e-6
C = 1e-6

OMEGA = 1/np.sqrt(L*C) 
Qf = 1/R * np.sqrt(L/C)
ZETA = 1/(2*Qf)

num = pl.poly1d([OMEGA**2])
den = pl.poly1d([1,2*OMEGA*ZETA,OMEGA**2])

H = sp.lti(num,den)

w,S,phi=H.bode()

# The magnitude bode plot
pl.figure(4)
pl.semilogx(w,S)
pl.title("Magnitude Bode plot")
pl.xlabel(r'$\omega\rightarrow$')
pl.ylabel(r'$20\log|H(j\omega)|\rightarrow$')
pl.grid(True)
pl.show()

# The phase bode plot
pl.figure(5)
pl.semilogx(w,phi)
pl.title("Phase Bode plot")
pl.xlabel(r'$\omega\rightarrow$')
pl.ylabel(r'$\angle H(j\omega)\rightarrow$')
pl.grid(True)
pl.show()

#To Find the output voltage from transfer function and input voltage for short term and long term time intervals.The plots of output voltages
t6 = pl.arange(0,25e-3,1e-7)
vi = np.cos(1e3*t6) - np.cos(1e6*t6)
t6,vo,svec = sp.lsim(H,vi,t6)

# The plot of Vo(t) vs t for large time interval.
pl.figure(6)
pl.plot(t6,vo)
pl.title("The Output Voltage for large time interval")
pl.xlabel(r'$t\rightarrow$')
pl.ylabel(r'$V_o(t)\rightarrow$')
pl.grid(True)
pl.show()

# The plot of Vo(t) vs t for small time interval.
pl.figure(7)
pl.plot(t6[0:300],vo[0:300])
pl.title("The Output Voltage for small time interval")
pl.xlabel(r'$t\rightarrow$')
pl.ylabel(r'$V_o(t)\rightarrow$')
pl.grid(True)
pl.show()