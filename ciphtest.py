r1 = {'B':'&', 'A':'#', 'C':'@','D':'~','E':'2','F':'\\','G':'/','H':'o','I':'!','J':'*','K':'1','L':'^','M':'6','N':'X','O':'=','P':'u','Q':'c','R':'3','S':'0','T':']','U':'v','V':'/','W':'#','X':'(','Y':'r','Z':'i',}
#round2
r2 = {'&':'I','#':'e','@':'q','~':'f','2':'A','\\':'H','/':'c','o':'0','!':'%','*':'S','1':'4','^':'b','6':'-','X':'R','=':'s','u':'K','c':'G','3':'a','0':'L',']':'|','v':'Y','/':'E','#':'e','(':'Q','b':'K','i':'y',}
def replace_all(text, *dic):
	for h in dic:
		for i, j in h.iteritems():
			text = text.replace(i, j)
	return text
print '''[*] Nymph: Cipher test System\n
               	   ____
        		  ( o__|---<
  	      ________/ / 
		<__________/\n\n
'''
my_text = raw_input('text>> ' )
catch1 = replace_all(my_text, r1)
catch2 = replace_all(catch1, r2)
print 'Round 1:',catch1,'\n','Round 2:',catch2