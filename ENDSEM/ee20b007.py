"""
APL EE2703 ENDSEM
ALLU YASWANTH
EE20B007
"""
import numpy as np
from pylab import *

#Function to determine M matrix for the 2nd question
def Matrix_M():
    M = np.identity(2 * N - 2)
    M = (1 / (2 * PI * rad)) * M
    return M

#Defining required variables

N = 100 # no of sections in each half section of antenna
len = 0.5  # quarter wavelength
C= 2.9979e8  # Speed of light
rad = 0.01  # radius of wire
Im = 1.0  # current injected into antenna
PI = np.pi # = 3.1415
mu0 = 4e-7 * PI  # permeability of free space
wave_len = len * 4.0  # Wavelength
dz = len / N  # Sample spacing
k = 2 * PI / wave_len  # wave number
f = C / wave_len  # frequency

#Question 1
z = arange(-len, len+len/N , len/N) #Points in A.P where we compurte the currents
I = np.zeros(2 * N + 1) # Initiating the I matrix with zeros
for i in range(0,N):
    I[i] = Im * sin(k * (len + z[i])) #Giving the I values as given in the problem 
for i in range(N,2*N):
    I[i] = Im * sin(k * (len - z[i]))  #Giving the I values as given in the problem 

u = [(i*dz)-0.5 for i in range(1, 2 * N)] 
u.__delitem__(N-1 ) #u gives the matrix z excluding the edge points and the middle one.

#Question 2

M = Matrix_M() #DETERMINING M MATRIX


#Question 3
#Determining Rz
Z = np.meshgrid(z,z)
Z_i = Z[0]
Z_j = Z[1]
Rz = np.sqrt((Z_i-Z_j)**2 + np.ones([2*N+1,2*N+1],dtype=complex)*(rad**2))

#Determining Ru
U = np.meshgrid(u,u)
U_i = U[0]
U_j = U[1]
Ru = np.sqrt((U_i-U_j)**2 + np.ones([2*N-2,2*N-2],dtype=complex)*(rad**2))

Rin = Rz[N]
Rin = np.delete(Rin, [0, N, 2 * N], 0)

#Computing the vectors P and PB
# P gives the Contribution due to all currents
P = np.zeros((2 * N - 2, 2 * N - 2), dtype=complex)
for i in range(2 * N - 2):
    for j in range(2 * N - 2):
        P[i][j] = (mu0 / (4.0 * PI)) * (np.exp(-1j * k * Ru[i][j])) * dz / Ru[i][j]

# Contribution of vector potential due to current IN
PB = (mu0 / (4 * PI)) * (np.exp(-1j * k * Rin)) * dz / Rin


#Question 4
# Computing Q and QB from given formula
Q = np.zeros((2 * N - 2, 2 * N - 2), dtype=complex)
for i in range(2 * N - 2):
    for j in range(2 * N - 2):
        Q[i][j] = -P[i][j] * (rad / mu0) * ((-1j * k / Ru[i][j]) - (1 / pow(Ru[i][j], 2)))


QB = -PB * (rad / mu0) * ((-1j * k / Rin) - (1 / Rin ** 2))

#Question 5
result_J = np.dot(linalg.inv(M - Q), QB) #The resultant I vector which doesn't include the edges and middle value
result_I = np.zeros(2*N+1, dtype = complex)#Defining a zero array to store the I values
#Forming the I vector for all elements by adding boundary conditions
result_I[1:N] = result_J[0:N-1]
result_I[N+1: 2*N] = result_J[N-1:2*N-1]
result_I[N] = Im  # I at z=0 is Im
#I at edges is 0

#Plotting the graph
figure()
plot(z,abs(result_I),label = "Estimated Current")
plot(z,I,label = "Assumed Current")
xlabel(r"z")
ylabel(r"I")
legend()
title("Antenna currents for N=100")
grid()
show()

#For printing out the required matrices
# print(Rz.round(2))
# print('*************************1')
# print(Ru.round(2))
# print('*************************2')
# print(Rin.round(2))
# print('*************************3')
# print((P*1e8).round(2))
# print('*************************4')
# print((PB*1e8).round(2))
# print('*************************5')
# print(Q.round(2))
# print('*************************6')
# print(QB.round(2))



