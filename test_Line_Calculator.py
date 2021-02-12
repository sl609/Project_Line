import pytest

@pytest.mark.parametrize("xy_tuples,x_input",[([(5,10),(15,5)],10),([(-2,7),(3,-5)],0),([(1,0),(0,1)],10)])


def test_Line_Calculator(xy_tuples,x_input):
	from Line_Calculator import Line_Calculator
	(x1,y1),(x2,y2) = xy_tuples[0],xy_tuples[1]
	calculated_y = Line_Calculator([(x1,y1),(x2,y2)],x_input);
	calculated_y1 = Line_Calculator([(x_input,calculated_y),(x2,y2)],x1);
	calculated_y2 = Line_Calculator([(x1,y1),(x_input,calculated_y)],x2);
	
	assert calculated_y1 == y1
	assert calculated_y2 == y2