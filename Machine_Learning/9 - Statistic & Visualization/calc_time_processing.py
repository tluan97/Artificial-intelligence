# calc time processing

import time

tic = time.process_time()
for i in range(0,10000000):
    x = 1
toc = time.process_time()
print ("\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")
