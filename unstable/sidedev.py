#!/usr/bin/python
#
#
# SIDEWINDER ENCRYPTION ALGORITHM!
# not so simple anymore ._.
#
# Compliments of 0xicl33n & Zexanima
#
#
#
import os
import platform
import v
import string
#
#
#
def replace_all(text, *dic):
	for h in dic:
		for i, j in h.iteritems():
			text = text.replace(i, j)
	return text	

def main():
	#clear screen before begin
	platClear = platform.system().lower()
	if platClear == "linux" or platClear == "unix":	
		os.system('clear')
	elif platClear == "windows":
		os.system('cls')
		os.system('title SideWinder')

	v.version()
#
# 
#	You probably dont want to modify this is if your working from source
# as this is still a work in progress, most of the cipher is coming from my brain
# and because of that, the cipher is not working properly.
#
# - 0xicl33n
#
# 				!begin cipher code block!
# 
#  cipher "wheels"
#
	#round1 - needs numbers and symbols, and A-D
	r1 = {'E':'A', 'F':'B','G':'C','H':'F',
	 'I':'E', 'J':'F', 'K':'G', 'L':'H','M':'I','N':'J',
	 'O':'K','P':'L','Q':'M','R':'N','S':'O','T':'P','U':'Q',
	 'V':'R','W':'S','X':'T','Y':'U','V':'W','Z':'X',}
	#round2
	r2 = {'A':'^',}
	#round3
	r3 = {'^':'Z',}
	#round4
	r4 = {'Z':'<'}
	#round5
	r5 = {'<':'#'}
#
# 					!end cipher block!
#
#
	my_text = raw_input("Text to cipher >>> ")
#
#  pipe the text into the next round
#
#  anything after round 1 is precipher text
#
# usage         replace(precipher text, round)
	catch1 = replace_all(my_text, r1)
	catch2 = replace_all(catch1, r2)
	catch3 = replace_all(catch2, r3)
	catch4 = replace_all(catch3, r4)
	catch5 = replace_all(catch4, r5)
	txt = replace_all(catch1,r2,r3,r4,r5)
	#
	#debug script removes the previous title, to give more space
	#os.system('cls')
	#
	if platClear == "linux" or platClear == "unix":	
		os.system('clear')
	elif platClear == "windows":
		os.system('cls')
		os.system('title SideWinder')
	v.version()


	#def displ(text):

	 #print """Encrypting the following\n>>>  %s  <<< \n\n""" % (my_text)
	 #text.format(align '^') 

print """
------------------------------------------------------------------------
[ * ] Round 1: %s                             
	
[ * ] Round 2: %s

[ * ] Round 3: %s

[ * ] Round 4: %s

[ * ] Round 5: %s
------------------------------------------------------------------------\n\n\n\n
Result: %s""" % (catch1,catch2,catch3,catch4,catch5,txt)


if __name__ == "__main__":
	main()