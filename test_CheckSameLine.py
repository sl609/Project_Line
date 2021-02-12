import pytest

@pytest.mark.parametrize("xy_tuples",[([(5,10),(15,5),(10,7.5)]),([(-2,7),(3,-5),(0,2.2)]),([(1,0),(0,1),(10,-9)])])

def test_Check_SameLine(xy_tuples):
	from Check_SameLine import Check_SameLine
	(x1,y1),(x2,y2),(x3,y3) = xy_tuples[0],xy_tuples[1],xy_tuples[2]
	expected_True = Check_SameLine([(x1,y1),(x2,y2),(x3,y3)]);
	expected_False = Check_SameLine([(x1,y1),(x2,y2),(x3,y3-1)]);
	
	assert expected_True == True
	assert expected_False == False