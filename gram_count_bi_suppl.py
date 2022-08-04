# August 2022

# python3 gram_count_bi_suppl.py
# python3 gram_count_bi_suppl.py > data_bgs_color_suppl.txt

f = open('freq_bgs.txt')
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
num_list.append(r"'zero'")
num_list.append(r"'one'")
num_list.append(r"'two'")
num_list.append(r"'three'")
num_list.append(r"'four'")
num_list.append(r"'five'")
num_list.append(r"'six'")
num_list.append(r"'seven'")
num_list.append(r"'eight'")
num_list.append(r"'nine'")

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
