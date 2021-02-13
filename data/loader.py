import csv

def check(x,y):
	return (x in dc.keys() and dc[x] == y) or (y in dc.keys() and dc[y]==x) or x==y

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

listy = getter('./restaurants.csv')[1:]
lbl = getter('./labeled.csv')[1:]

dc = dict()
for x in lbl:
	dc[x[0]] = x[1]
	dc[x[1]] = x[0]

colA = ["address","city","id","name","phone","type"]


new_fin = []
newl = ["_id"]
for x in colA:
	newl.append("ltable."+x)
for x in colA:
	newl.append("rtable."+x)

newl.append("label")
new_fin.append(newl) 

print(new_fin)
s=1
for i,li in enumerate(listy):
	for l in listy:
		
		new_fin.append([s]+listy[i].copy())
		new_fin[-1].extend(l.copy())
		# print(li,l)

		if(check(li[2],l[2])):
			new_fin[-1].append(1)
		else:
			new_fin[-1].append(0)
		
		s+=1


print(s)
updatecsv("labeled_res_data.csv",new_fin)
