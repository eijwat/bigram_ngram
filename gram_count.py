# August 2022

# python3 gram_count.py
# python3 gram_count.py > data_tgs_color.txt
# python3 gram_count.py > data_bgs_color.txt
# python3 gram_count.py > data_5gs_color.txt

import re

#f = open('freq_tgs.txt')
f = open('freq_5gs.txt')
#f = open('freq_bgs.txt')

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

numa_list=[]
numa_list.append(r"'zero'")
numa_list.append(r"'one'")
numa_list.append(r"'two'")
numa_list.append(r"'three'")
numa_list.append(r"'four'")
numa_list.append(r"'five'")
numa_list.append(r"'six'")
numa_list.append(r"'seven'")
numa_list.append(r"'eight'")
numa_list.append(r"'nine'")

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

for st1 in color_list:
	l_in1 = []
	l_in1 = [s for s in txtlist if st1 in s]
	for st2 in az_list:
		l_in2 = []
		l_in2 = [s for s in l_in1 if st2 in s]
		print("Searching word = " + st1 + "and" + st2)
		#print(l_in2)
		t=0
		for st3 in l_in2:
			t=t+int(re.findall('[0-9]+$', st3)[0])
		print(t)

for st1 in color_list:
	l_in1 = []
	l_in1 = [s for s in txtlist if st1 in s]
	for st2 in num_list:
		l_in2 = []
		l_in2 = [s for s in l_in1 if st2 in s]
		print("Searching word = " + st1 + "and" + st2)
		#print(l_in2)
		t=0
		for st3 in l_in2:
			t=t+int(re.findall('[0-9]+$', st3)[0])
		print(t)

for st1 in color_list:
	l_in1 = []
	l_in1 = [s for s in txtlist if st1 in s]
	for st2 in numa_list:
		l_in2 = []
		l_in2 = [s for s in l_in1 if st2 in s]
		print("Searching word = " + st1 + "and" + st2)
		#print(l_in2)
		t=0
		for st3 in l_in2:
			t=t+int(re.findall('[0-9]+$', st3)[0])
		print(t)
