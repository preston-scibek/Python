import os
os.system('python get-pip.py')
try:
	os.chdir('C:\Python27\Scripts')
	os.system('cd C:\Python27\Scripts')
	os.system('pip install requests')
	os.system('pip install beautifulsoup4')
	os.system('pip install lxml')
except:
	os.system('cd C:\Python27\Scripts')
	os.system('pip install requests')
	os.system('pip install beautifulsoup4')
	os.system('pip install lxml')