import numpy as np
def Line_Calculator(xy_tuples,x_input):
	(x1,y1),(x2,y2) = xy_tuples[0],xy_tuples[1]
	if(np.abs(x2-x1)>0):
		return np.round((y2-y1)/(x2-x1)*(x_input-x1)+y1,4)
	else:
		if(x_input == x1):
			return y1
		else:
			return None
