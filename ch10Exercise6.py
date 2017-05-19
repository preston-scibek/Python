dictt = {}
times = 0
q = open('clothes.txt', 'w')
q.write('hi')
q.close()
f = open('clothes.txt', 'r')
print f
import json
#old_d = json.load(f)
old_d ={}
x = json.dumps('{1:{1:1}}')
print x
key = raw_input('What shirt')
key_v2 = raw_input('What color')
times = times + 1
old_d[str(key)] = {}
old_d[str(key)][str(key_v2)] = times
print old_d