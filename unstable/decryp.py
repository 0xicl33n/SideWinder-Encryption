
#!/usr/bin/python
#
# SIDEWINDER ENCRYPTION ALGORITHM!
v = 'RC 2.1'
#
# Compliments of ExploitOG & Zexanima
#
import os
import platform
def replace_all(text, *dic):
	for h in dic:
		for i, j in h.iteritems():
			text = text.replace(i, j)
	return text	

def main():
	#clear screen before begin
	platClear = platform.system()
	if platClear == "Linux":	
		os.system('clear')
	elif platClear == "Windows":
		os.system('cls')
		
	print ""
	print ""
	print """##########################################################################
           _
  _______/   \________________       _______/ O  \___/   
 <________/ \_____SideWinder__ \ _ / ____________/   \   %s
                              \ ___ / 

            single cipher demo release candidate
##########################################################################""" %(v)
	#cipher1 - needs numbers and symbols!
	r1 = {'A':'E', 'B':'F','C':'G','F':'F',
	 'I':'E', 'J':'F', 'K':'G', 'L':'H','M':'I','N':'J',
	 'O':'K','P':'L','Q':'M','R':'N','S':'O','T':'P','U':'Q',
	 'V':'R','W':'S','X':'T','Y':'U','V':'W','Z':'X','1':"Y",'2':'Z',}
	print ""
	print "please use caps"
	print ""
	my_text = raw_input("Text to cypher >>> ")
	print ""
	print ""
	txt = replace_all(my_text, r1)
	print "-------------------------------------------------------------------------"
	print "[ * ] Result:", txt
	print 
	print "-------------------------------------------------------------------------"
	print ""
	


if __name__ == "__main__":
	main()