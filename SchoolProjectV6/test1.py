from functools import reduce


PERSONS_FIELDS_STRING = "person_id,first_name,last_name,email,address,tel,salary,login,password,position_id,course_id"
print("('" + (PERSONS_FIELDS_STRING.replace(",", "','")) + "')")
convert_to_fields = lambda s : "('" + (','.join(s.split(',')[1:]).replace(",", "','")) + "')"
print (convert_to_fields("position_id,position_name,description"))

TABLE_NAME_PERSONS = "persons"
PERSONS_FIELDS_STRING = "person_id,first_name,last_name,email,address,tel,salary,login,password,position_id,course_id"
# lambda
# ("first_name","last_name","email","address","tel","salary","login","password","position_id","course_id")
# convert_to_db_fields =  lambda s: "('" + "','".join(s.split(",")[1:]) + "')"
# convert_to_db_fields = "(" + ",".join(map(lambda s:"'"+s+"'", PERSONS_FIELDS_STRING.split(",")[1:] )) + ")"
convert_to_db_fields = "('" +  reduce(lambda s1,s2: s1 + "','" + s2, PERSONS_FIELDS_STRING.split(",")[1:]) + "')"
# (?,?,?,?,?,?,?,?,?,?)
convert_to_db_values =  lambda s:  s
# join()
# map()

# SQL_IMPORT_CSV_PERSONS = F"""
# INSERT INTO "{TABLE_NAME_PERSONS}" 
# {convert_to_db_fields(PERSONS_FIELDS_STRING)}
# VALUES 
# {convert_to_db_fields(PERSONS_FIELDS_STRING)};

# """

SQL_IMPORT_CSV_PERSONS = F"""
INSERT INTO "{TABLE_NAME_PERSONS}" 
{convert_to_db_fields}
VALUES 
{convert_to_db_values(PERSONS_FIELDS_STRING)};

"""

# a = PERSONS_FIELDS_STRING.split("")
# str(s)

# convert_to_db_fields = lambda a: a.split(',')
# a = str(convert_to_db_fields(PERSONS_FIELDS_STRING)).strip('[] ')
print (SQL_IMPORT_CSV_PERSONS)

