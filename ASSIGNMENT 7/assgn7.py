
from sympy import *                                         
import pylab as py
import numpy as np
import scipy.signal as sp

# defining a function to convert sympy function into a scipy version	 
def sympy_to_LTI(Y):
	n,d=fraction(simplify(Y))
	num,den = (np.array(Poly(n,s).all_coeffs(),dtype=float),np.array(Poly(d,s).all_coeffs(),dtype=float))
	H = sp.lti(num,den)
	return H

#  Defifning High Pass Filter and solving matrices to get output Vo4ltage
def highpass(R1,R3,C1,C2,G,Vi):                     
     
     A = Matrix([[0,0,1,-1/G],                              
                 [0,G,-G,-1],
                 [s*C2*R3/(1+s*C2*R3),-1,0,0],
                 [(s*C2+s*C1+1/R1),-s*C2,0,-1/R1]])
     b = Matrix([0,0,0,-s*C1*Vi])
     V = A.inv()*b
     return (A,b,V)
     

#  Defifning Low Pass Filter and solving matrices to get output Vo4ltage
def lowpass(R1,R2,C1,C2,G,Vi):
    
    A=Matrix([[0,0,1,-1/G],                                 
              [-1/(1+s*R2*C2),1,0,0],
              [0,-G,G,1], 
              [-1/R1-1/R2-s*C1,1/R2,0,s*C1]])
    b=Matrix([0,0,0,-Vi/R1])                                 
    V = A.inv()*b                                         
    return (A,b,V)

s=symbols('s')                                              

# Question_1
# Finding the Tansfer Function of low pass filter
A1,b1,V1 = lowpass(10000,10000,1e-9,1e-9,1.586,1)          
V = V1[3]
H1 = sympy_to_LTI(V)                                 
t  = np.linspace(0,0.01,50001)                              
Vo4 = sp.step(H1,T=t)                  

py.plot(Vo4[0],Vo4[1],'-r',label=r'$V_{o}$')
py.xlabel(r't$\rightarrow$')
py.ylabel(r'$V_{o}\rightarrow$')
py.legend(loc ='upper right')
py.grid()
py.show()

# Question_2 

Vi1 = np.multiply((np.sin(2000*np.pi*t)+np.cos(2000000*np.pi*t)),np.heaviside(t,0.5))                       # Sinusoidally oscillating input to the Low pass filter
Vo2 = sp.lsim(H1,Vi1,t)                                                           # Convolution of the input with the Impulse Response
py.plot(Vo2[0],Vi1,label=r'$V_{in}$')
py.plot(Vo2[0],Vo2[1],'-r',label=r'$V_{o}$')
py.xlabel(r't$\rightarrow$')
py.ylabel(r'$V_{o}\rightarrow$')
py.legend(loc ='upper right')
py.grid()
py.show()


# Question_3

A2,b2,V2 = highpass(10000,10000,1e-9,1e-9,1.586,1)                                       # Finding the Tansfer Function of high pass filter 
Vo3 = V2[3]
H = sympy_to_LTI(Vo3)
w  = py.logspace(0,8,801)                                                                # Range of Frequencies for the function to be plotted
ss = 1j*w
hf = lambdify(s,Vo3,'numpy')                                                             # converting the Sympy variable into python function
v  = hf(ss)

py.loglog(w,abs(v),lw=2)
py.xlabel(r'$w\rightarrow$')
py.ylabel(r'$|H(jw)|\rightarrow$')
py.grid()
py.show()

# Question_4

t = np.linspace(0,10,1000)
Vi = np.multiply(np.multiply(np.exp(-0.5*t),np.sin(2*np.pi*t)),np.heaviside(t,0.5))
Vo4 = sp.lsim(H,Vi,T=t)
py.plot(Vo4[0],Vi,label=r'$V_{in}$')
py.plot(Vo4[0],Vo4[1],'-r',label=r'$V_{o}$')
py.xlabel(r't$\rightarrow$')
py.ylabel(r'$V_{o}\rightarrow$')
py.legend(loc ='upper right')
py.grid()
py.show()

t = np.linspace(0,0.0001,10000)
Vi = np.multiply(np.multiply(np.exp(-0.5*t),np.sin(2*np.pi*200000*t)),np.heaviside(t,0.5))
Vo5 = sp.lsim(H,Vi,T=t)
py.plot(Vo5[0],Vi,label=r'$V_{in}$')
py.plot(Vo5[0],Vo5[1],'-r',label=r'$V_{o}$')
py.xlabel(r't$\rightarrow$')
py.ylabel(r'$V_{o}\rightarrow$')
py.legend(loc ='upper right')
py.grid()
py.show()


# Question_5

t5  = np.linspace(0,0.001,50001)                                                           # Time steps for plotting the input and the output                                                         
# Convolution of Unit step with impulse response of high pass filter
Vo6 = sp.step(H,T=t5)
py.plot(Vo6[0],Vo6[1],'-r',label=r'$V_{o}$')
py.xlabel(r't$\rightarrow$')
py.ylabel(r'$V_{o}\rightarrow$')
py.legend(loc ='upper right')
py.grid()
py.show()














