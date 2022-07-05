#importing required modules
from pylab import *								
from scipy import integrate						
from numpy import transpose								
from numpy import *



#defining functions required for the code
def F(x):										
	return exp(x)								

def G(x):										
	return cos(cos(x))							
	
def u_exp(x,k):															
	return exp(x)*cos(k*x)								

def v_exp(x,k):									
	return exp(x)*sin(k*x)								

def u_cos(x,k):									
	return cos(cos(x))*cos(k*x)							
	
def v_cos(x,k):								
	return cos(cos(x))*sin(k*x)							


#Finding the coefficients of fourier series by integrating and storing them in matrix

#Fourier coeffs for exp function											
exp_coeff = zeros((51,1))									
exp_coeff[0][0] = (1/(2*pi))*(integrate.quad(F,0,2*pi))[0]					
for k in range(1,26):									
	exp_coeff[2*k-1][0] = (1/pi)*(integrate.quad(u_exp,0,2*pi,args=(k)))[0]	
	exp_coeff[2*k][0] = (1/pi)*(integrate.quad(v_exp,0,2*pi,args=(k)))[0]		

cos_coeff = zeros((51,1))					
cos_coeff[0][0] = (1/(2*pi))*(integrate.quad(G,0,2*pi))[0]		
for k in range(1,26):									
	cos_coeff[2*k-1][0] = (1/pi)*(integrate.quad(u_cos,0,2*pi,args=(k)))[0]	
	cos_coeff[2*k][0] = (1/pi)*(integrate.quad(v_cos,0,2*pi,args=(k)))[0]	


#creating the matrix A.

n = array(range(1,52))							
a=linspace(0,2*pi,401)								
a=a[:-1]									
B_e = F(a)			#B matrx for exp					
B_c = G(a)			# B matrx for coscos												
A = zeros((400,51))		#Initrializing with zeros					
A[:,0] = 1							
for k in range(1,26):								
	A[:,2*k-1] = cos(k*a)							
	A[:,2*k] = sin(k*a)							
C_exp = lstsq(A,B_e,rcond=None)[0]				
C_coscos = lstsq(A,B_c,rcond=None)[0]					
c_trans_exp = transpose(exp_coeff)							
c_trans_coscos = transpose(cos_coeff)							

#Absolute difference bewtween estimated and calculated coeffs
Absolute_diff_exp = abs(C_exp - c_trans_exp)							#absolute difference between calculated and estimated fourier coefficients of exp(x)
Absolute_diff_coscos = abs(C_coscos - c_trans_coscos)						#absolute difference between calculated and estimated fourier coefficients of cos(cosx)

#Finding largest deviation
large_dev_exp = max(Absolute_diff_exp[0])							#largest deviation in fourier coefficients of exp(x)
large_dev_coscos = max(Absolute_diff_coscos[0])						#largest deviation in fourier coefficients of cos(cos(x))

print("The largest deviation between coefficients for exp() is ",large_dev_exp)	
print("The largest deviation between coefficients for coscos() is ",large_dev_coscos)


cl_exp = dot(A,C_exp)									#Estimated exp(x) function
cl_coscos = dot(A,C_coscos)								#Estimated cos(cosx) function		

x=linspace(-2*pi,4*pi,1200)				
xt = linspace(0,2*pi,400)								
t = tile(xt,3)										


#plot of exp
figure(1)								
plt.semilogy(x,F(x),'r',label='true value')						
plt.semilogy(x,F(t),'-b',label='Periodic extension')			
plt.semilogy(xt,cl_exp,'go',label='estimated value')					
plt.title("Semilog plot of $e^{x}$ function")								
plt.xlabel(r'$x\rightarrow$',size=15)							
plt.ylabel(r'$e^x\rightarrow$',size=15)							
plt.grid(True)										
plt.legend()
plt.show()								

#plot of coscos
figure(2)										
plt.plot(x,G(x),'r',label='true value')						
plt.plot(x,G(t),'-b',label='Periodic extension')						
plt.plot(xt,cl_coscos,'go',label='estimated value')					
plt.title("plot of cos(cos(x)) function")							
plt.xlabel(r'$x\rightarrow$',size=15)						
plt.ylabel(r'$cos(cos(x))\rightarrow$',size=15)						
plt.grid(True)									
plt.legend()	
plt.show()									

#semilog plot of exp coeffs
figure(3)									
plt.semilogy(n,abs(exp_coeff),'ro',label='direct integration')				
plt.semilogy(n,abs(C_exp),'go',label='Least Squares approach')				
plt.title("Semilog Plot of coefficients for $e^{x}$")					
plt.xlabel(r'$n\rightarrow$',size=15)							
plt.ylabel('Magnitude of coefficients for $e^{x}$ ',size=15)			
plt.grid(True)									
plt.legend()									
plt.show()

#loglog plot of exp coeffs
figure(4)										
plt.loglog(n,abs(exp_coeff),'ro',label='direct integration')				
plt.loglog(n,abs(C_exp),'go',label='Least Squares approach')				
plt.title("Loglog Plot of coefficients of $e^{x}$")					
plt.xlabel(r'$n\rightarrow$',size=15)							
plt.ylabel('Magnitude of coefficients for $e^{x}$',size=15)			
plt.grid(True)										
plt.legend()										
plt.show()

#semilog plot of coscos coeffs
figure(5)										
plt.semilogy(n,abs(cos_coeff),'ro',label='direct integration')				
plt.semilogy(n,abs(C_coscos),'go',label='Least Squares approach')			
plt.title("Semilog Plot of coefficients for cos(cos(x))")				
plt.xlabel(r'$n\rightarrow$',size=15)							
plt.ylabel('Magnitude of coefficients for cos(cos(x)) ',size=15)				
plt.grid(True)									
plt.legend()									
plt.show()

#loglog plot of coscos coeffs
figure(6)										
plt.loglog(n,abs(cos_coeff),'ro',label='direct integration')			
plt.loglog(n,abs(C_coscos),'go',label='Least Squares approach')				
plt.title("Loglog Plot of coefficients of cos(cos(x))")			
plt.xlabel(r'$n\rightarrow$',size=15)						
plt.ylabel('Magnitude of coefficients for cos(cos(x))',size=15)				
plt.grid(True)									
plt.legend()										
plt.show()											