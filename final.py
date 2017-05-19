__author__ = "Preston Scibek"
#This Python file uses the following encoding: utf-8
"""python final project - Hangman
"""
import Tkinter
from Tkinter import *
import tkMessageBox
zz = ['']
hang_pictt = """
           ____________       {0}
           |          |     ____________
           {1}          |     |  Counter |
          {6}{2}{5}         |     |    {7}    |			  
          {3} {4}        |     |__________|
                      |     ____________
                      |     | High Score|
                    __|__   |    {8}     |
                            |___________|		
				   
	"""
multi_hang_pictt = """
           ____________       {0}
           |          |     ____________
           {1}          |     |     P1   |
          {6}{2}{5}         |     |    {7}    |			  
          {3} {4}        |     |__________|
                      |     ____________
                      |     |    P2     |
                    __|__   |    {8}     |
                            |___________|		
				   
	"""
def open_file(number=60):#function 1
	"""gets a random word from a word list """
	from datetime import datetime
	import time
	epoch_time = str(time.mktime(time.gmtime()))
	epoch_time = epoch_time[6:]
	cur_time = datetime.timetuple(datetime.now())
	fin = open('hangman.txt')
	listo = []
	for line in fin:
		listo.append(line.strip())
	length = len(listo)
	for i in range(10):
		number = number * cur_time[3]
	number = ((cur_time[7] + (((cur_time[0])/(cur_time[1]*cur_time[2])) + number) * (cur_time[5]) + cur_time[6])) / int(float(epoch_time))
	while number > length:
		number = number - length
	return listo[number]#return value
def user_word(gui=False):#function 2
	if gui:
		x = Tkinter.Tk()
		letter_var = Tkinter.StringVar()
		letters = Tkinter.Entry(x, textvariable = letter_var,show='*')
		def callback(event):#function 10
			global zz
			zz[0] = letters.get()
			x.quit()
			return x.destroy()
		letters.bind("<Return>", callback)
		letters.pack()
		get_letter = Tkinter.Button(x, text ="submit", command =lambda: callback(None))
		get_letter.bind("<Return>", callback)
		get_letter.pack()
		x.mainloop()
		user_word = zz[0]
		return user_word#return value
	else:
		import getpass
		""" gets users input for its own word"""
		chosen_word = getpass.getpass("Enter your word or phrase: ")
		chosen_word.replace(' ', '|')
		return chosen_word#return value
def print_hangman(word, hang_pict):#function 3
	""" Generates the initial hangman"""
	choice = [[], " ", " ", " ", "  ", " ", " ", "  ", "  ",]
	hang_pict = hang_pict + " "
	for i in range(len(word)):
		hang_pict = hang_pict + "{%s} " %str(i+9)
	hang_pict = hang_pict + "\n         "
	for indice, letter in enumerate(word):
		if letter == "|":
			hang_pict = hang_pict + "  "
			choice.append("|")
		else:
			hang_pict = hang_pict + "_ "
			choice.append(" ")
	hang_pict = hang_pict + " "
	print hang_pict.format(*choice)
	result = [hang_pict, choice]
	return result#return value
def guess_the_word(word,gui=False):#function 4
	if gui:
		x = Tkinter.Tk()
		letter_var = Tkinter.StringVar()
		letters = Tkinter.Entry(x, textvariable = letter_var)
		def callback(event):#function 11
			global zz
			zz[0] = letters.get()
			x.quit()
			return x.destroy()
		letters.bind("<Return>", callback)
		letters.pack()
		get_letter = Tkinter.Button(x, text ="submit", command =lambda: callback(None))
		get_letter.bind("<Return>", callback)
		get_letter.pack()
		x.mainloop()
		user_word = zz[0]
	else:
		user_word = raw_input("Enter your word: ")
	return user_word.lower() == word.lower()#return value
def guess_funct(word, hang_pict, choice,counter = 1, guess=0, hs = 0, players={'0':'0', '1':'0'}, player=-1, multi=False, hinted=False, gui=False, text = None,guii=None,rooot=False,root=None,intput=False):#function 5
	""" gets user input checks if letter in word builds hangman if not"""
	if multi==True:
		if len(str(counter)) == 2:
			players[str(player)] = str(counter)
		else:
			players[str(player)] = str(counter) + " "
		if len(str(players['0'])) == 2:
			choice[7] = str(players['0'])
		else:
			choice[7] = str(players['0']) + " "
		if len(str(int(players['1']))) == 2:
			choice[8] = str(int(players['1']))
		else:
			choice[8] = str(int(players['1'])) + " "
	else:
		if len(str(counter)) == 2:
			choice[7] = str(counter)
		else:
			choice[7] = str(counter) + " "
		if len(str(hs)) == 2:
			choice[8] = str(hs)
		else:
			choice[8] = str(hs) + " "
	global zz
	if gui:
		if intput:
			x = Tkinter.Tk()
			letter_var = Tkinter.StringVar()
			letters = Tkinter.Entry(x, textvariable = letter_var)
			def callback(event):#function 12
				global zz
				zz[0] = letters.get()
				x.quit()
				return x.destroy()
			letters.bind('<Return>', callback)
			letters.pack()
			get_letter = Tkinter.Button(x, text ="submit", command =lambda: callback(None))
			get_letter.bind("<Return>", callback)
			get_letter.pack()
			x.mainloop()
			letter = zz[0]
		else:
			if rooot==False:
				root = Tkinter.Tk()
				rooot = True
				a = Tkinter.Button(root, text='a', command=lambda: callback('a',a))
				b = Tkinter.Button(root, text='b', command=lambda: callback('b',b))
				c = Tkinter.Button(root, text='c', command=lambda: callback('c',c))
				d = Tkinter.Button(root, text='d', command=lambda: callback('d',d))
				e = Tkinter.Button(root, text='e', command=lambda: callback('e',e))
				f = Tkinter.Button(root, text='f', command=lambda: callback('f',f))
				g = Tkinter.Button(root, text='g', command=lambda: callback('g',g))
				h = Tkinter.Button(root, text='h', command=lambda: callback('h',h))
				i = Tkinter.Button(root, text='i', command=lambda: callback('i',i))
				j = Tkinter.Button(root, text='j', command=lambda: callback('j',j))
				k = Tkinter.Button(root, text='k', command=lambda: callback('k',k))
				l = Tkinter.Button(root, text='l', command=lambda: callback('l',l))
				m = Tkinter.Button(root, text='m', command=lambda: callback('m',m))
				n = Tkinter.Button(root, text='n', command=lambda: callback('n',n))
				o = Tkinter.Button(root, text='o', command=lambda: callback('o',o))
				p = Tkinter.Button(root, text='p', command=lambda: callback('p',p))
				q = Tkinter.Button(root, text='q', command=lambda: callback('q',q))
				r = Tkinter.Button(root, text='r', command=lambda: callback('r',r))
				s = Tkinter.Button(root, text='s', command=lambda: callback('s',s))
				t = Tkinter.Button(root, text='t', command=lambda: callback('t',t))
				u = Tkinter.Button(root, text='u', command=lambda: callback('u',u))
				v = Tkinter.Button(root, text='v', command=lambda: callback('v',v))
				w = Tkinter.Button(root, text='w', command=lambda: callback('w',w))
				x = Tkinter.Button(root, text='x', command=lambda: callback('x',x))
				y = Tkinter.Button(root, text='y', command=lambda: callback('y',y))
				z = Tkinter.Button(root, text='z', command=lambda: callback('z',z))
				hh = Tkinter.Button(root, text='hint', command=lambda: callback1())
				gg = Tkinter.Button(root, text='guess', command=lambda: callback2())
				a.pack()
				b.pack()
				c.pack()
				d.pack()
				e.pack()
				f.pack()
				g.pack()
				h.pack()
				i.pack()
				j.pack()
				k.pack()
				l.pack()
				m.pack()
				n.pack()
				o.pack()
				p.pack()
				q.pack()
				r.pack()
				s.pack()
				t.pack()
				u.pack()
				v.pack()
				w.pack()
				x.pack()
				y.pack()
				z.pack()
				hh.pack()
				gg.pack()
			else:
				root = root
			def callback(lettre,funct):#function 13
				global zz
				zz[0] = str(lettre)
				funct.forget()
				root.quit()
			def callback1():#function 14
				global zz
				zz[0] = 'hint'
				root.quit()
			def callback2():#function 15
				global zz
				zz[0] = 'guess'
				root.quit()
			root.mainloop()
			letter = zz[0]
	else:
		letter = raw_input("Guess a letter or type \"Guess\" to guess the word, or type \"Hint\" to get a hint: ")	
	in_word = False
	word_match = False
	if letter.lower() == "guess":
		if guess_the_word(word,gui=gui):
			for indice, char in enumerate(word):
				choice[indice+9] = char
			if gui==True:
				players[str(player)] = str(counter)
				text.delete('1.0', END)
				text.insert(INSERT, 'You win')
				players[str(player)] = str(counter)
				text.insert(INSERT, hang_pict.format(*choice))
				return [counter, player]
			else:
				print "You win"
				players[str(player)] = str(counter)
				print hang_pict.format(*choice)
				return [counter,players]
	if letter.lower() == "hint" and hinted == False:
		hint(word,guui=gui,texxt=text)
		return guess_funct(word, hang_pict, choice, counter=counter, guess=guess, player=player, multi=multi, hs = hs, players=players, hinted=True,gui=gui,text=text,guii=guii,rooot=rooot,root=root,intput=intput)#recursive function
	if letter.lower() == "hint" and hinted == True:
		hint(word,guui=gui,texxt=text)
		return guess_funct(word, hang_pict, choice, counter=counter+1, guess=guess, player=player, multi=multi, hs = hs, players=players, hinted=True,gui=gui,text=text,guii=guii,rooot=rooot,root=root,intput=intput)#recursive function
	else:
		for indice, char in enumerate(word):
			if letter == char:
				choice[indice+9] = letter
				in_word = True
				continue
		for indice, char in enumerate(word):
			if char == choice[indice+9]:
				word_match = True
				continue
			else:
				word_match = False
				break
		if word_match:
			players[str(player)] = str(counter)
			if multi:
				if gui == True:
					players[str(player)] = str(counter)
					text.delete('1.0', END)
					text.insert(INSERT, hang_pict.format(*choice))
				else:
					players[str(player)] = str(counter)
					print hang_pict.format(*choice)
				return [hs,players]
			if hs == 0:
				if gui==True:
					players[str(player)] = str(counter)
					text.delete('1.0', END)
					text.insert(INSERT, 'You Win')
					text.insert(INSERT, hang_pict.format(*choice))
				else:
					players[str(player)] = str(counter)
					print hang_pict.format(*choice)
				return [counter,players]
			if hs > counter:
				if gui==True:
					players[str(player)] = str(counter)
					text.delete('1.0', END)
					text.insert(INSERT, 'You Win')
					text.insert(INSERT, hang_pict.format(*choice))
				else:
					players[str(player)] = str(counter)
					print hang_pict.format(*choice)
				return [counter,players]
			if counter > hs:
				if gui==True:
					players[str(player)] = str(counter)
					text.delete('1.0', END)
					text.insert(INSERT, 'You Win')
					text.insert(INSERT, hang_pict.format(*choice))
				else:
					players[str(player)] = str(counter)
					print hang_pict.format(*choice)
				return [hs,players]
		if not in_word:
			choice[0].append(letter)
			guess += 1
		if guess == 1:
			choice[1] = "O"
		if guess == 2:
			choice[2] = "|"
		if guess == 3:
			choice[3] = "/"
		if guess == 4:
			choice[4] = "\\ "
		if guess == 5:
			choice[5] = "/"
		if guess == 6:
			choice[6] = "\\"
		if guess == 7:
			choice[1] = " "
			choice[4] = "\\O"
			if gui==True:
				text.insert(INSERT, "You lose")
				players[str(player)] = str(0)
				text.delete('1.0', END)
				text.insert(INSERT, hang_pict.format(*choice))
				text.insert(INSERT, "The word was ... %s" %word)
				return [hs,players]
			else:
				print "You lose"
				players[str(player)] = str(0)
				print hang_pict.format(*choice)
				print "The word was ... %s" %word
				return [hs,players]
		if gui == True:
			text.delete('1.0', END)
			text.insert(INSERT, hang_pict.format(*choice))
		else:
			print hang_pict.format(*choice)
		return guess_funct(word, hang_pict, choice, counter=counter+1, guess=guess, player=player, multi=multi, hs = hs, players=players, gui=gui,text=text,guii=guii,rooot=rooot,root=root,intput=intput)#recursive function
def calc_formula(word,counter):#function 6 
	""" made up formula to decide whose better at hangman based on word length and number of turns"""
	return len(word)-int(counter)#return value
def hintedd(word,guui=False,texxt=None):#function 7
	import lxml
	counter = 0
	import requests
	requests.packages.urllib3.disable_warnings()
	url = 'http://www.merriam-webster.com/dictionary/'+word
	r = requests.get(url)
	text = r.text.encode('ascii', 'ignore')
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(text, 'lxml')
	try:
		x = (soup.find('p', class_='bottom_entry'))
		if type(x) == type(None):
			raise Exception('nothingy')
	except:
		try:
			x = (soup.find('div', class_='scnt'))
			if type(x) == type(None):
				raise Exception('nothing')
		except:
			try:
				x = (soup.find('span', class_='ssens'))
				if type(x) == type(None):
					raise Exception('nothing')
			except:
				try: 
					x = soup.find('a', class_='ct-link sc')
					if type(x) == type(None):
						raise Exception('nothing')
				except:
					try:
						url = 'http://dictionary.reference.com/browse/'+word
						r = requests.get(url)
						text = r.text.encode('ascii', 'ignore')
						soup = BeautifulSoup(text, 'lxml')
						x = soup.find('div', class_='def-content')
						if type(x) == type(None):
							raise Exception('nothing')
					except:
						try:
							url = 'http://dictionary.webster.us/'+word
							r = requests.get(url)
							text = r.text.encode('ascii', 'ignore')
							soup = BeautifulSoup(text, 'lxml')
							x = soup.find('div', class_='parts')
							if type(x) == type(None):
								raise Exception('nothing')
							else:
								z = " "
								counter = 0
								for string in x.stripped_strings:
									if counter == 0:
										counter +=1
										continue
									if counter == 1:
										counter +=1
										z += 'A' + ' '
										continue
									else:
										counter +=1
										z += string +" "
									if gui:
										text.insert(INSERT, x.strip())
									else:
										print x.strip()
									return
						except:
							if type(x) == type(None):
								raise Exception('nothing')
	x = x.get_text()
	x = x.replace(u'\u2014', '--')
	x = x.encode('ascii', 'ignore')
	x = x.replace('&#8212;', '--')
	x = x.strip()
	if guui:
		print x
		texxt.insert(INSERT, "\n"+x)
	else:
		print x.strip()
def hint(word,guui=False,texxt=None):#function 8
	if word == 'aa':
		if guui:
			texxt.insert(INSERT, 'basaltic lava forming very rough jagged masses with a light frothy texture.')
		else:
			print 'basaltic lava forming very rough jagged masses with a light frothy texture.'
	if word == 'wastrie':
		if guui:
			texxt.insert(INSERT, 'waste')
		else:
			print 'waste'
	if word == 'hello world':
		if guui:
			texxt.insert(INSERT, 'beginner programming program')
		else:
			print 'beginner programming program'
	if word == 'abcdefghijklmnopqrstuvwxyz':
		if guui:
			texxt.insert(INSERT, 'zyxwvutsrqpomnlkjihgfedcba')
		else:
			print 'zyxwvutsrqpomnlkjihgfedcba'
	else:
		try:
			hintedd(word,guui=guui,texxt=texxt)
		except:
			try:
				hintedd(word[0:len(word)-1],guui=guui,texxt=texxt)
			except:
				f = open('errors.txt', 'a')
				f.write('\n' +word)
				print 'No hint available'
hs = ['0','0']
def gui(inputt):#function 9
	import Tkinter
	import tkMessageBox
	hanged = Tkinter.Tk()
	hanggged_pict = Tkinter.Text(hanged)
	hanggged_pict.pack()
	x = ''
	def callback(event):#functin 16
		use_wordm.forget()
		randm.forget()
		global hs
		players = {'0':'0', '1':'0'}
		words = ['','']
		words[0]=user_word(gui=True)
		words[1] = user_word(gui=True)
		for i in range(2):
			word = words[i]
			result = print_hangman(word, multi_hang_pictt)
			hang_pict = result[0]
			choice = result[1]
			hanggged_pict.delete('1.0', END)
			hanggged_pict.insert(INSERT, hang_pict)
			resultt = guess_funct(word, hang_pict, choice, hs = hs[0],multi=True,players=players,player=i, gui = True, text = hanggged_pict, guii=hanged,intput=inputt)
			players=resultt[1]
			hs[0] = str(players['0'])
			choice[7] = str(players['0'])
			choice[8] = str(players['1'])
			hanggged_pict.insert(INSERT,hang_pict.format(*choice))
		zzz = calc_formula(words[0],players['0'])
		zzzz = calc_formula(words[1],players['1'])
		if zzz > zzzz: 
			hanggged_pict.insert(INSERT, "Player 1 wins, congrats")
		if zzz < zzzz:
			hanggged_pict.insert(INSERT,"Player 2 wins, congrats")
		if zzz == zzzz:
			hanggged_pict.insert(INSERT,"Wow you guys tied")
		rematch.pack()
	def callbacks(event):#function 17
		global hs
		players = {'0':'0', '1':'0'}
		words = ['','']
		x = word_type.get()
		word = x
		result = print_hangman(word, hang_pictt)
		hang_pict = result[0]
		choice = result[1]
		hanggged_pict.insert(INSERT, hang_pict)
		hs = guess_funct(word, hang_pict, choice, hs = hs[0],players=players, gui = True, text = hanggged_pict,intput=inputt)
		hanggged_pict.insert(INSERT,hang_pict.format(*choice))
		rematch.pack()
	word_type= Tkinter.StringVar()
	wordss = Tkinter.Entry(hanged, textvariable = word_type, show='*')
	wordss.bind('<Return>', callback)
	wordsss = Tkinter.Entry(hanged, textvariable = word_type,show='*')
	wordsss.bind("<Return>", callbacks)
	def user_word_gui_s():#function 18
		use_words.pack_forget()
		rands.pack_forget()
		wordsss.pack()
		use_wrod_get.pack()
	def rand_word_gui_s():#function 19
		global hs
		players = {'0':'0', '1':'0'}
		words = ['','']
		use_words.pack_forget()
		rands.pack_forget()
		word = open_file()
		result = print_hangman(word, hang_pictt)
		hang_pict = result[0]
		choice = result[1]
		hanggged_pict.insert(INSERT, hang_pict)
		hs = guess_funct(word, hang_pict, choice, hs = hs[0],multi=False, gui = True, text = hanggged_pict,intput=inputt)
		hanggged_pict.insert(INSERT,hang_pict.format(*choice))
		rematch.pack()
	def rand_word_gui_m():#function 20
		use_wordm.forget()
		randm.forget()
		global hs
		players = {'0':'0', '1':'0'}
		words = ['','']
		for i in range(2):
			words[i] = open_file()
			word = words[i]
			result = print_hangman(word, multi_hang_pictt)
			hang_pict = result[0]
			choice = result[1]
			hanggged_pict.delete('1.0', END)
			hanggged_pict.insert(INSERT, hang_pict)
			resultt = guess_funct(word, hang_pict, choice, hs = hs[0],multi=True,players=players,player=i, gui = True, text = hanggged_pict, guii=hanged,intput=inputt)
			players=resultt[1]
			hs[0] = str(players['0'])
			hanggged_pict.insert(INSERT,hang_pict.format(*choice))
		choice[7] = str(players['0'])
		choice[8] = str(players['1'])
		zzz = calc_formula(words[0],players['0'])
		zzzz = calc_formula(words[1],players['1'])
		if zzz > zzzz: 
			hanggged_pict.insert(INSERT, "Player 1 wins, congrats")
		if zzz < zzzz:
			hanggged_pict.insert(INSERT,"Player 2 wins, congrats")
		if zzz == zzzz:
			hanggged_pict.insert(INSERT,"Wow you guys tied")
		rematch.pack()
	def multi():#function 21
		use_wordm.pack()
		hanggged_pict.insert(INSERT, '       ')
		hanggged_pict.delete('1.0', END)
		randm.pack()
		mult.pack_forget()
		sing.pack_forget()
	def single():#function 22
		use_words.pack()
		hanggged_pict.insert(INSERT, '       ')
		hanggged_pict.delete('1.0', END)
		rands.pack()
		mult.pack_forget()
		sing.pack_forget()
	def start():
		rematch.pack_forget()
		mult.pack()
		sing.pack()
	mult = Tkinter.Button(hanged, text ="Multiplayer", command = multi)
	sing = Tkinter.Button(hanged, text ="Single Player", command = single)
	rematch = Tkinter.Button(hanged, text='New Game', command = start)
	use_wordm = Tkinter.Button(hanged, text ="User Chooses Word", command =lambda:callback(None))
	rands = Tkinter.Button(hanged, text ="Random Word", command = rand_word_gui_s)
	use_words = Tkinter.Button(hanged, text ="User Chooses Word", command =  user_word_gui_s)
	randm = Tkinter.Button(hanged, text ="Random Word", command = rand_word_gui_m)
	use_wrod_get = Tkinter.Button(hanged, text ="submit",  command =lambda: callbacks(None))
	hanged.mainloop()
if __name__ == "__main__":#if else
	print "Type normal to use the terminal for hangman, Type gui to do a gui hangman."
	what_to_do = raw_input("What to do: ")#user input
	if what_to_do.lower() == 'gui':#if else
		print ("Do you want to click button for letter or type your letter?\n ")
		inputt = raw_input("Y(button)/N(type): ")#user input
		if inputt.lower() == 'y':#if else
			gui(False)
		else:#if else
			gui(True)
	if what_to_do.lower() == 'tester':#if else
		ltter = get_letter_gui()
		print ltter
		testttt()
	if what_to_do.lower() == 'test':#if else
		x = Tkinter.Tk()
		y = Tkinter.Text(x)
		y.pack()
		def callback():
			hintedd("falderal",guui = True, texxt = y)
		y.insert(INSERT,";l;;jl;kjfdas")
		f = Tkinter.Button(x, command=callback)
		f.pack()
		x.mainloop()
	if what_to_do.lower() == 'normal':#if else
		z = 1
		hs = [0,0]#list
		players = {'0':'0', '1':'0'}
		while z == 1:#while loop
			game_mode = raw_input("Multiplayer?: ")#user input
			if game_mode.lower() == 'yes' or game_mode.lower() == 'y' or game_mode.lower() == 'sure':#method string class
				words = ['','']
				word_type = raw_input("User chooses word?: ")#user input
				for i in range(2):#for loop
					if word_type.lower() == 'yes' or word_type.lower() == 'y' or word_type.lower() == 'sure':
						word=user_word()
					else:
						word=open_file()
					words[i] = (word)
					result = print_hangman(word, multi_hang_pictt)
					hang_pict = result[0]
					choice = result[1]
					resultt = guess_funct(word, hang_pict, choice, hs = hs[0], players = players, multi=True, player=i)
					players=resultt[1]
					hs[0] = players['0']
					print hang_pict.format(*choice)
				choice[7] = str(players['0'])
				choice[8] = str(players['1'])
				zzz = calc_formula(words[0],players['0'])
				zzzz = calc_formula(words[1],players['1'])
				if zzz > zzzz:#if else
					print "Player 1 wins, congrats"
				if zzz < zzzz:#if else
					print "Player 2 wins, congrats"
				if zzz == zzzz:#if else
					print "Wow you guys tied"
				rematch = raw_input("Play Again?")#user input
				if rematch.lower() == 'yes' or rematch.lower() == 'sure' or rematch.lower() == 'ok' or rematch.lower() == 'y':#if else
					continue
				else:#if else
					print "Either you said no or I couldn't understand your input. Goodbye."
					print "-----------------------------------------------------------------"
					z = 0
			else:#if else
				word_type = raw_input("User chooses word?: ")#user input
				if word_type.lower() == 'yes' or word_type.lower() == 'y' or word_type.lower() == 'sure':#if else
					word=user_word()
				else:#if else
					word=open_file()
				result = print_hangman(word, hang_pictt)
				hang_pict = result[0]
				choice = result[1]
				hs = guess_funct(word, hang_pict, choice, hs = hs[0])
				rematch = raw_input("Play Again?")#user input
				if rematch.lower() == 'yes' or rematch.lower() == 'sure' or rematch.lower() == 'ok' or rematch.lower() == 'y':#if else
					continue
				else:#if else
					print "Either you said no or I couldn't understand your input. Goodbye."
					print "-----------------------------------------------------------------"
					z = 0
