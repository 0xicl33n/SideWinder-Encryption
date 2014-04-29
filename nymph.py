#!/usr/bin/env python
import os
import platform
version = '0.3'
def clear_screen():
	platClear = platform.system().lower()
	if platClear == "linux" or platClear == "unix":	
		os.system('clear')
	elif platClear == "windows":
		os.system('cls')
		os.system('title Nymph')
#rounds go here, you can easily add more, as i will
r1 = {'B':'&', 'A':'#', 'C':'@','D':'~','E':'2','F':'\\','G':'/','H':'o','I':'!','J':'*','K':'1','L':'^','M':'6','N':'X','O':'=','P':'u','Q':'c','R':'3','S':'0','T':']','U':'v','V':'/','W':'#','X':'(','Y':'r','Z':'i',}
#round2
r2 = {'&':'I','#':'e','@':'q','~':'f','2':'A','\\':'H','/':'c','o':'0','!':'%','*':'S','1':'4','^':'b','6':'-','X':'R','=':'s','u':'K','c':'G','3':'a','0':'L',']':'|','v':'Y','/':'E','#':'e','(':'Q','b':'K','i':'y','r':'['}

#this is the replace function, dont mess with it, or itll break 
def replace_all(text, *dic):
	for h in dic:
		for i, j in h.iteritems():
			text = text.replace(i, j)
	return text
clear_screen()	
print '''[*] Nymph: Multi-Wheel Algorithm Tester [*]\n
                          ____
                         ( o__|---<
                 ________/ / 
            ((((__________/\n
              Version: %s\n
'''%(version)
my_text = raw_input('[] Text >>> ' )
uptext = my_text.upper()
#catch works like this
# catch = replace(text, round)
catch1 = replace_all(uptext, r1)
catch2 = replace_all(catch1, r2)
# since im reworking sidewinder, im using 5 rounds
#catch3 = replace_all(catch2, r3)
#catch4 = replace_all(catch3, r4)
#catch5 = replace_all(catch4, r5)
#decryption still has not been perfected but it works the same way basically
# decrypt = replace(catch, round)
# if you have more then one round, it would be
# d1 = replace(catch, round)
# d2 = replace(catch, round2)
#where the final 'd' variable is the decrypted text
print '\n\n[*] Round 1:%s\n\n''[*] Round 2:%s'%(catch1,catch2)