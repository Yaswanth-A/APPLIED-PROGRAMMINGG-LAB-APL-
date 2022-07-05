"""
        EE2703 Applied Programming Lab - 2022
        Assignment 3
        Name : Allu Yaswanth
        Roll Number : EE20B007
        Date : 18th Feb 2022
"""

import numpy as np
from pylab import *
import scipy.special as sp
from scipy.linalg import lstsq

#Checking for fitting.dat file
try:
	data = np.loadtxt("fitting.dat")       
except IOError:
    print('fitting.dat file not found')
    exit()

#creating the function g
def g(t,A,B):
    return A*sp.jv(2,t) + B*t

#function to check whether both g and matrix give same output
def equal_or_not(Q,fk):
	count = 0
	for i in range(N):
		if Q[i] == fk[i]:
			count += 1

	if(count == 101):
		print("The two vectors are equal.")				#print as equal.
	else:									#else print as not equal.
		print("The two vectors are not equal.")

# function to modify thevalues of epsilon
def UpdateEpsilonValues(A,B,mean_sq_err):
    for i in range(len(A)):
        for j in range((len(B))):
            mean_sq_err[i,j] = np.mean(np.square(fk - g(t,A[i],B[j])))


#Defining all the varaiables required for us
sigma=np.logspace(-1,-3,9) #definig sigma
N,k = data.shape # N= no. of rows , k = no. off columns
M = np.zeros((N,2))
Q = np.zeros((N,1))
t = data[:,0]

for i in range(N):
    M[i,0] = sp.jv(2,data[i,0])
    M[i,1] = data[i,0] #Assigning values to M matrix
    Q[i] = M[i,0]*1.05 + M[i,1]*(-0.105) #Redefining Q
fk = g(t,1.05,-0.105)
equal_or_not(Q,fk) #Checking whether both are equal

A = linspace(0,2,20)
B = linspace(-0.2,0,20)

mean_sq_err = np.zeros((20,20))

#Plot -1
for i in range(k-1):
    plot(data[:,0],data[:,i+1],label = '$\sigma$' +"="+ str(np.around(sigma[i],3)))
xlabel(r'$t$',size=20)
ylabel(r'$f(t)+n$',size=20)
title(r'Q4:Plot of the data to be fitted')
grid(True)
legend()

plot(t,g(t,1.05,-0.105),label = r"True value")
legend()
show()

#Plot-2
errorbar(t[::5],data[::5,1],sigma[1],fmt='ro',label = r"Error bar")
xlabel(r"$t$",size=20)
title(r"Q5:Data points for $\sigma$ = 0.1 along with exact function")
legend()
plot(t,g(t,1.05,-0.105),label = r"True value")
legend()
show()

#modifing thevalues of epsilon
UpdateEpsilonValues(A,B,mean_sq_err)

cp = contour(A,B,mean_sq_err,20)

#plot-3
plot(1.05,-0.105,"ro")
annotate(r"$Exact\ location$",xy=(1.05,-0.105))
clabel(cp,inline=True)
xlabel(r"$A$",size=20)
ylabel(r"$B$",size=20)
title(r"Q8:Countour plot for $\epsilon_{ij}$")
show()       


pred=[]
Aerr=[]
Berr=[]
y_true = g(t,1.05,-0.105)
for i in range(k-1):
    p,resid,rank,sig=lstsq(M,data[:,i+1])
    a_temp = np.square(p[0]-1.05)
    b_temp = np.square(p[1]+0.105)   
    Aerr.append(a_temp)
    Berr.append(b_temp)

#plot-4
plot(sigma,Aerr,"ro",linestyle="--", linewidth = 1,label=r"$Aerr$")
legend()
plot(sigma,Berr,"go",linestyle="--",linewidth = 1,label=r"Berr")
legend()
grid(True)
xlabel(r"Noise standard deviation")
ylabel(r"$MS Error$",size=20)
title(r"$Q10:Variation\ of\  error\  with\  noise$")
show()

#plot-5
loglog(sigma,Aerr,"ro")
errorbar(sigma,Aerr,np.std(Aerr),fmt="ro",label=r"$Aerr$")
legend()
loglog(sigma,Berr,"go")
errorbar(sigma,Berr,np.std(Berr),fmt="go",label=r"$Berr$")
legend()
grid(True)
ylabel(r"$MS Error$",size=20)
title(r"$Q10:Variation\ of\ error\ with\ noise$")
xlabel(r"$\sigma_{n}$",size=20)
show()

