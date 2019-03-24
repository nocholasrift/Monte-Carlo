import math as m
import matplotlib.pyplot as mpl

#j is a variable that allows rng to never return the same number when rng is called
j = 0
def rng(seed):
	global j
	i,x,a,c,K = 0,seed,7893,3517,2**14
	while(i < j):
		x = (x*a + c) % K
		i+=1
	j+=1
	return x/K

#random variable generator that returns time waited to get an answer if there was one.
def rvg(U):
	return -12*m.log(1-U)

def call_process():
	i,w,BUSY, UNAVAILABLE=0,7,3,25
	for i in range(4):
		num = rng(1000)
		#line is busy
		if num < .2:
			w += BUSY
		elif num < .5:
			w += UNAVAILABLE
		else:
			U = rng(1000)
			secs = rvg(U)
			if secs < 25:
				w += secs
				break
			else:
				w += 25
	return w

def main():
	n,NUM_RUNS,index,tot = 0,1000,0,0
	w_space = []
	#plot_domain = [i for i in range(1000)]
	maximum = -1
	minimum = 107
	for n in range(NUM_RUNS):
		w_space.append(call_process())
		tot += w_space[n]
	w_space.sort()
	median = NUM_RUNS//2
	first_quart = median//2
	third_quart = (NUM_RUNS)//4 + median
	mean = tot/NUM_RUNS
			
	print("MEAN IS:",mean)
	print("MEDIAN IS:",w_space[median])
	print("FIRST QUARTILE IS:",w_space[first_quart])
	print("THIRD QUARTILE IS:",w_space[third_quart])
	print("MAX IS:",w_space[-1])
	print("MIN IS: ",w_space[0])
	print("P(W <= 15):",len([i for i in w_space if i <= 15])/1000)
	print("P(W <= 20):",len([i for i in w_space if i <= 20])/1000)
	print("P(W <= 30):",len([i for i in w_space if i <= 30])/1000)
	print("P(W > 40): ",len([i for i in w_space if i > 40])/1000)
	print("P(W > 107):",len([i for i in w_space if i > 107])/1000)
	print("P(W > 87): ",len([i for i in w_space if i > 87])/1000)
	print("P(W > 63.5):",len([i for i in w_space if i > 63.5])/1000)
	"""mpl.scatter(plot_domain,w_space, alpha = .5)
				mpl.show()"""
main()

