import math as m
import matplotlib.pyplot as mpl
def rng(seed, targ_num):
	i,x,a,c,K = 0,seed,7893,3517,2**14
	while(i < targ_num):
		x = (x*a + c) % K
		i+=1
	return x/K

#random variable generator that returns time waited to get an answer if there was one.
def rvg(U):
	return -12*m.log(1-U)

def call_process(ind):
	i,w,busy,unavailable=0,7,3,25
	while(i < 4):
		num = rng(1000,ind+i)
		#line is busy
		if num < .2:
			w += busy
			i+=1
		elif num < .5:
			#idk if unavailable is supposed to be 25s or not
			w += unavailable
			i+=1
		else:
			secs = rvg(num)
			#not sure if this should be < or just <=
			if secs < 25:
				w += secs
				break
			else:
				w += 25
				i+=1
	return w

def main():
	n,NUM_RUNS,index,tot = 0,1000,0,0
	w_space = []
	#plot_domain = [i for i in range(1000)]
	for n in range(NUM_RUNS):
		w_space.append(call_process(index))
		#add 3 to index so no repeat parameters go into rng method in call_process
		index += 3
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

	"""mpl.scatter(plot_domain,w_space, alpha = .5)
				mpl.show()"""
main()

