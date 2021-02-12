def Check_SameLine(xy_tuples):
	from Line_Calculator import Line_Calculator
	(x1,y1),(x2,y2),(x3,y3) = xy_tuples[0],xy_tuples[1],xy_tuples[2]
	calculated_y1 = Line_Calculator([(x2,y2),(x3,y3)],x1);
	calculated_y2 = Line_Calculator([(x1,y1),(x3,y3)],x2);
	calculated_y3 = Line_Calculator([(x1,y1),(x2,y2)],x3);

	if( calculated_y1==y1 and calculated_y2==y2 and calculated_y3==y3):
		return True
	else:
		return False