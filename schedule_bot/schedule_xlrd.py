import xlrd

workbook = xlrd.open_workbook('rp.xls',on_demand=True)
worksheet_by_index = workbook.sheet_by_index(0)

# Понедельник первый класс
def monday_one_one():
    cell_value1 = worksheet_by_index.cell(6,2).value
    return cell_value1

def monday_one_two():  
    cell_value2 = worksheet_by_index.cell(7,2).value
    return cell_value2

def monday_one_three():   
    cell_value3 = worksheet_by_index.cell(8,2).value
    return cell_value3

def monday_one_four():
    cell_value4 = worksheet_by_index.cell(9,2).value
    return cell_value4


# Понедельник второй класс
def monday_two_one():
    cell_value1 = worksheet_by_index.cell(6,3).value
    return cell_value1

def monday_two_two():
	cell_value2 = worksheet_by_index.cell(7,3).value
	return cell_value2

def monday_two_three():
    cell_value3 = worksheet_by_index.cell(8,3).value
    return cell_value3

def monday_two_four():
    cell_value4 = worksheet_by_index.cell(9,3).value
    return cell_value4


#Понедельник третий класс
def monday_three_one():
	cell_value1 = worksheet_by_index.cell(6,4).value
	return cell_value1

def monday_three_two():
	cell_value2 = worksheet_by_index.cell(7,4).value
	return cell_value2

def monday_three_three():
	cell_value3 = worksheet_by_index.cell(8,4).value
	return cell_value3

def monday_three_four():
	cell_value4 = worksheet_by_index.cell(9,4).value
	return cell_value4

def monday_three_five():
	cell_value5 = worksheet_by_index.cell(10,4).value
	return cell_value5


#Понедельник четвёртый класс
def monday_four_one():
	cell_value1 = worksheet_by_index.cell(6,5).value
	return cell_value1	

def monday_four_two():
	cell_value2 = worksheet_by_index.cell(7,5).value
	return cell_value2

def monday_four_three():
	cell_value3 = worksheet_by_index.cell(8,5).value
	return cell_value3

def monday_four_four():
	cell_value4 = worksheet_by_index.cell(9,5).value
	return cell_value4


#Понедельник пятый класс
def monday_five_one():
	cell_value1 = worksheet_by_index.cell(6,6).value
	return cell_value1

def monday_five_two():
	cell_value2 = worksheet_by_index.cell(7,6).value
	return cell_value2

def monday_five_three():
	cell_value3 = worksheet_by_index.cell(8,6).value
	return cell_value3

def monday_five_four():
	cell_value4 = worksheet_by_index.cell(9,6).value
	return cell_value4

def monday_five_five():
	cell_value5 = worksheet_by_index.cell(10,6).value
	return cell_value5

def monday_five_six():
	cell_value6 = worksheet_by_index.cell(11,6).value
	return cell_value6


#Понедельник шестой класс
def monday_six_one():
	cell_value1 = worksheet_by_index.cell(6,7).value
	return cell_value1

def monday_six_two():
	cell_value2 = worksheet_by_index.cell(7,7).value
	return cell_value2

def monday_six_three():
	cell_value3 = worksheet_by_index.cell(8,7).value
	return cell_value3
	
def monday_six_four():
	cell_value4 = worksheet_by_index.cell(9,7).value
	return cell_value4

def monday_six_five():
	cell_value5 = worksheet_by_index.cell(10,7).value
	return cell_value5

def monday_six_six():
	cell_value6 = worksheet_by_index.cell(11,7).value
	return cell_value6


#Понедельник седьмой класс
def monday_seven_one():
	cell_value1 = worksheet_by_index.cell(6,8).value
	return cell_value1

def monday_seven_two():
	cell_value2 = worksheet_by_index.cell(7,8).value
	return cell_value2

def monday_seven_three():
	cell_value3 = worksheet_by_index.cell(8,8).value
	return cell_value3

def monday_seven_four():
	cell_value4 = worksheet_by_index.cell(9,8).value
	return cell_value4

def monday_seven_five():
	cell_value5 = worksheet_by_index.cell(10,8).value
	return cell_value5

def monday_seven_six():
	cell_value6 = worksheet_by_index.cell(11,8).value
	return cell_value6


#Понедельник восьмой класс
def monday_eight_one():
	cell_value1 = worksheet_by_index.cell(6,9).value
	return cell_value1

def monday_eight_two():
	cell_value2 = worksheet_by_index.cell(7,9).value
	return cell_value2

def monday_eight_three():
	cell_value3 = worksheet_by_index.cell(8,9).value
	return cell_value3

def monday_eight_four():
	cell_value4 = worksheet_by_index.cell(9,9).value
	return cell_value4

def monday_eight_five():
	cell_value5 = worksheet_by_index.cell(10,9).value
	return cell_value5

def monday_eight_six():
	cell_value6 = worksheet_by_index.cell(11,9).value
	return cell_value6

def monday_eight_seven():
	cell_value7 = worksheet_by_index.cell(12,9).value
	return cell_value7


#Понедельник девятый класс
def monday_nine_one():
	cell_value1 = worksheet_by_index.cell(6,10).value
	return cell_value1

def monday_nine_two():
	cell_value2 = worksheet_by_index.cell(7,10).value
	return cell_value2

def monday_nine_three():
	cell_value3 = worksheet_by_index.cell(8,10).value
	return cell_value3

def monday_nine_four():
	cell_value4 = worksheet_by_index.cell(9,10).value
	return cell_value4

def monday_nine_five():
	cell_value5 = worksheet_by_index.cell(10,10).value
	return cell_value5

def monday_nine_six():
	cell_value6 = worksheet_by_index.cell(11,10).value
	return cell_value6


#Понедельник десятый класс
def monday_ten_one():
	cell_value1 = worksheet_by_index.cell(6,11).value
	return cell_value1

def monday_ten_two():
	cell_value2 = worksheet_by_index.cell(7,11).value
	return cell_value2

def monday_ten_three():
	cell_value3 = worksheet_by_index.cell(8,11).value
	return cell_value3

def monday_ten_four():
	cell_value4 = worksheet_by_index.cell(9,11).value
	return cell_value4

def monday_ten_five():
	cell_value5 = worksheet_by_index.cell(10,11).value
	return cell_value5

def monday_ten_six():
	cell_value6 = worksheet_by_index.cell(11,11).value
	return cell_value6


#Понедельник одинадцатый класс
def monday_eleven_one():
	cell_value1 = worksheet_by_index.cell(6,12).value
	return cell_value1

def monday_eleven_two():
	cell_value2 = worksheet_by_index.cell(7,12).value
	return cell_value2

def monday_eleven_three():
	cell_value3 = worksheet_by_index.cell(8,12).value
	return cell_value3

def monday_eleven_four():
	cell_value4 = worksheet_by_index.cell(9,12).value
	return cell_value4

def monday_eleven_five():
	cell_value5 = worksheet_by_index.cell(10,12).value
	return cell_value5

def monday_eleven_six():
	cell_value6 = worksheet_by_index.cell(11,12).value
	return cell_value6


#Вторник


#Вторник первый класс
def tuesday_one_one():
	cell_value1 = worksheet_by_index.cell(13,2).value
	return cell_value1

def tuesday_one_two():
	cell_value2 = worksheet_by_index.cell(14,2).value
	return cell_value2

def tuesday_one_three():
	cell_value3 = worksheet_by_index.cell(15,2).value
	return cell_value3

def tuesday_one_four():
	cell_value4 = worksheet_by_index.cell(16,2).value
	return cell_value4


#Вторник второй класс
def tuesday_two_one():
	cell_value1 = worksheet_by_index.cell(13,3).value
	return cell_value1

def tuesday_two_two():
	cell_value2 = worksheet_by_index.cell(14,3).value
	return cell_value2

def tuesday_two_three():
	cell_value3 = worksheet_by_index.cell(15,3).value
	return cell_value3

def tuesday_two_four():
	cell_value4 = worksheet_by_index.cell(16,3).value
	return cell_value4


#Вторник третий класс
def tuesday_three_one():
	cell_value1 = worksheet_by_index.cell(13,4).value
	return cell_value1

def tuesday_three_two():
	cell_value2 = worksheet_by_index.cell(14,4).value
	return cell_value2

def tuesday_three_three():
	cell_value3 = worksheet_by_index.cell(15,4).value
	return cell_value3

def tuesday_three_four():
	cell_value4 = worksheet_by_index.cell(16,4).value
	return cell_value4

def tuesday_three_five():
	cell_value5 = worksheet_by_index.cell(17,4).value
	return cell_value5


#Вторник четвёртый класс
def tuesday_four_one():
	cell_value1 = worksheet_by_index.cell(13,5).value
	return cell_value1

def tuesday_four_two():
	cell_value2 = worksheet_by_index.cell(14,5).value
	return cell_value2

def tuesday_four_three():
	cell_value3 = worksheet_by_index.cell(15,5).value
	return cell_value3

def tuesday_four_four():
	cell_value4 = worksheet_by_index.cell(16,5).value
	return cell_value4

def tuesday_four_five():
	cell_value5 = worksheet_by_index.cell(17,5).value
	return cell_value5


#Вторник пятый класс
def tuesday_five_one():
	cell_value1 = worksheet_by_index.cell(13,6).value
	return cell_value1

def tuesday_five_two():
	cell_value2 = worksheet_by_index.cell(14,6).value
	return cell_value2

def tuesday_five_three():
	cell_value3 = worksheet_by_index.cell(15,6).value
	return cell_value3

def tuesday_five_four():
	cell_value4 = worksheet_by_index.cell(16,6).value
	return cell_value4

def tuesday_five_five():
	cell_value5 = worksheet_by_index.cell(17,6).value
	return cell_value5

def tuesday_five_six():
	cell_value6 = worksheet_by_index.cell(18,6).value
	return cell_value6


#Вторник шестой класс
def tuesday_six_one():
	cell_value1 = worksheet_by_index.cell(13,7).value
	return cell_value1

def tuesday_six_two():
	cell_value2 = worksheet_by_index.cell(14,7).value
	return cell_value2

def tuesday_six_three():
	cell_value3 = worksheet_by_index.cell(15,7).value
	return cell_value3

def tuesday_six_four():
	cell_value4 = worksheet_by_index.cell(16,7).value
	return cell_value4

def tuesday_six_five():
	cell_value5 = worksheet_by_index.cell(17,7).value
	return cell_value5

def tuesday_six_six():
	cell_value6 = worksheet_by_index.cell(18,7).value
	return cell_value6


#Вторник седьмой класс
def tuesday_seven_one():
	cell_value1 = worksheet_by_index.cell(13,8).value
	return cell_value1

def tuesday_seven_two():
	cell_value2 = worksheet_by_index.cell(14,8).value
	return cell_value2

def tuesday_seven_three():
	cell_value3 = worksheet_by_index.cell(15,8).value
	return cell_value3

def tuesday_seven_four():
	cell_value4 = worksheet_by_index.cell(16,8).value
	return cell_value4

def tuesday_seven_five():
	cell_value5 = worksheet_by_index.cell(17,8).value
	return cell_value5

def tuesday_seven_six():
	cell_value6 = worksheet_by_index.cell(18,8).value
	return cell_value6


#Вторник восьмой класс
def tuesday_eight_one():
	cell_value1 = worksheet_by_index.cell(13,9).value
	return cell_value1

def tuesday_eight_two():
	cell_value2 = worksheet_by_index.cell(14,9).value
	return cell_value2

def tuesday_eight_three():
	cell_value3 = worksheet_by_index.cell(15,9).value
	return cell_value3

def tuesday_eight_four():
	cell_value4 = worksheet_by_index.cell(16,9).value
	return cell_value4

def tuesday_eight_five():
	cell_value5 = worksheet_by_index.cell(17,9).value
	return cell_value5

def tuesday_eight_six():
	cell_value6 = worksheet_by_index.cell(18,9).value
	return cell_value6


#Вторник девятый класс
def tuesday_nine_one():
	cell_value1 = worksheet_by_index.cell(13,10).value
	return cell_value1

def tuesday_nine_two():
	cell_value2 = worksheet_by_index.cell(14,10).value
	return cell_value2

def tuesday_nine_three():
	cell_value3 = worksheet_by_index.cell(15,10).value
	return cell_value3

def tuesday_nine_four():
	cell_value4 = worksheet_by_index.cell(16,10).value
	return cell_value4

def tuesday_nine_five():
	cell_value5 = worksheet_by_index.cell(17,10).value
	return cell_value5

def tuesday_nine_six():
	cell_value6 = worksheet_by_index.cell(18,10).value
	return cell_value6

def tuesday_nine_seven():
	cell_value7 = worksheet_by_index.cell(19,10).value
	return cell_value7


#Вторник десятый класс
def tuesday_ten_one():
	cell_value1 = worksheet_by_index.cell(13,11).value
	return cell_value1

def tuesday_ten_two():
	cell_value2 = worksheet_by_index.cell(14,11).value
	return cell_value2

def tuesday_ten_three():
	cell_value3 = worksheet_by_index.cell(15,11).value
	return cell_value3

def tuesday_ten_four():
	cell_value4 = worksheet_by_index.cell(16,11).value
	return cell_value4

def tuesday_ten_five():
	cell_value5 = worksheet_by_index.cell(17,11).value
	return cell_value5

def tuesday_ten_six():
	cell_value6 = worksheet_by_index.cell(18,11).value
	return cell_value6


#Вторник одинадцатый класс
def tuesday_eleven_one():
	cell_value1 = worksheet_by_index.cell(13,12).value
	return cell_value1

def tuesday_eleven_two():
	cell_value2 = worksheet_by_index.cell(14,12).value
	return cell_value2

def tuesday_eleven_three():
	cell_value3 = worksheet_by_index.cell(15,12).value
	return cell_value3

def tuesday_eleven_four():
	cell_value4 = worksheet_by_index.cell(16,12).value
	return cell_value4

def tuesday_eleven_five():
	cell_value5 = worksheet_by_index.cell(17,12).value
	return cell_value5

def tuesday_eleven_six():
	cell_value6 = worksheet_by_index.cell(18,12).value
	return cell_value6


#Среда


#Среда первый класс
def wensday_one_one():
	cell_value1 = worksheet_by_index.cell(20,2).value
	return cell_value1

def wensday_one_two():
	cell_value2 = worksheet_by_index.cell(21,2).value
	return cell_value2

def wensday_one_three():
	cell_value3 = worksheet_by_index.cell(22,2).value
	return cell_value3

def wensday_one_four():
	cell_value4 = worksheet_by_index.cell(23,2).value
	return cell_value4

#Среда второй класс
def wensday_two_one():
	cell_value1 = worksheet_by_index.cell(20,3).value
	return cell_value1

def wensday_two_two():
	cell_value2 = worksheet_by_index.cell(21,3).value
	return cell_value2

def wensday_two_three():
	cell_value3 = worksheet_by_index.cell(22,3).value
	return cell_value3

def wensday_two_four():
	cell_value4 = worksheet_by_index.cell(23,3).value
	return cell_value4

def wensday_two_five():
	cell_value5 = worksheet_by_index.cell(24,3).value
	return cell_value5


#Среда третий класс
def wensday_three_one():
	cell_value1 = worksheet_by_index.cell(20,4).value
	return cell_value1

def wensday_three_two():
	cell_value2 = worksheet_by_index.cell(21,4).value
	return cell_value2

def wensday_three_three():
	cell_value3 = worksheet_by_index.cell(22,4).value
	return cell_value3

def wensday_three_four():
	cell_value4 = worksheet_by_index.cell(23,4).value
	return cell_value4

def wensday_three_five():
	cell_value5 = worksheet_by_index.cell(24,4).value
	return cell_value5


#Среда четвёртый класс
def wensday_four_one():
	cell_value1 = worksheet_by_index.cell(20,5).value
	return cell_value1

def wensday_four_two():
	cell_value2 = worksheet_by_index.cell(21,5).value
	return cell_value2

def wensday_four_three():
	cell_value3 = worksheet_by_index.cell(22,5).value
	return cell_value3

def wensday_four_four():
	cell_value4 = worksheet_by_index.cell(23,5).value
	return cell_value4

def wensday_four_five():
	cell_value5 = worksheet_by_index.cell(24,5).value
	return cell_value5


#Среда пятый класс
def wensday_five_one():
	cell_value1 = worksheet_by_index.cell(20,6).value
	return cell_value1

def wensday_five_two():
	cell_value2 = worksheet_by_index.cell(21,6).value
	return cell_value2

def wensday_five_three():
	cell_value3 = worksheet_by_index.cell(22,6).value
	return cell_value3

def wensday_five_four():
	cell_value4 = worksheet_by_index.cell(23,6).value
	return cell_value4

def wensday_five_five():
	cell_value5 = worksheet_by_index.cell(24,6).value
	return cell_value5


#Среда шестой класс
def wensday_six_one():
	cell_value1 = worksheet_by_index.cell(20,7).value
	return cell_value1

def wensday_six_two():
	cell_value2 = worksheet_by_index.cell(21,7).value
	return cell_value2

def wensday_six_three():
	cell_value3 = worksheet_by_index.cell(22,7).value
	return cell_value3

def wensday_six_four():
	cell_value4 = worksheet_by_index.cell(23,7).value
	return cell_value4

def wensday_six_five():
	cell_value5 = worksheet_by_index.cell(24,7).value
	return cell_value5

def wensday_six_six():
	cell_value6 = worksheet_by_index.cell(25,7).value
	return cell_value6


#Среда седьмой класс
def wensday_seven_one():
	cell_value1 = worksheet_by_index.cell(20,8).value
	return cell_value1

def wensday_seven_two():
	cell_value2 = worksheet_by_index.cell(21,8).value
	return cell_value2

def wensday_seven_three():
	cell_value3 = worksheet_by_index.cell(22,8).value
	return cell_value3

def wensday_seven_four():
	cell_value4 = worksheet_by_index.cell(23,8).value
	return cell_value4

def wensday_seven_five():
	cell_value5 = worksheet_by_index.cell(24,8).value
	return cell_value5

def wensday_seven_six():
	cell_value6 = worksheet_by_index.cell(25,8).value
	return cell_value6

def wensday_seven_seven():
	cell_value7 = worksheet_by_index.cell(26,8).value
	return cell_value7

#Среда восьмой класс
def wensday_eight_one():
	cell_value1 = worksheet_by_index.cell(20,9).value
	return cell_value1

def wensday_eight_two():
	cell_value2 = worksheet_by_index.cell(21,9).value
	return cell_value2

def wensday_eight_three():
	cell_value3 = worksheet_by_index.cell(22,9).value
	return cell_value3

def wensday_eight_four():
	cell_value4 = worksheet_by_index.cell(23,9).value
	return cell_value4

def wensday_eight_five():
	cell_value5 = worksheet_by_index.cell(24,9).value
	return cell_value5

def wensday_eight_six():
	cell_value6 = worksheet_by_index.cell(25,9).value
	return cell_value6

def wensday_eight_seven():
	cell_value7 = worksheet_by_index.cell(26,9).value
	return cell_value7


#Среда девятый класс
def wensday_nine_one():
	cell_value1 = worksheet_by_index.cell(20,10).value
	return cell_value1

def wensday_nine_two():
	cell_value2 = worksheet_by_index.cell(21,10).value
	return cell_value2

def wensday_nine_three():
	cell_value3 = worksheet_by_index.cell(22,10).value
	return cell_value3

def wensday_nine_four():
	cell_value4 = worksheet_by_index.cell(23,10).value
	return cell_value4

def wensday_nine_five():
	cell_value5 = worksheet_by_index.cell(24,10).value
	return cell_value5

def wensday_nine_six():
	cell_value6 = worksheet_by_index.cell(25,10).value
	return cell_value6

#Среда десятый класс
def wensday_ten_one():
	cell_value1 = worksheet_by_index.cell(20,11).value
	return cell_value1

def wensday_ten_two():
	cell_value2 = worksheet_by_index.cell(21,11).value
	return cell_value2

def wensday_ten_three():
	cell_value3 = worksheet_by_index.cell(22,11).value
	return cell_value3

def wensday_ten_four():
	cell_value4 = worksheet_by_index.cell(23,11).value
	return cell_value4

def wensday_ten_five():
	cell_value5 = worksheet_by_index.cell(24,11).value
	return cell_value5

def wensday_ten_six():
	cell_value6 = worksheet_by_index.cell(25,11).value
	return cell_value6

def wensday_ten_seven():
	cell_value7 = worksheet_by_index.cell(26,11).value
	return cell_value7


#Среда одинадцатый класс
def wensday_eleven_one():
	cell_value1 = worksheet_by_index.cell(20,12).value
	return cell_value1

def wensday_eleven_two():
	cell_value2 = worksheet_by_index.cell(21,12).value
	return cell_value2

def wensday_eleven_three():
	cell_value3 = worksheet_by_index.cell(22,12).value
	return cell_value3

def wensday_eleven_four():
	cell_value4 = worksheet_by_index.cell(23,12).value
	return cell_value4

def wensday_eleven_five():
	cell_value5 = worksheet_by_index.cell(24,12).value
	return cell_value5

def wensday_eleven_six():
	cell_value6 = worksheet_by_index.cell(25,12).value
	return cell_value6

def wensday_eleven_seven():
	cell_value7 = worksheet_by_index.cell(26,12).value
	return cell_value7


#Четверг


#Четверг первый класс
def thursday_one_one():
	cell_value1 = worksheet_by_index.cell(27,2).value
	return cell_value1

def thursday_one_two():
	cell_value2 = worksheet_by_index.cell(28,2).value
	return cell_value2

def thursday_one_three():
	cell_value3 = worksheet_by_index.cell(29,2).value
	return cell_value3


#Четверг второй класс
def thursday_two_one():
	cell_value1 = worksheet_by_index.cell(27,3).value
	return cell_value1

def thursday_two_two():
	cell_value2 = worksheet_by_index.cell(28,3).value
	return cell_value2

def thursday_two_three():
	cell_value3 = worksheet_by_index.cell(29,3).value
	return cell_value3

def thursday_two_four():
	cell_value4 = worksheet_by_index.cell(30,3).value
	return cell_value4


#Четверг третий класс
def thursday_three_one():
	cell_value1 = worksheet_by_index.cell(27,4).value
	return cell_value1

def thursday_three_two():
	cell_value2 = worksheet_by_index.cell(28,4).value
	return cell_value2

def thursday_three_three():
	cell_value3 = worksheet_by_index.cell(29,4).value
	return cell_value3

def thursday_three_four():
	cell_value4 = worksheet_by_index.cell(30,4).value
	return cell_value4

def thursday_three_five():
	cell_value5 = worksheet_by_index.cell(31,4).value
	return cell_value5


#Четверг четвёртый класс
def thursday_four_one():
	cell_value1 = worksheet_by_index.cell(27,5).value
	return cell_value1

def thursday_four_two():
	cell_value2 = worksheet_by_index.cell(28,5).value
	return cell_value2

def thursday_four_three():
	cell_value3 = worksheet_by_index.cell(29,5).value
	return cell_value3

def thursday_four_four():
	cell_value4 = worksheet_by_index.cell(30,5).value
	return cell_value4

def thursday_four_five():
	cell_value5 = worksheet_by_index.cell(31,5).value
	return cell_value5


#Четверг пятый класс
def thursday_five_one():
	cell_value1 = worksheet_by_index.cell(27,6).value
	return cell_value1

def thursday_five_two():
	cell_value2 = worksheet_by_index.cell(28,6).value
	return cell_value2

def thursday_five_three():
	cell_value3 = worksheet_by_index.cell(29,6).value
	return cell_value3

def thursday_five_four():
	cell_value4 = worksheet_by_index.cell(30,6).value
	return cell_value4

def thursday_five_five():
	cell_value5 = worksheet_by_index.cell(31,6).value
	return cell_value5


#Четверг шестой класс
def thursday_six_one():
	cell_value1 = worksheet_by_index.cell(27,7).value
	return cell_value1

def thursday_six_two():
	cell_value2 = worksheet_by_index.cell(28,7).value
	return cell_value2

def thursday_six_three():
	cell_value3 = worksheet_by_index.cell(29,7).value
	return cell_value3

def thursday_six_four():
	cell_value4 = worksheet_by_index.cell(30,7).value
	return cell_value4

def thursday_six_five():
	cell_value5 = worksheet_by_index.cell(31,7).value
	return cell_value5

def thursday_six_six():
	cell_value6 = worksheet_by_index.cell(32,7).value
	return cell_value6


#Четверг седьмой класс
def thursday_seven_one():
	cell_value1 = worksheet_by_index.cell(27,8).value
	return cell_value1

def thursday_seven_two():
	cell_value2 = worksheet_by_index.cell(28,8).value
	return cell_value2

def thursday_seven_three():
	cell_value3 = worksheet_by_index.cell(29,8).value
	return cell_value3

def thursday_seven_four():
	cell_value4 = worksheet_by_index.cell(30,8).value
	return cell_value4

def thursday_seven_five():
	cell_value5 = worksheet_by_index.cell(31,8).value
	return cell_value5

def thursday_seven_six():
	cell_value6 = worksheet_by_index.cell(32,8).value
	return cell_value6


#Четверг восьмой класс
def thursday_eight_one():
	cell_value1 = worksheet_by_index.cell(27,9).value
	return cell_value1

def thursday_eight_two():
	cell_value2 = worksheet_by_index.cell(28,9).value
	return cell_value2

def thursday_eight_three():
	cell_value3 = worksheet_by_index.cell(29,9).value
	return cell_value3

def thursday_eight_four():
	cell_value4 = worksheet_by_index.cell(30,9).value
	return cell_value4

def thursday_eight_five():
	cell_value5 = worksheet_by_index.cell(31,9).value
	return cell_value5

def thursday_eight_six():
	cell_value6 = worksheet_by_index.cell(32,9).value
	return cell_value6


#Четверг девятый класс
def thursday_nine_one():
	cell_value1 = worksheet_by_index.cell(27,10).value
	return cell_value1

def thursday_nine_two():
	cell_value2 = worksheet_by_index.cell(28,10).value
	return cell_value2

def thursday_nine_three():
	cell_value3 = worksheet_by_index.cell(29,10).value
	return cell_value3

def thursday_nine_four():
	cell_value4 = worksheet_by_index.cell(30,10).value
	return cell_value4

def thursday_nine_five():
	cell_value5 = worksheet_by_index.cell(31,10).value
	return cell_value5

def thursday_nine_six():
	cell_value6 = worksheet_by_index.cell(32,10).value
	return cell_value6


#Четверг десятый класс
def thursday_ten_one():
	cell_value1 = worksheet_by_index.cell(27,11).value
	return cell_value1

def thursday_ten_two():
	cell_value2 = worksheet_by_index.cell(28,11).value
	return cell_value2

def thursday_ten_three():
	cell_value3 = worksheet_by_index.cell(29,11).value
	return cell_value3

def thursday_ten_four():
	cell_value4 = worksheet_by_index.cell(30,11).value
	return cell_value4

def thursday_ten_five():
	cell_value5 = worksheet_by_index.cell(31,11).value
	return cell_value5

def thursday_ten_six():
	cell_value6 = worksheet_by_index.cell(32,11).value
	return cell_value6


#Четверг одинадцатый класс
def thursday_eleven_one():
	cell_value1 = worksheet_by_index.cell(27,12).value
	return cell_value1

def thursday_eleven_two():
	cell_value2 = worksheet_by_index.cell(28,12).value
	return cell_value2

def thursday_eleven_three():
	cell_value3 = worksheet_by_index.cell(29,12).value
	return cell_value3

def thursday_eleven_four():
	cell_value4 = worksheet_by_index.cell(30,12).value
	return cell_value4

def thursday_eleven_five():
	cell_value5 = worksheet_by_index.cell(31,12).value
	return cell_value5

def thursday_eleven_six():
	cell_value6 = worksheet_by_index.cell(32,12).value
	return cell_value6

def thursday_eleven_seven():
	cell_value7 = worksheet_by_index.cell(33,12).value
	return cell_value7


#Пятница


#Пятница первый класс
def friday_one_one():
	cell_value1 = worksheet_by_index.cell(34,2).value
	return cell_value1

def friday_one_two():
	cell_value2 = worksheet_by_index.cell(35,2).value
	return cell_value2

def friday_one_three():
	cell_value3 = worksheet_by_index.cell(36,2).value
	return cell_value3

def friday_one_four():
	cell_value4 = worksheet_by_index.cell(37,2).value
	return cell_value4


#Пятница второй класс
def friday_two_one():
	cell_value1 = worksheet_by_index.cell(34,3).value
	return cell_value1

def friday_two_two():
	cell_value2 = worksheet_by_index.cell(35,3).value
	return cell_value2

def friday_two_three():
	cell_value3 = worksheet_by_index.cell(36,3).value
	return cell_value3

def friday_two_four():
	cell_value4 = worksheet_by_index.cell(37,3).value
	return cell_value4


#Пятница третий класс
def friday_three_one():
	cell_value1 = worksheet_by_index.cell(34,4).value
	return cell_value1

def thursday_three_two():
	cell_value2 = worksheet_by_index.cell(35,4).value
	return cell_value2

def friday_three_three():
	cell_value3 = worksheet_by_index.cell(36,4).value
	return cell_value3

def friday_three_four():
	cell_value4 = worksheet_by_index.cell(37,4).value
	return cell_value4


#Пятница четвёртый класс
def friday_four_one():
	cell_value1 = worksheet_by_index.cell(34,5).value
	return cell_value1

def friday_four_two():
	cell_value2 = worksheet_by_index.cell(35,5).value
	return cell_value2

def friday_four_three():
	cell_value3 = worksheet_by_index.cell(36,5).value
	return cell_value3

def friday_four_four():
	cell_value4 = worksheet_by_index.cell(37,5).value
	return cell_value4

def friday_four_five():
	cell_value5 = worksheet_by_index.cell(38,5).value
	return cell_value5


#Пятница пятый класс
def friday_five_one():
	cell_value1 = worksheet_by_index.cell(34,6).value
	return cell_value1

def friday_five_two():
	cell_value2 = worksheet_by_index.cell(35,6).value
	return cell_value2

def friday_five_three():
	cell_value3 = worksheet_by_index.cell(36,6).value
	return cell_value3

def friday_five_four():
	cell_value4 = worksheet_by_index.cell(37,6).value
	return cell_value4

def friday_five_five():
	cell_value5 = worksheet_by_index.cell(38,6).value
	return cell_value5


#Пятница шестой класс
def friday_six_one():
	cell_value1 = worksheet_by_index.cell(34,7).value
	return cell_value1

def friday_six_two():
	cell_value2 = worksheet_by_index.cell(35,7).value
	return cell_value2

def friday_six_three():
	cell_value3 = worksheet_by_index.cell(36,7).value
	return cell_value3

def friday_six_four():
	cell_value4 = worksheet_by_index.cell(37,7).value
	return cell_value4

def friday_six_five():
	cell_value5 = worksheet_by_index.cell(38,7).value
	return cell_value5


#Пятница седьмой класс
def friday_seven_one():
	cell_value1 = worksheet_by_index.cell(34,8).value
	return cell_value1

def friday_seven_two():
	cell_value2 = worksheet_by_index.cell(35,8).value
	return cell_value2

def friday_seven_three():
	cell_value3 = worksheet_by_index.cell(36,8).value
	return cell_value3

def friday_seven_four():
	cell_value4 = worksheet_by_index.cell(37,8).value
	return cell_value4

def friday_seven_five():
	cell_value5 = worksheet_by_index.cell(38,8).value
	return cell_value5


#Пятница восьмой класс
def friday_eight_one():
	cell_value1 = worksheet_by_index.cell(34,9).value
	return cell_value1

def friday_eight_two():
	cell_value2 = worksheet_by_index.cell(35,9).value
	return cell_value2

def friday_eight_three():
	cell_value3 = worksheet_by_index.cell(36,9).value
	return cell_value3

def friday_eight_four():
	cell_value4 = worksheet_by_index.cell(37,9).value
	return cell_value4

def friday_eight_five():
	cell_value5 = worksheet_by_index.cell(38,9).value
	return cell_value5

def friday_eight_six():
	cell_value6 = worksheet_by_index.cell(39,9).value
	return cell_value6


#Пятница девятый класс
def friday_nine_one():
	cell_value1 = worksheet_by_index.cell(34,10).value
	return cell_value1

def friday_nine_two():
	cell_value2 = worksheet_by_index.cell(35,10).value
	return cell_value2

def friday_nine_three():
	cell_value3 = worksheet_by_index.cell(36,10).value
	return cell_value3

def friday_nine_four():
	cell_value4 = worksheet_by_index.cell(37,10).value
	return cell_value4

def friday_nine_five():
	cell_value5 = worksheet_by_index.cell(38,10).value
	return cell_value5

def friday_nine_six():
	cell_value6 = worksheet_by_index.cell(39,10).value
	return cell_value6

def friday_nine_seven():
	cell_value7 = worksheet_by_index.cell(40,10).value
	return cell_value7


#Пятница десятый класс
def friday_ten_one():
	cell_value1 = worksheet_by_index.cell(34,11).value
	return cell_value1

def friday_ten_two():
	cell_value2 = worksheet_by_index.cell(35,11).value
	return cell_value2

def friday_ten_three():
	cell_value3 = worksheet_by_index.cell(36,11).value
	return cell_value3

def friday_ten_four():
	cell_value4 = worksheet_by_index.cell(37,11).value
	return cell_value4

def friday_ten_five():
	cell_value5 = worksheet_by_index.cell(38,11).value
	return cell_value5

def friday_ten_six():
	cell_value6 = worksheet_by_index.cell(39,11).value
	return cell_value6

def friday_ten_seven():
	cell_value7 = worksheet_by_index.cell(40,11).value
	return cell_value7


#Пятница одинадцатый класс
def friday_eleven_one():
	cell_value1 = worksheet_by_index.cell(34,12).value
	return cell_value1

def friday_eleven_two():
	cell_value2 = worksheet_by_index.cell(35,12).value
	return cell_value2

def friday_eleven_three():
	cell_value3 = worksheet_by_index.cell(36,12).value
	return cell_value3

def friday_eleven_four():
	cell_value4 = worksheet_by_index.cell(37,12).value
	return cell_value4

def friday_eleven_five():
	cell_value5 = worksheet_by_index.cell(38,12).value
	return cell_value5

def friday_eleven_six():
	cell_value6 = worksheet_by_index.cell(39,12).value
	return cell_value6


#Суббота


def sb_one():
	cell_value1 = worksheet_by_index.cell(41,2).value
	return cell_value1

def sb_two():
	cell_value1 = worksheet_by_index.cell(41,3).value
	return cell_value1

def sb_three():
	cell_value1 = worksheet_by_index.cell(41,4).value
	return cell_value1

def sb_four():
	cell_value1 = worksheet_by_index.cell(41,5).value
	return cell_value1

def sb_five():
	cell_value1 = worksheet_by_index.cell(41,6).value
	return cell_value1

def sb_six():
	cell_value1 = worksheet_by_index.cell(41,7).value
	return cell_value1

def sb_seven():
	cell_value1 = worksheet_by_index.cell(41,8).value
	return cell_value1

def sb_eight():
	cell_value1 = worksheet_by_index.cell(41,9).value
	return cell_value1

def sb_nine():
	cell_value1 = worksheet_by_index.cell(41,10).value
	return cell_value1

def sb_ten_time():
	cell_value1 = worksheet_by_index.cell(41,11).value
	return cell_value1

def sb_ten():
	cell_value1 = worksheet_by_index.cell(42,11).value
	return cell_value1

def sb_eleven_time():
	cell_value1 = worksheet_by_index.cell(41,12).value
	return cell_value1

def sb_eleven():
	cell_value1 = worksheet_by_index.cell(42,12).value
	return cell_value1









