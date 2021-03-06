file = open('infile_table.txt','r')
file_out = open('outfile.txt','w') 

list_of_lists=[]
dict_of_dicts={}
id=0
for line in file:

	weight=float(line.split()[0])
	height=float(line.split()[1])
	BMI=weight/height**2
	list_of_lists.append([weight, height,BMI])

	dict_of_dicts[id]={"Patient": id, \
				   "Weight": weight, \
				   "Height": height,"BMI": BMI}
	id=id+1
	file_out.write("Weight {:.2f} Weight {:.2f} gives BMI: {:.2f} \n".format(weight,height,BMI))


print(list_of_lists)

file.close()
file_out.close()
