#!/usr/bin/python
#
# SIDEWINDER ENCRYPTION ALGORITHM!
# not so simple anymore ._.
#
# Compliments of 0xicl33n & Zexanima
#
#
#
# personal note on revision
#rev = "revision 4"
#
import os
import platform
import v
#
#
#replace fucntion
def replace_all(text, *dic):
	for h in dic:
		for i, j in h.iteritems():
			text = text.replace(i, j)
	return text	

#clear screen before begin
def clear_screen():
	platClear = platform.system().lower()
	if platClear == "linux" or platClear == "unix":	
		os.system('clear')
	elif platClear == "windows":
		os.system('cls')
		os.system('title SideWinder')
#non working menu
def menu_options():
    print "Menu:"
    print "  /e to to encrypt text as normal"
    print "  /d to decrypt text"
    print "  /dd for debug mode( view all rounds)"
    print "  /q  quit"

def main():
	loop = True
	print "\n\n"
#
# 
#	You probably dont want to modify this is if your working from source
# as this is still a work in progress, most of the cipher is coming from my brain
# and because of that, the cipher is not working properly.....yet.
#
# - 0xicl33n
#
# 				!begin cipher code block!
# 
#  cipher "wheels"
#
# currently A nd B work (lol)
	#round1 
	r1 = {'B':'&', 'A':'#', 'C':'@','D':'~',}
	#round2
	r2 = {'&':'I','#':'e','@':'q','~':'f',}
	#round3
	r3 = {'e':'F','I':'i','q':'7','f':'1',}
	#round4
	r4 = {'F':'&','i':'\\','7':'V','1':'A',}
	#round5
	r5 = {'&':'1','\\':'}','V':'e','A':'#',}
#
# 					!end cipher block!
#
# replace function
def replace():
	catch1 = replace_all(my_text, r1)
	catch2 = replace_all(catch1, r2)
	catch3 = replace_all(catch2, r3)
	catch4 = replace_all(catch3, r4)
	catch5 = replace_all(catch4, r5)
	txt = replace_all(catch1,r2,r3,r4,r5)
#
#	
	my_text = " "
	clear_screen()
	v.version()
	

	while loop:
		print """    Type /m for menu
         /q to quit \n\n\n\n"""
		my_text = raw_input("[] Text to Cipher  >>> ")
		if my_text == "/q":
			clear_screen()
			v.version()
			#print rev
			my_text = my_text.upper()
		 #menu isnt working atm, needs some work :(	
		if my_text == "/m":
			menu_options()
		if my_text == "/e":
			replace()
#	
#  pipe the text into the next round
#
#
#  anything after round 1 is precipher
# usage         replace(precipher text, round)
	
	#
	#debug script removes the previous title, to give more space
	#os.system('cls')
	#
			print """
	Crypting 		>>>   %s   <<<""" % (my_text)
			print """ \n
------------------------------------------------------------------------
[ * ] Round 1: %s                             
	
[ * ] Round 2: %s

[ * ] Round 3: %s

[ * ] Round 4: %s

[ * ] Round 5: %s
------------------------------------------------------------------------\n\n\n\n
Result: %s \n\n""" % (catch1,catch2,catch3,catch4,catch5,txt)
		else:
			clear_screen()
			loop = False


if __name__ == "__main__":
	main()