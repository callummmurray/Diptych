#this version contains work on rests, and there is also no decision made about held notes in part II.


import randomdotorg
import random
import urllib
import urllib2
import threading       
_LOCK = threading.Lock() 

r = randomdotorg.RandomDotOrg('calmur8@gmail.com')
r.get_quota()

print r.get_quota()

d_mode = ('D','D','E','E','F#','G','G','A','A','B','B','C#') #notes doubled so they appear more often
a_mode = ('A','A','B','B','C#','D','D','E','E','F#','F#','G#')
eb_mode = ('Eb','Eb','F','F','G','G','Ab','Bb','Bb','C','C','D')
bb_mode = ('Bb','Bb','C','C','D','D','Eb','F','F','G','G','A',)

rest_probability = r.randint(1,4) #lengths of rests
if rest_probability == 1:
	rest = r.randint(4,16)
if rest_probability	== 1:
	rest = r.randint(4,16)
if rest_probability == 3:
	rest = r.randint(4,16)
if rest_probability == 4:
	rest = r.randint(4,24)

v1_num = r.randint(10,30) #violin 1
v2_num = r.randint(10,30) #violin 2
va_num = r.randint(10,30) #viola
vc_num = r.randint(10,30) #cello

# print '\n'
# print 'PART I \n' #PART I

c = 5 #number of cycles of ALL FOUR tonalities (should be a nultiple of 4 because of part II)
phrase_num = 1

for x in range(c): 
	print 'phrase ',phrase_num,' D major' #D major
	print 'v1 num',v1_num,' v2 num',v2_num,' va num',va_num,' vc num',vc_num,'\n'
	i = 0
	while i < v1_num:
		print 'v1 ',r.choice(d_mode)
		i += 1
	i = 0
	while i < v2_num:
		print 'v2 ',r.choice(d_mode)	
		i += 1 
	i = 0
	while i < va_num:
		print 'va ',r.choice(d_mode)
		i += 1
	i = 0	
	while i < vc_num:
		print 'vc ',r.choice(d_mode)	
		i += 1
	v1_num = r.randint(10,30) #violin 1
	v2_num = r.randint(10,30) #violin 2
	va_num = r.randint(10,30) #viola
	vc_num = r.randint(10,30) #cello

	align = r.randint(1,2)
	if align == 1:
		print '\nalign: start'
	if align == 2:
		print '\nalign: end'	

	rest_probability = r.randint(1,4) #lengths of rests
	if rest_probability == 1:
		rest = r.randint(4,16)
	if rest_probability	== 1:
		rest = r.randint(4,16)
	if rest_probability == 3:
		rest = r.randint(4,16)
	if rest_probability == 4:
		rest = r.randint(4,24)

	print 'rest ',rest,'\n'	

	phrase_num += 1

	print 'phrase ',phrase_num,' A major' #A major
	print 'v1 num',v1_num,' v2 num',v2_num,' va num',va_num,' vc num',vc_num,'\n'
	i = 0
	while i < v1_num:
		print 'v1 ',r.choice(a_mode)
		i += 1
	i = 0
	while i < v2_num:
		print 'v2 ',r.choice(a_mode)	
		i += 1 
	i = 0
	while i < va_num:
		print 'va ',r.choice(a_mode)
		i += 1
	i = 0	
	while i < vc_num:
		print 'vc ',r.choice(a_mode)	
		i += 1					
	v1_num = r.randint(10,30) #violin 1
	v2_num = r.randint(10,30) #violin 2
	va_num = r.randint(10,30) #viola
	vc_num = r.randint(10,30) #cello

	align = r.randint(1,2)
	if align == 1:
		print '\nalign: start'
	if align == 2:
		print '\nalign: end'	

	rest_probability = r.randint(1,4) #lengths of rests
	if rest_probability == 1:
		rest = r.randint(4,16)
	if rest_probability	== 1:
		rest = r.randint(4,16)
	if rest_probability == 3:
		rest = r.randint(4,16)
	if rest_probability == 4:
		rest = r.randint(4,24)

	print 'rest ',rest,'\n'	

	phrase_num += 1	

	print 'phrase ',phrase_num,' Eb major\n' #Eb major
	print 'v1 num',v1_num,' v2 num',v2_num,' va num',va_num,' vc num',vc_num,'\n'
	i = 0
	while i < v1_num:
		print 'v1 ',r.choice(eb_mode)
		i += 1
	i = 0
	while i < v2_num:
		print 'v2 ',r.choice(eb_mode)	
		i += 1 
	i = 0
	while i < va_num:
		print 'va ',r.choice(eb_mode)
		i += 1
	i = 0	
	while i < vc_num:
		print 'vc ',r.choice(eb_mode)	
		i += 1
	v1_num = r.randint(10,30) #violin 1
	v2_num = r.randint(10,30) #violin 2
	va_num = r.randint(10,30) #viola
	vc_num = r.randint(10,30) #cello

	align = r.randint(1,2)
	if align == 1:
		print '\nalign: start'
	if align == 2:
		print '\nalign: end'		

	rest_probability = r.randint(1,4) #lengths of rests
	if rest_probability == 1:
		rest = r.randint(4,16)
	if rest_probability	== 1:
		rest = r.randint(4,16)
	if rest_probability == 3:
		rest = r.randint(4,16)
	if rest_probability == 4:
		rest = r.randint(4,24)

	print 'rest ',rest,'\n'

	phrase_num += 1	

	print 'phrase ',phrase_num,' Bb major\n' #Bb major
	print 'v1 num',v1_num,' v2 num',v2_num,' va num',va_num,' vc num',vc_num,'\n'
	i = 0
	while i < v1_num:
		print 'v1 ',r.choice(bb_mode)
		i += 1
	i = 0
	while i < v2_num:
		print 'v2 ',r.choice(bb_mode)	
		i += 1 
	i = 0
	while i < va_num:
		print 'va ',r.choice(bb_mode)
		i += 1
	i = 0	
	while i < vc_num:
		print 'vc ',r.choice(bb_mode)	
		i += 1
	v1_num = r.randint(10,30) #violin 1
	v2_num = r.randint(10,30) #violin 2
	va_num = r.randint(10,30) #viola
	vc_num = r.randint(10,30) #cello

	align = r.randint(1,2)
	if align == 1:
		print '\nalign: start'
	if align == 2:
		print '\nalign: end'

	rest_probability = r.randint(1,4) #lengths of rests
	if rest_probability == 1:
		rest = r.randint(4,16)
	if rest_probability	== 1:
		rest = r.randint(4,16)
	if rest_probability == 3:
		rest = r.randint(4,16)
	if rest_probability == 4:
		rest = r.randint(4,24)

	print 'rest ',rest,'\n'	

	phrase_num += 1				

print '\n'
print 'PART II \n' #PART II

v1_num = r.randint(10,30) #violin 1
v2_num = r.randint(10,30) #violin 2
va_num = r.randint(10,30) #viola
vc_num = r.randint(10,30) #cello	

phrase_num = 1

for x in range(c*4): #ACTUAL number of cycles 

	rand_mode_num = r.randint(1,4) #decides which mode to use

	if rand_mode_num == 1:
		rand_mode = r.choice(d_mode)
		rand_mode_title = 'D major'
	if rand_mode_num == 2:
		rand_mode = r.choice(a_mode)
		rand_mode_title = 'A major'
	if rand_mode_num == 3:
		rand_mode = r.choice(eb_mode)
		rand_mode_title = 'Eb major'
	if rand_mode_num == 4:
		rand_mode = r.choice(eb_mode)
		rand_mode_title = 'Bb major'	
	print 'phrase ',phrase_num,' ',rand_mode_title #title of the scale
	print 'v1 num',v1_num,' v2 num',v2_num,' va num',va_num,' vc num',vc_num,'\n'
	
	i = 0	
		
	while i < v1_num:
		if rand_mode_num == 1:
			rand_mode = r.choice(d_mode)
			rand_mode_title = 'D major'
		if rand_mode_num == 2:
			rand_mode = r.choice(a_mode)
			rand_mode_title = 'A major'
		if rand_mode_num == 3:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Eb major'
		if rand_mode_num == 4:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Bb major'
		print 'v1 ',rand_mode	
		i += 1

	i = 0

	while i < v2_num:
		if rand_mode_num == 1:
			rand_mode = r.choice(d_mode)
			rand_mode_title = 'D major'
		if rand_mode_num == 2:
			rand_mode = r.choice(a_mode)
			rand_mode_title = 'A major'
		if rand_mode_num == 3:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Eb major'
		if rand_mode_num == 4:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Bb major'
		print 'v2 ',rand_mode					
		i += 1

	i = 0

	while i < va_num:
		if rand_mode_num == 1:
			rand_mode = r.choice(d_mode)
			rand_mode_title = 'D major'
		if rand_mode_num == 2:
			rand_mode = r.choice(a_mode)
			rand_mode_title = 'A major'
		if rand_mode_num == 3:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Eb major'
		if rand_mode_num == 4:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Bb major'
		print 'va ',rand_mode			
		i += 1

	i = 0		

	while i < vc_num:	
		if rand_mode_num == 1:
			rand_mode = r.choice(d_mode)
			rand_mode_title = 'D major'
		if rand_mode_num == 2:
			rand_mode = r.choice(a_mode)
			rand_mode_title = 'A major'
		if rand_mode_num == 3:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Eb major'
		if rand_mode_num == 4:
			rand_mode = r.choice(eb_mode)
			rand_mode_title = 'Bb major'
		print 'vc ',rand_mode	
		i += 1	

		v1_num = r.randint(10,30) #violin 1
		v2_num = r.randint(10,30) #violin 2
		va_num = r.randint(10,30) #viola
		vc_num = r.randint(10,30) #cello

	align = r.randint(1,2)
	if align == 1:
		print '\nalign: start'
	if align == 2:
		print '\nalign: end'			

	rest_probability = r.randint(1,4) #lengths of rests
	if rest_probability == 1:
		rest = r.randint(4,16)
	if rest_probability	== 1:
		rest = r.randint(4,16)
	if rest_probability == 3:
		rest = r.randint(4,16)
	if rest_probability == 4:
		rest = r.randint(4,24)

	print 'rest ',rest,'\n'

	held = ['v1','v2','va','vc']
	h_texture = r.choice(held,2)
	print 'held notes: ',h_texture

	phrase_num += 1












