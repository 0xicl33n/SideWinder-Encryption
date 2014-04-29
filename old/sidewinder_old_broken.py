#!/usr/bin/python
#
# SIDEWINDER ENCRYPTION ALGORITHM!
# EXTREMELY SIMPLE ;D
#
#!/usr/bin/python
print "#####################################"
print """
  ________________________/ O  \___/
 <_____________________________/   \ """
print "Sidewinder text encryption v2.0"
print ""
print "#####################################" 
#replace function
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
	my_text = input('something:')
	return text	

print my_text
	
#possible tuple use for character reference? o_O
#ascii = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+[]\,./;-')


#  using excel sheet to make sure all numbers are lined up right ^_^


#cipher1
r1 = {'E':'A', 'F':'B','G':'C','H':'F', 'I':'E', 'J':'F', 'K':'G', 'L':'H','M':'I','N':'J','O':'K','P':'L','Q':'M','R':'N','S':'O','T':'P','U':'Q','V':'R','W':'S','X':'T','Y':'U','V':'W','Z':'X','1':"Y",'2':'Z',}
#cipher2
# r2 = {''}
#cipher3
# r3 = {''}
#cipher4
# r4 = {''}
#cipher5
# r5 = {''}




#will be txt1

txt = replace_all(my_text, r1)
print 'Text before encrypt 1:', my_text
print txt


# it will be done like this:
# hash1 = txt1
#
# hash 2
# txt2 = replace_all(txt1, rep2)
#
# hash 3 
# txt3 = replace_all(txt2, rep3)
#
# hash 4
# txt4 = replace_all(txt3, rep4)
# 
# hash 5
#txt5 = replace_all(txt4,rep5)
#
# hash 5 will be the final one
#print txt5