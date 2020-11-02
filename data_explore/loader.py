import csv

def updatecsv(fname,listy):
    out_file = fname  
    row_writer = csv.writer(open(out_file, "w",encoding="utf-8", newline=''))  
    for row in listy:
        row_writer.writerow(row)
    print("CSV File Updated.")

def getter(fname):
	listy=list()
	row_reader = csv.reader(open(fname, "r", encoding="utf8"))  
	for row in row_reader:
	    listy.append(row)

	print(listy[0]) 
	return listy

listy = getter('../music2.csv')

count = dict()
genres = ['Pop','Rap & Hip-Hop','Rock','Dance','Country','Electronic','Alternative','Soundtrack','Other']

for x in genres:
	count[x]=0

num = -2
for i,rw in enumerate(listy):
	if(i==0):
		pass
	else:
		flag=0
		for gj in genres:
			x = len(gj)
			if(rw[num][0:x] == gj):
				count[gj]+=1
				if(gj == 'Rap & Hip-Hop'):
					listy[i][-1] = 'Hip-Hop'
				else:
					listy[i][-1] = gj
				flag=1
				break
		if(flag==0):
			count['Other']+=1
			listy[i][-1] = 'Other'

# for x in list(listy):
# 	print(x[-1])

print(count)

# updatecsv('../music2.csv',listy)
