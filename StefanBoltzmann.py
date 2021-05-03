from pylab import *
from scipy.optimize import curve_fit
from numpy import arange

subtracted1820 = np.std([-0.099, -0.056])
Rref = 0.47

trials = [
{
	tuple([2.0, 1.21])  : 0.324,
	tuple([2.2, 1.27])  : 0.658,
	tuple([2.5, 1.33])  : 0.966,
	tuple([3.0, 1.44])  : 1.401,
	tuple([3.7, 1.58])  : 2.179,
	tuple([4.1, 1.67])  : 2.726,
	tuple([5.0, 1.84])  : 3.984,
	tuple([6.0, 2.01])  : 5.614,
	tuple([8.1, 2.35])  : 9.811,
	tuple([10.0, 2.63]) : 14.144
	},

{
	tuple([2.0, 1.20])  : 1.655,
	tuple([2.2, 1.24])  : 1.500,
	tuple([2.5, 1.33])  : 1.563,
	tuple([3.0, 1.43])  : 1.867,
	tuple([3.7, 1.58])  : 2.550,
	tuple([4.1, 1.67])  : 3.110,
	tuple([5.0, 1.84])  : 4.513,
	tuple([6.0, 2.02])  : 6.230,
	tuple([8.1, 2.36])  : 10.197,
	tuple([10.0, 2.63]) : 14.760
	},

{
	tuple([2.0, 1.19])  : 1.445,
	tuple([2.2, 1.24])  : 1.352,
	tuple([2.5, 1.33])  : 1.495,
	tuple([3.0, 1.43])  : 1.049,
	tuple([3.7, 1.58])  : 2.594,
	tuple([4.1, 1.66])  : 3.154,
	tuple([5.0, 1.84])  : 4.526,
	tuple([6.0, 2.01])  : 6.330,
	tuple([8.1, 2.35])  : 10.552,
	tuple([10.0, 2.63]) : 15.167
	},

{
	tuple([2.0, 1.21])  : 1.263,
	tuple([2.2, 1.25])  : 1.273,
	tuple([2.5, 1.32])  : 1.425,
	tuple([3.0, 1.43])  : 1.833,
	tuple([3.7, 1.58])  : 2.616,
	tuple([4.1, 1.67])  : 3.183,
	tuple([5.0, 1.84])  : 4.570,
	tuple([6.0, 2.02])  : 6.336,
	tuple([8.1, 2.36])  : 10.613,
	tuple([10.0, 2.64]) : 15.210
	}
]



def objective(t, c, n):
	return c * t ** n


i = 1
xs = np.arange(800,1800,100)
for trial in trials:

	alpha = 4.5 * 10**(-3)
	R = []
	Ts = []
	Tref = 293
	Rads = list(trial.values())
	for key in list(trial.keys()):
		R.append(float(key[0] / key[1]))
	for r in R:
		T = (r - Rref) / (alpha * Rref) + Tref
		Ts.append(T)
	Label = "Trial " + str(i)
	err = np.sqrt(np.std(R)**2 +  subtracted1820**2 + 0.2682**2)
	#errorbar(Ts, Rads,  yerr=err, label=Label)
	popt, _ = curve_fit(objective, Ts, Rads)
	Rt = []
	c, n = popt
	for x in xs:
		Rt.append(c * x**n)
	loglog(xs, Rt, label=Label)
	print("Trial " + str(i) +":\nc: " + str(c) + "\nnn: " + str(n) + "\n\n")
	i+=1

legend()
xlabel("Filament Temperature (K)")
ylabel("Radiation Level (mV)")
title("Radiation Level with Temperature")
show()
print("Std:", str(np.std([4.0179, 3.576766, 3.774685, 3.7184475])))
