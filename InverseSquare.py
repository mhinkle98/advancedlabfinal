from pylab import *
from scipy.optimize import curve_fit
from numpy import arange

trial1 = {
	4  : 21.673,
	5  : 14.174,
	6  : 10.165,
	8  : 6.203,
	13 : 2.688,
	18 : 1.473,
	28 : 0.594,
	38 : 0.319,
	58 : 0.074,
	80 : 0.010
	}

trial2 = {
	4  : 20.819,
	5  : 14.585,
	6  : 10.606,
	8  : 6.624,
	13 : 2.733,
	18 : 1.440,
	28 : 0.559,
	38 : 0.259,
	58 : 0.034,
	80 : -0.043
	}

trial3 = {
	4  : 21.047,
	5  : 14.673,
	6  : 11.008,
	8  : 6.595,
	13 : 2.625,
	18 : 1.382,
	28 : 0.495,
	38 : 0.175,
	58 : -0.025,
	80 : -0.094
	}

trial4 = {
	4  : 21.426,
	5  : 15.105,
	6  : 10.839,
	8  : 6.713,
	13 : 2.731,
	18 : 1.375,
	28 : 0.483,
	38 : 0.174,
	58 : -0.051,
	80 : -0.126
	}

def objective1(x, n):
	return 50 * 21.673 * x ** n
def objective2(x,n):
	return 50 * 20.819 * x ** n
def objective3(x, n):
	return 50 * 21.047 * x ** n
def objective4(x,n):
	return 50 * 21.426 * x ** n


subtracted49 = [0.013,-0.25]

popt, _ = curve_fit(objective1, list(trial1.keys()), list(trial1.values()))
popt2, _ = curve_fit(objective2, list(trial2.keys()), list(trial2.values()))
popt3, _ = curve_fit(objective3, list(trial3.keys()), list(trial3.values()))
popt4, _ = curve_fit(objective4, list(trial4.keys()), list(trial4.values()))
n1 = popt
n2 = popt2
n3 = popt3
n4 = popt4

print('From Trial 1: R(x) = 21.673x^%.5f' % n1)
print('From Trial 2: R(x) = 20.819x^%.5f' % n2)
print('From Trial 3: R(x) = 21.047x^%.5f' % n3)
print('From Trial 4: R(x) = 21.426x^%.5f' % n4)
print('Error', str(np.std([-2.74571,-2.72397,-2.72322,-2.72411])))
Rx1 = []
Rx2 = []
Rx3 = []
Rx4 = []

xs = arange(4,100,1)

for x in xs:
	Rx1.append(21.673 * x ** n1)
	Rx2.append(20.819 * x ** n2)
	Rx3.append(21.047 * x ** n3)
	Rx4.append(21.426 * x ** n4)

def calcerror(values):
	return np.sqrt((np.std(values))**2 + 0.5**2 + (np.std(subtracted49))**2)

#errorbar(list(trial1.keys()), list(trial1.values()), yerr=calcerror(list(trial1.values())), label="Trial 1")
#errorbar(list(trial2.keys()), list(trial2.values()), yerr=calcerror(list(trial2.values())), label="Trial 2")
#errorbar(list(trial3.keys()), list(trial3.values()), yerr=calcerror(list(trial3.values())), label="Trial 3")
#errorbar(list(trial4.keys()), list(trial4.values()), yerr=calcerror(list(trial4.values())), label="Trial 4")
#title("Radiation vs Distance")
#xlabel("Distance (cm)")
#ylabel("Radiation (mV)")
#legend()
#show()

loglog(xs, Rx1, label="Trial 1 Fit")
loglog(xs, Rx2, label="Trial 2 Fit")
loglog(xs, Rx3, label="Trial 3 Fit")
loglog(xs, Rx4, label="Trial 4 Fit")
xlabel("Distance (cm) [Log-Scale]")
ylabel("Radiance Fit (W)")
title("Log-log Fit of Radiance with Distance")
legend()
show()

#loglog(list(trial1.keys()), list(trial1.values()), label="Trial 1")
#loglog(list(trial2.keys()), list(trial2.values()), label="Trial 2")
#loglog(list(trial3.keys()), list(trial3.values()), label="Trial 3")
#loglog(list(trial4.keys()), list(trial4.values()), label="Trial 4")
#legend()
#show()
def calcerrorfit(values):
	return np.sqrt((np.std(values))**2)
errorbar(xs, Rx1, yerr=calcerrorfit(Rx1),label="Trial 1 Fit")
errorbar(xs, Rx2, yerr=calcerrorfit(Rx2),label="Trial 2 Fit")
errorbar(xs, Rx3, yerr=calcerrorfit(Rx3),label="Trial 3 Fit")
errorbar(xs, Rx4, yerr=calcerrorfit(Rx4),label="Trial 4 Fit")
xlabel("Distance (cm)")
ylabel("Radiation Fit (W)")
title("Radiation Fits with Distance")
legend()
show()

