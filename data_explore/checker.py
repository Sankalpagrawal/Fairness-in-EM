import csv

def updatecsv(fname,listy):
    out_file = fname  
    row_writer = csv.writer(open(out_file, "w",encoding="utf-8", newline=''))  
    for row in listy:
        row_writer.writerow(row)
    print("CSV File Updated.")

def getdata(fname):
	listy=list()
	row_reader = csv.reader(open(fname, "r", encoding="utf8"))  
	for row in row_reader:
	    listy.append(row)

	return listy


def getter(fname,num):
	listy=list()
	row_reader = csv.reader(open(fname, "r", encoding="utf8"))  
	for row in row_reader:
	    listy.append(row)

	# print(listy[0])
	# print(listy[1]) 
	dic = dict()
	for i,rw in enumerate(listy):
		if(i==0):
			pass
		else:
			dic[int(rw[0])]=rw[num]

	return dic


labeled = getdata('../music_labeled_data.csv')
genre1 = getter('../music1.csv',-1)
genre2 = getter('../music2.csv',-1)

print(labeled[0][2],labeled[0][3])

print(len(genre1))
print(len(genre2))

for i,x in enumerate(labeled):
	if(i==0):
		labeled[i].append("lgenre")
		labeled[i].append("rgenre")

	if(i!=0):
		lsno = int(labeled[i][2])
		rsno = int(labeled[i][3])
		labeled[i].append(genre1[lsno])
		labeled[i].append(genre2[rsno])

print(labeled[0])
# for x in labeled:
# 	print(x[-2])

# updatecsv('../music_labeled_data.csv',labeled)
# genre2 = getter('../music2.csv',-1)

# print(len(genre1),len(genre2))

# g1 = list(genre1.values())
# g2 = list(genre2.values())

# g1.sort()
# g2.sort()

# # print(g1,g2)
# def removal(genre_dic,grp):
# 	gl1  = list(genre_dic.keys())
# 	genre_dic[grp] = 0
# 	for g in gl1:
# 		if g[0:len(grp)]==(grp) and g!=grp:
# 			genre_dic[grp]+= genre_dic[g]
# 			genre_dic.pop(g)
# 	print(len(genre_dic))
# 	return genre_dic

# print(len(genre1))
# genre1 = removal(genre1,'Pop')
# genre1 = removal(genre1,'Rap & Hip-Hop')
# genre1 = removal(genre1,'Rock')
# genre1 = removal(genre1,'Dance')
# genre1 = removal(genre1,'Country')
# genre1 = removal(genre1,'Electronic')
# genre1 = removal(genre1,'Alternative')
# genre1 = removal(genre1,'Soundtrack')
# for x in list(genre1.keys()):
# 	print(x,genre1[x])