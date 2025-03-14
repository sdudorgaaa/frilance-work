import xlrd

workbook = xlrd.open_workbook('facult.xls',on_demand=True)
worksheet_by_index = workbook.sheet_by_index(0)

#Понедельник

def monday_prepod():
    cell_value1 = worksheet_by_index.cell(1,1).value
    return cell_value1

def monday_facult_name():
    cell_value1 = worksheet_by_index.cell(1,2).value
    return cell_value1

def monday_school_class():
    cell_value1 = worksheet_by_index.cell(1,3).value
    return cell_value1

def monday_time():
    cell_value1 = worksheet_by_index.cell(1,4).value
    return cell_value1

def monday_kab():
    cell_value1 = worksheet_by_index.cell(1,5).value
    return cell_value1


# Вторник one

def tuesday_prepod_one():
    cell_value1 = worksheet_by_index.cell(2,1).value
    return cell_value1

def tuesday_facult_name_one():
    cell_value1 = worksheet_by_index.cell(2,2).value
    return cell_value1

def tuesday_school_class_one():
    cell_value1 = worksheet_by_index.cell(2,3).value
    return cell_value1

def tuesday_time_one():
    cell_value1 = worksheet_by_index.cell(2,4).value
    return cell_value1

def tuesday_kab_one():
    cell_value1 = worksheet_by_index.cell(2,5).value
    return cell_value1

#Вторник two

def tuesday_prepod_two():
    cell_value1 = worksheet_by_index.cell(3,1).value
    return cell_value1

def tuesday_facult_name_two():
    cell_value1 = worksheet_by_index.cell(3,2).value
    return cell_value1

def tuesday_school_class_two():
    cell_value1 = worksheet_by_index.cell(3,3).value
    return cell_value1

def tuesday_time_two():
    cell_value1 = worksheet_by_index.cell(3,4).value
    return cell_value1

def tuesday_kab_two():
    cell_value1 = worksheet_by_index.cell(3,5).value
    return cell_value1

#Вторник three

def tuesday_prepod_three():
    cell_value1 = worksheet_by_index.cell(4,1).value
    return cell_value1

def tuesday_facult_name_three():
    cell_value1 = worksheet_by_index.cell(4,2).value
    return cell_value1

def tuesday_school_class_three():
    cell_value1 = worksheet_by_index.cell(4,3).value
    return cell_value1

def tuesday_time_three():
    cell_value1 = worksheet_by_index.cell(4,4).value
    return cell_value1

def tuesday_kab_three():
    cell_value1 = worksheet_by_index.cell(4,5).value
    return cell_value1

#Среда one 

def wensday_prepod_one():
    cell_value1 = worksheet_by_index.cell(5,1).value
    return cell_value1

def wensday_facult_name_one():
    cell_value1 = worksheet_by_index.cell(5,2).value
    return cell_value1

def wensday_school_class_one():
    cell_value1 = worksheet_by_index.cell(5,3).value
    return cell_value1

def wensday_time_one():
    cell_value1 = worksheet_by_index.cell(5,4).value
    return cell_value1

def wensday_kab_one():
    cell_value1 = worksheet_by_index.cell(5,5).value
    return cell_value1

#Среда two

def wensday_prepod_two():
    cell_value1 = worksheet_by_index.cell(6,1).value
    return cell_value1

def wensday_facult_name_two():
    cell_value1 = worksheet_by_index.cell(6,2).value
    return cell_value1

def wensday_school_class_two():
    cell_value1 = worksheet_by_index.cell(6,3).value
    return cell_value1

def wensday_time_two():
    cell_value1 = worksheet_by_index.cell(6,4).value
    return cell_value1

def wensday_kab_two():
    cell_value1 = worksheet_by_index.cell(6,5).value
    return cell_value1

# Пятница one

def friday_prepod_one():
    cell_value1 = worksheet_by_index.cell(7,1).value
    return cell_value1

def friday_facult_name_one():
    cell_value1 = worksheet_by_index.cell(7,2).value
    return cell_value1

def friday_school_class_one():
    cell_value1 = worksheet_by_index.cell(7,3).value
    return cell_value1

def friday_time_one():
    cell_value1 = worksheet_by_index.cell(7,4).value
    return cell_value1

def friday_kab_one():
    cell_value1 = worksheet_by_index.cell(7,5).value
    return cell_value1

#Пятница two

def friday_prepod_two():
    cell_value1 = worksheet_by_index.cell(8,1).value
    return cell_value1

def friday_facult_name_two():
    cell_value1 = worksheet_by_index.cell(8,2).value
    return cell_value1

def friday_school_class_two():
    cell_value1 = worksheet_by_index.cell(8,3).value
    return cell_value1

def friday_time_two():
    cell_value1 = worksheet_by_index.cell(8,4).value
    return cell_value1

def friday_kab_two():
    cell_value1 = worksheet_by_index.cell(8,5).value
    return cell_value1

#Пятница three

def friday_prepod_three():
    cell_value1 = worksheet_by_index.cell(9,1).value
    return cell_value1

def friday_facult_name_three():
    cell_value1 = worksheet_by_index.cell(9,2).value
    return cell_value1

def friday_school_class_three():
    cell_value1 = worksheet_by_index.cell(9,3).value
    return cell_value1

def friday_time_three():
    cell_value1 = worksheet_by_index.cell(9,4).value
    return cell_value1

def friday_kab_three():
    cell_value1 = worksheet_by_index.cell(9,5).value
    return cell_value1

#Пятница four

def friday_prepod_four():
    cell_value1 = worksheet_by_index.cell(10,1).value
    return cell_value1

def friday_facult_name_four():
    cell_value1 = worksheet_by_index.cell(10,2).value
    return cell_value1

def friday_school_class_four():
    cell_value1 = worksheet_by_index.cell(10,3).value
    return cell_value1

def friday_time_four():
    cell_value1 = worksheet_by_index.cell(10,4).value
    return cell_value1

def friday_kab_four():
    cell_value1 = worksheet_by_index.cell(10,5).value
    return cell_value1

# Суббота one

def saturday_prepod_one():
    cell_value1 = worksheet_by_index.cell(11,1).value
    return cell_value1

def saturday_facult_name_one():
    cell_value1 = worksheet_by_index.cell(11,2).value
    return cell_value1

def saturday_school_class_one():
    cell_value1 = worksheet_by_index.cell(11,3).value
    return cell_value1

def saturday_time_one():
    cell_value1 = worksheet_by_index.cell(11,4).value
    return cell_value1

def saturday_kab_one():
    cell_value1 = worksheet_by_index.cell(11,5).value
    return cell_value1

#Суббота two

def saturday_prepod_two():
    cell_value1 = worksheet_by_index.cell(12,1).value
    return cell_value1

def saturday_facult_name_two():
    cell_value1 = worksheet_by_index.cell(12,2).value
    return cell_value1

def saturday_school_class_two():
    cell_value1 = worksheet_by_index.cell(12,3).value
    return cell_value1

def saturday_time_two():
    cell_value1 = worksheet_by_index.cell(12,4).value
    return cell_value1

def saturday_kab_two():
    cell_value1 = worksheet_by_index.cell(12,5).value
    return cell_value1

#Суббота three

def saturday_prepod_three():
    cell_value1 = worksheet_by_index.cell(13,1).value
    return cell_value1

def saturday_facult_name_three():
    cell_value1 = worksheet_by_index.cell(13,2).value
    return cell_value1

def saturday_school_class_three():
    cell_value1 = worksheet_by_index.cell(13,3).value
    return cell_value1

def saturday_time_three():
    cell_value1 = worksheet_by_index.cell(13,4).value
    return cell_value1

def saturday_kab_three():
    cell_value1 = worksheet_by_index.cell(13,5).value
    return cell_value1

#Суббота four

def saturday_prepod_four():
    cell_value1 = worksheet_by_index.cell(14,1).value
    return cell_value1

def saturday_facult_name_four():
    cell_value1 = worksheet_by_index.cell(14,2).value
    return cell_value1

def saturday_school_class_four():
    cell_value1 = worksheet_by_index.cell(14,3).value
    return cell_value1

def saturday_time_four():
    cell_value1 = worksheet_by_index.cell(14,4).value
    return cell_value1

def saturday_kab_four():
    cell_value1 = worksheet_by_index.cell(14,5).value
    return cell_value1

#Суббота five

def saturday_prepod_five():
    cell_value1 = worksheet_by_index.cell(15,1).value
    return cell_value1

def saturday_facult_name_five():
    cell_value1 = worksheet_by_index.cell(15,2).value
    return cell_value1

def saturday_school_class_five():
    cell_value1 = worksheet_by_index.cell(15,3).value
    return cell_value1

def saturday_time_five():
    cell_value1 = worksheet_by_index.cell(15,4).value
    return cell_value1

def saturday_kab_five():
    cell_value1 = worksheet_by_index.cell(15,5).value
    return cell_value1





