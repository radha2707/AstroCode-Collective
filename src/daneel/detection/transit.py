import batman
import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the first planet
params1 = batman.TransitParams()
params1.t0 = 0.5                   # Time of inferior conjunction
params1.per = 3.52472              # Orbital period [days]
params1.rp = 0.139                 # Planet radius (in units of stellar radii)
params1.a = 10.21                  # Semi-major axis (in units of stellar radii)
params1.inc = 86.59                # Orbital inclination [degrees]
params1.ecc = 0.0082               # Eccentricity
params1.w = 43.8                   # Longitude of periastron [degrees]
params1.limb_dark = "quadratic"    # Limb darkening model
params1.u = [0.1281, 0.9648]       # Limb darkening coefficients

# Define parameters for the second planet (radius reduced by half)
params2 = batman.TransitParams()
params2.t0 = params1.t0            # Same time of inferior conjunction
params2.per = params1.per          # Same orbital period
params2.rp = params1.rp / 2        # Radius reduced by a factor of ½
params2.a = params1.a              # Same semi-major axis
params2.inc = params1.inc          # Same orbital inclination
params2.ecc = params1.ecc          # Same eccentricity
params2.w = params1.w              # Same longitude of periastron
params2.limb_dark = params1.limb_dark  # Same limb darkening model
params2.u = params1.u              # Same limb darkening coefficients

# Generate the transit light curve
t = np.linspace(0.35, 0.75, 2000)  # Time array
m1 = batman.TransitModel(params1, t)
m2 = batman.TransitModel(params2, t)

flux1 = m1.light_curve(params1)    # Light curve for the first planet
flux2 = m2.light_curve(params2)    # Light curve for the second planet

# Plot and save the light curve
plt.figure(figsize=(10, 6))
plt.plot(t - params1.t0, flux1, label="Planet 1 (HD 209458 b)", color="blue")
plt.plot(t - params1.t0, flux2, label="Planet 2 (Radius ½ HD 209458 b)", color="orange")
plt.xlabel("Time from central transit [days]")
plt.ylabel("Relative flux")
plt.title("Transit Light Curve: Two Planets (HD 209458 b and Reduced Radius)")
plt.legend()
plt.grid()
plt.savefig("assignment2_taskB.png")
plt.close()