# python3 gram_count_uni.py
# python3 gram_count_uni.py > data_ugs_color.txt

#f = open('log_bgs_wiki103.txt')
#f = open('freq_bgs.txt')
f = open('freq_ugs.txt')
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

for st in color_list:
	l_in = [s for s in txtlist if st in s]
	print("Searching word = " + st)
	print(l_in)
