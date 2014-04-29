#!/usr/bin/python

# -*- coding: utf-8 -*-


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
	r1 = {'B':'&', 'A':'#', 'C':'@','D':'~','E':'2','F':'\\','G':'/','H':'o','I':'!','J':'*','K':'1','L':'^','M':'6','N':'X','O':'=','P':'u','Q':'c','R':'3','S':'0','T':']','U':'v','V':'/','W':'#','X':'(','Y':'r','Z':'i',}
	#round2
	r2 = {'&':'I','#':'e','@':'q','~':'f','2':'A','\\':'H','/':'c','o':'0','!':'%','*':'S','1':'4','b':'^','6':'-','X':'R','=':'s','u':'K','c':'G','3':'a','0':'L',']':'|','v':'Y','/':'E','#':'e','(':'Q','b':'K','i':'y',}
	#round3
	r3 = {'e':'u','I':'i','q':'7','f':'1','A':'!','H':'Q','c':'3','0':'X','%':'M','S':'B','4':')','b':'N','-':'/','R':'g','s':'J','K':';','G':'p','a':'}','L':'$','|':'>','Y':'H','E':'p','e':'_','Q':'^','K':']','y':'u',}
	#round4
	r4 = {'u':'&','i':'\\','7':'V','1':'A','!':'Z','Q':'%','3':'b','X':'C','M':'+','B':'T',')':'2','N':'z','/':'Y','g':'|','J':'P',';':'.','l':'n','}':':','$':'r','>':'c','H':'5','p':'8','_':'{','^':'W',']':'L','u':'F'}
	#round5
	r5 = {'&':'1','\\':'}','V':'e','A':'#','Z':'C','%':'<','b':'@','C':'B','+':']','T':'7','2':'$','z':'F','Y':'Q','|':'i','P':'?','.':'.','n':'D',':':'@','r':'*','c':'>','5':'6','8':',','{':'n','W':'S','L':'G','F':'!'}
#
# 					!end cipher block!
#
#	
	state = "/m"
	clear_screen()
	v.version()
	

	while loop == True:

		if state == "/m":
			clear_screen()
			v.version()
			print """    Type /d for Decrypter
         /q to quit \n\n\n\n"""
			my_text = raw_input("[] Text to Cipher  >>> ")
			if my_text == "/q" or my_text == "/d":
				state = my_text
				continue

			#print rev
			my_text = my_text.upper()
		# menu isnt working atm, needs some work :(	
		#if my_text == "/m":
			#menu_options()
#
#  pipe the text into the next round
#
#
#  anything after round 1 is precipher
# usage         replace(precipher text, round)
			catch1 = replace_all(my_text, r1)
			catch2 = replace_all(catch1, r2)
			catch3 = replace_all(catch2, r3)
			catch4 = replace_all(catch3, r4)
			catch5 = replace_all(catch4, r5)
			txt = replace_all(catch1,r2,r3,r4,r5)
			# decrypt function, does not work yet ;_;
			txt2 = replace_all(catch5,r4,r3,r2,r1)
	#debug script removes the previous title, to give more space
	#os.system('cls')
	#		#
			# decrypt does not work...
			#print "decrypted", txt2
	#		print """
	#Crypting >>>   %s   <<<""" % (my_text)
			print """ \n
------------------------------------------------------------------------
[ * ] Round 1: %s
	
[ * ] Round 2: %s

[ * ] Round 3: %s

[DBG] Round 4: %s

[ * ] Round 5: %s
------------------------------------------------------------------------\n\n\n\n
	------------------------------------------------------------
	| Result: %s\n                                             
	------------------------------------------------------------ \n\n""" % (catch1,catch2,catch3,catch4,catch5,txt)
			raw_input("(Enter to clear)")

		elif state == "/d":
			clear_screen()
			print """
******************************************
*               Decrpytion               *
*      (/m to return to Encryption)      *
******************************************
"""
			decrypt = raw_input("[]	Decrypting >>>")
			if decrypt == "/m":
				state = decrypt
				continue

			decrever = decrypt[::-1]
			f1 = dict(zip(r1.values(),r1.keys()))
			f2 = dict(zip(r2.values(),r2.keys()))
			f3 = dict(zip(r3.values(),r3.keys()))
			f4 = dict(zip(r4.values(),r4.keys()))
			f5 = dict(zip(r5.values(),r5.keys()))
			decrever = replace_all(decrever, f5,f4,f3,f2,f1)
			decrypt = decrever[::-1]
			print """
|Original Text -> %s

""" % (decrypt)
			raw_input("(Enter to clear)")
		
		elif state == "/q":
			clear_screen()
			loop = False


if __name__ == "__main__":
	main()
