# path_A

# American 165
# american 137 or 212/632-5100 american': 1 dive american: 1 or 212/941-0772 american'": 1, only in las vegas'": 1 old san francisco'": 3 californian 12 southern': 8  'southwestern': 1
# French/italian/european 164
# eastern european'": 1 east european'": 2 continental 19 russian/german': 1
# french 63 italian 78

# Asian 88
# asian 72 and 212/614-9345 asian'": 1 or 415/982-3811 asian'": 1 middle eastern'": 6 greek and middle eastern'": 5 delicatessen:3

# Diners/Cafes 35
# coffee bar 25 coffee shops/diners'": 5 steak houses'": 5

# fast food/bbq 30
# seafood 16 health food'": 2 barbecue': 5  vegetarian': 2,buffets': 5


# Fusion food(Mexican/mediterranean/caribbean) 50
# caribbean': 4 tel caribbean:1 'cajun': 1, fusion': 1 international': 6, 'ext 6108 international'": 1, mediterannean 18 mexican 9 latin american'": 6 mexican/latin american/spanish'": 3

# B

# American 70
# american': 15, "'american (new)'": 25,  "'american (traditional)'": 1 'southwestern': 4, 'southern/soul': 7, 'californian': 18
# diners/cafes 44
# "'coffee shops'": 7, 'coffeehouses': 2, 'cafeterias': 4, 'diners': 9, 'steakhouses': 17, 'eclectic': 5, 
# Italian/French/European 70
# 'ukrainian': 2, 'polish': 1, 'spanish': 1, , 'scandinavian': 1, 'russian': 2, 'continental': 9
# 'italian': 20, , "'nuova cucina italian'": 1 "'french (new)'": 13, "'french (classic)'": 9 "'french bistro'": 10, 'french': 1, 

# Asian 69
# "'middle eastern'": 3, 'indonesian': 1, 'vietnamese': 4, 'japanese': 12, 'afghan': 1, 'indian': 7, 'greek': 2, 'pan-asian': 1,  'thai': 11, 'asian': 3 'cambodian': 1 'delis': 6, noodle shops'": 3, 'chinese': 14,
# fast food/bbq 47
# "'health food'": 2, 'desserts': 2, 'sandwiches': 1, 'vegetarian': 3, 'bbq': 4,  'seafood': 13, 'chicken': 1, "'fast food'": 1, 'hamburgers': 11, "'hot dogs'": 4, 'pizza': 5,
# Fusion food(Mexican/mediterranean/caribbean) 31
# 'mediterranean': 4, 'caribbean': 2, 'cuban': 3, 'cajun/creole': 2, "'pacific new wave'": 4 pacific rim'": 1, mexican': 12, 'mexican/tex-mex': 1, 'tex-mex': 2,


##### Using this link- https://thispointer.com/python-add-a-column-to-an-existing-csv-file/

from csv import writer
from csv import reader
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

def get_list_of_groups_for_A(mat):
    t1 = mat.to_numpy()
    groups = ['group']
    for x in t1:
        if x[-2] in ['american', "'or 212/632-5100 american'" ,"'dive american'","'or 212/941-0772 american'","'only in las vegas'","'old san francisco'",'californian' ,'southern', 'southwestern']:
            groups.append("American")
        elif x[-2] in ['french','italian',"'eastern european'","'east european'",'continental','russian/german']:
            groups.append("French/Italian/European")
        elif x[-2] in ['asian', "'and 212/614-9345 asian'" , "'or 415/982-3811 asian'", "'middle eastern'","'greek and middle eastern'",'delicatessen']:
            groups.append("Asian")
        elif x[-2] in ["'coffee bar'" , "'coffee shops/diners'", "'steak houses'"]:
            groups.append("Diners/Cafes")
        elif x[-2] in ['seafood',"'health food'",'barbecue','vegetarian','buffets']:
            groups.append("bbq/fast food")
        else:
            groups.append("Fusion food(Mexican/mediterranean/caribbean)")
    return groups 


def get_list_of_groups_for_B(mat):
    t1 = mat.to_numpy()
    groups = ['group']
    for x in t1:
        if x[-2] in ['american', "'american (new)'", "'american (traditional)'", 'southwestern', 'southern/soul', 'californian']:
            groups.append("American")
        elif x[-2] in ["'coffee shops'",'coffeehouses','cafeterias','diners','steakhouses','eclectic']:
            groups.append("Diners/Cafes")
        elif x[-2] in ['ukrainian','polish','spanish','scandinavian','russian','continental','italian',"'nuova cucina italian'","'french (new)'","'french (classic)'", "'french bistro'",'french']:
            groups.append("French/Italian/European")
        elif x[-2] in ["'middle eastern'",'indonesian','vietnamese','japanese','afghan','indian','greek','pan-asian','thai','asian','cambodian','delis',"'noodle shops'",'chinese']:
            groups.append("Asian")
        elif x[-2] in ["'health food'",'desserts','sandwiches','vegetarian','bbq','seafood','chicken',"'fast food'",'hamburgers',"'hot dogs'",'pizza']:
            groups.append("bbq/fast food")
        else:
            groups.append("Fusion food(Mexican/mediterranean/caribbean)")
    return groups

l1 = get_list_of_groups_for_A(A)
l2 = get_list_of_groups_for_B(B)

path_A = path_variable+"restaurant/fodors.csv"
path_B = path_variable+"restaurant/zagats.csv"

path_A_1 = path_variable+"restaurant/fodors_1.csv"
path_B_1 = path_variable+"restaurant/zagats_1.csv"

add_column_in_csv(path_A, path_A_1, lambda row, line_num: row.append(l1[line_num - 1]))
add_column_in_csv(path_B, path_B_1, lambda row, line_num: row.append(l2[line_num - 1]))