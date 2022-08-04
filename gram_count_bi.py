# python3 gram_count_bi.py
# python3 gram_count_bi.py > data_bgs_color.txt


#f = open('log_bgs_wiki103.txt')
f = open('freq_bgs.txt')
#f = open('freq_ugs.txt')
txt = f.read()
f.close()
txt = txt.lower()
txtlist = txt.split('\n')

color_list=[]
color_list.append(r"'red'")
color_list.append(r"'blue'")
color_list.append(r"'green'")
color_list.append(r"'yellow'")
color_list.append(r"'orange'")
color_list.append(r"'purple'")
color_list.append(r"'pink'")
color_list.append(r"'brown'")
color_list.append(r"'white'")
color_list.append(r"'black'")
color_list.append(r"'grey'")
color_list.append(r"'gray'")

num_list=[]
num_list.append(r"'0'")
num_list.append(r"'1'")
num_list.append(r"'2'")
num_list.append(r"'3'")
num_list.append(r"'4'")
num_list.append(r"'5'")
num_list.append(r"'6'")
num_list.append(r"'7'")
num_list.append(r"'8'")
num_list.append(r"'9'")

for st_col in color_list:
	for st_num in num_list:
		space=", "
		st1=st_col + space + st_num
		st2=st_num + space + st_col
		l_in1 = [s for s in txtlist if st1 in s]
		l_in2 = [s for s in txtlist if st2 in s]
		print("Searching word = " + st1)
		print(l_in1)
		print("Searching word = " + st2)
		print(l_in2)

az_list=[]
az_list.append(r"'a'")
az_list.append(r"'b'")
az_list.append(r"'c'")
az_list.append(r"'d'")
az_list.append(r"'e'")
az_list.append(r"'f'")
az_list.append(r"'g'")
az_list.append(r"'h'")
az_list.append(r"'i'")
az_list.append(r"'j'")
az_list.append(r"'k'")
az_list.append(r"'l'")
az_list.append(r"'m'")
az_list.append(r"'n'")
az_list.append(r"'o'")
az_list.append(r"'p'")
az_list.append(r"'q'")
az_list.append(r"'r'")
az_list.append(r"'s'")
az_list.append(r"'t'")
az_list.append(r"'u'")
az_list.append(r"'v'")
az_list.append(r"'w'")
az_list.append(r"'x'")
az_list.append(r"'y'")
az_list.append(r"'z'")

for st_col in color_list:
	for st_az in az_list:
		space=", "
		st1=st_col + space + st_az
		st2=st_az + space + st_col
		l_in1 = [s for s in txtlist if st1 in s]
		l_in2 = [s for s in txtlist if st2 in s]
		print("Searching word = " + st1)
		print(l_in1)
		print("Searching word = " + st2)
		print(l_in2)
