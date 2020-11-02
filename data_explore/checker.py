import csv

def updatecsv(listy):
    out_file = 'roaddist.csv'  
    row_writer = csv.writer(open(out_file, "w",encoding="utf-8", newline=''))  
    for row in listy:
        row_writer.writerow(row)
    print("CSV File Updated.")

def getter(fname,num):
	listy=list()
	row_reader = csv.reader(open(fname, "r", encoding="utf8"))  
	for row in row_reader:
	    listy.append(row)

	print(listy[0]) 
	dic = dict()
	for i,rw in enumerate(listy):
		if(i==0):
			pass
		if(rw[num] not in dic):
			dic[rw[num]]=0
			# print(rw[num])
		dic[rw[num]]+=1

	print(len(dic))
	return dic

genre1 = getter('../music2.csv',-1)
# genre2 = getter('../music2.csv',-1)

# print(len(genre1),len(genre2))

# g1 = list(genre1.values())
# g2 = list(genre2.values())

# g1.sort()
# g2.sort()

# print(g1,g2)
def removal(genre_dic,grp):
	gl1  = list(genre_dic.keys())
	genre_dic[grp] = 0
	for g in gl1:
		if g[0:len(grp)]==(grp) and g!=grp:
			genre_dic[grp]+= genre_dic[g]
			genre_dic.pop(g)
	print(len(genre_dic))
	return genre_dic

print(len(genre1))
genre1 = removal(genre1,'Pop')
genre1 = removal(genre1,'Rap & Hip-Hop')
genre1 = removal(genre1,'Rock')
genre1 = removal(genre1,'Dance')
genre1 = removal(genre1,'Country')
genre1 = removal(genre1,'Electronic')
genre1 = removal(genre1,'Alternative')
genre1 = removal(genre1,'Soundtrack')
for x in list(genre1.keys()):
	print(x,genre1[x])