import json
#f = open('fornick.txt', 'r')
#dictt = {}
#times = 0
key_v1 = raw_input("What shirt: ")
key_v2 = raw_input("what color: ")
#dictt[str(key_v1)] = {}
#dictt[str(key_v1)][str(key_v2)] = times+1
f = open('fornick.json', 'r')
x = json.load(f)
f.close()
print x
inkey = False
inkeykey = False
for key in x.keys():
	print str(key)
	print str(key_v1)
	if str(key) == str(key_v1):
		inkey = True
		for keyss in x[key].keys():
			if str(keyss) == str(key_v2):
				inkeykey = True
				x[key][keyss] = x[key][keyss] + 1
				break
			else:
				continue
		if inkeykey == False:
			x[key][key_v2] = 1
	else:
		continue
if inkey == False:
	x[key_v1] = {}
	x[key_v1][key_v2] = 1
print x
		
f = open('fornick.json', 'w')
json.dump(x, f)
f.close()
