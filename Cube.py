import math
import numpy as np

face1 = np.array([5.909, 5.564, 5.691, 5.7])
face2 = np.array([17.421, 17.348, 18.310, 17.709])
face3 = np.array([18.220, 18.128, 18.067, 17.983])
face4 = np.array([0.554, 0.534, 0.539, 0.528])

face1avg = np.average(face1)
face2avg = np.average(face2)
face3avg = np.average(face3)
face4avg = np.average(face4)

print("Face 1 Average mV: " + str(face1avg))
print("Face 2 Average mV: " + str(face2avg))
print("Face 3 Average mV: " + str(face3avg))
print("Face 4 Average mV: " + str(face4avg))

