__author__ = "Preston"
# This Python file uses the following encoding: utf-8
def function(dictt):
	for key in dictt.keys():
	if type(dictt[key]) == list:
		for item in dictt[key]:
			print key + ": " + item
	else:
		print key + ": " + str(dictt[key])
def make_google():
	to_be_google = '1'
	for i in range(100):
		to_be_google = to_be_google + '0'
	return int(to_be_google)
def make_googleplex():
	google = make_google()
	to_be_googleplex = '1'
	counter = 0
	while counter < google:
		to_be_googleplex = to_be_googleplex + '0'
		counter = counter + 1