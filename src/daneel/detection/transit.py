import batman
import numpy as np
import matplotlib.pyplot as plt

# Define parameters 
params = batman.TransitParams()
params.t0 = 0.5                 
params.per = 3.52472            
params.rp = 0.139               
params.a = 10.21                
params.inc = 86.59              
params.ecc = 0.0082             
params.w = 43.8                 
params.limb_dark = "quadratic"  
params.u = [0.1281, 0.9648]     


# Generate the transit light curve
t = np.linspace(0.40, 0.60, 1000)   
m = batman.TransitModel(params, t) 
flux = m.light_curve(params)       
cen = np.argmin(flux)
print(t[cen])
t0 = t[cen]
# Plot and save the light curve
plt.figure()
plt.plot(t-t0, flux, label="HD 209458 b Transit Light Curve")
plt.xlabel("Time from central transit [days]")
plt.ylabel("Relative flux")
plt.title("Transit Light Curve for HD 209458 b")
# plt.legend()
# plt.xlim(-0.14, 0.14)
plt.savefig("assignment2_taskA.png") 

plt.close()