import irclib
import feedparser
import re
import random
import time
from time import strftime

print """
####################################################
# Python IRC bot named Kell		  
# By phezord			 			  
# email : sphreaz@gmail.com / strahinja@linux.rs
# Web : http://nix2.me  http://linux.rs
# Greetz : lugoNS , and mindfreaks.org staff
##################################################### """




# Informacije za konekciju
me='sphreaz'
network ="irc.freenode.net"
server=network
port = 6667
channel ="#linuxxas"
nick = 'k3ll'
name = 'm1nd3_bot'
cs='ChanServ'


#Ostale promenjive

odgovor=['Da','Ne','Mozda','Nego sta nego jeste', 'Ma de to' , 'To da pitas mamu ','Hmmm..','A jel ti pusis ladan kurac ? ' , 'Pazi da ti ne kazem' , ' Sinko ja sam ti otac ' ]

slaps=['Kell udara  ' , 'Kell slaps ' ,'Kell fucks up ', 'Kell gadja ']
afts=[' odgromnim cekicem' , ' gumenom patkicom', ' techovom carapom' , ' sa kiselim kupusom']

brg=0
pozit=0
negat=0

def makedict(**kwargs):
    return kwargs

color = makedict(white="\0030", black="\0031", blue="\0032", red="\0034",
dred="\0035", purple="\0036", dyellow="\0037", yellow="\0038", bgreen="\0039", dgreen="\00310", green="\00311", bpurple="\00313", dgrey="\00314", lgrey="\00315", close="\003", bold="\002")





# Definisanje hendlera
def handleJoin ( connection, event ):

 
   print event.source().split ( '!' ) [ 0 ] + ' has joined ' + event.target()
   
def handleInvite ( connection, event ):

   connection.join ( event.arguments() [ 0 ] )
   
def handlePrivMessage ( connection, event ):

   print event.target() + '> ' + event.arguments() [ 0 ]

   if event.arguments() [ 0 ].lower().find ( 'hello' ) == 0:
      connection.privmsg ( event.source().split ( '!' ) [ 0 ],'Hello.' )
def handlePubMessage (connection, event ):
	print event.target() + '> ' + event.source().split ( '!' ) [ 0 ] + ': ' + event.arguments() [ 0 ]
	

	# Dodatne varijable
	tk=event.target() #trenutni kanal
	to=event.source().split ( '!' ) [ 0 ] #trenutna osoba


#------------------------------Pocetak bota.------------------------------------



	#Dodana funkcija cuvanja logova u text fajlu log.txt
	#f.write(event.target() + '> ' + event.source().split ( '!' ) [ 0 ] + ': ' + event.arguments() [ 0 ])
	#f.write("\n" )
	
	#Random odgovor na pitanje koje prethodi 'kell' 
	if event.arguments() [0].lower().find( 'kell' ) == 0:
		connection.privmsg(tk, random.choice(odgovor))
	
	#Odgovor na pitanje vlasnika	
	if event.arguments() [0].lower().find( '@owner' ) == 0:
		connection.privmsg(tk, 'My master is sphreaz , his email is : sphreaz@gmail.com')


##---------------------Kanal regulatorne funkcije-----------------------------
		
	
	# Funkcija ulaska na kanal

	if event.arguments() [0].lower().find( '@join' ) == 0:
		tekst=event.arguments() [0].lower()
		server.join(tekst.split(' ',1)[1])

	# Funkcija napustanja kanala

	if event.arguments() [0].lower().find( '@part' ) == 0:
		tekst=event.arguments() [0].lower()
		kanal=tekst[5:]
		if len(kanal)>1 and kanal[0:1]==' ':
			server.part(kanal.split(' ',1)[1])
		elif len(kanal)==0:
			server.part(tk)
		else:
			connection.privmsg(tk, 'Greska u komandi!')
	
	#dodatak za proveru licnosti

	if event.arguments() [0].lower().find( '@kosam' ) == 0:
			connection.privmsg(tk, to)


##------------ Operatorske funkcije ------------------------------------------
	
	
	#op i deop funkcije
	if event.arguments() [0].lower().find( '@op' ) == 0:
		tekst=event.arguments() [0].lower()
		opman=tekst[3:]
		if len(opman)>1 and opman[0:1]==' ':
			connection.mode(tk,'+o %s' % (opman[1:]))
		elif len(opman)==0:
			connection.mode(tk,'+o %s' % to)
		else:
			connection.privmsg(tk, 'Greska u komandi!')

	if event.arguments() [0].lower().find( '@deop' ) == 0:
		tekst=event.arguments() [0].lower()
		opman=tekst[5:]
		if len(opman)>1 and opman[0:1]==' ':
			connection.mode(tk,'-o %s' % (opman[1:]))
		elif len(opman)==0:
			connection.mode(tk,'-o %s' % to)
		else:
			connection.privmsg(tk, 'Greska u komandi!')

	#voice i devoice funkcije
	if event.arguments() [0].lower().find( '@voice' ) == 0:
		tekst=event.arguments() [0].lower()
		opman=tekst[6:]
		if len(opman)>1 and opman[0:1]==' ':
			connection.mode(tk,'+v %s' % (opman[1:]))
		elif len(opman)==0:
			connection.mode(tk,'+v %s' % to)
		else:
			connection.privmsg(tk, 'Greska u komandi!')

	if event.arguments() [0].lower().find( '@devoice' ) == 0:
		tekst=event.arguments() [0].lower()
		opman=tekst[8:]
		if len(opman)>1 and opman[0:1]==' ':
			connection.mode(tk,'-v %s' % (opman[1:]))
		elif len(opman)==0:
			connection.mode(tk,'-v %s' % to)
		else:
			connection.privmsg(tk, 'Greska u komandi!')



##------------------ Ostale funkcije -----------------------------------------

		
	# Slap funkcija omogucena
	if event.arguments() [0].lower().find( '@slap' ) == 0:
		sbody=event.arguments() [0].lower()
		sman=sbody[5:]
		if sman == "":
		 slaper = random.choice(slaps) + random.choice(afts)
		 connection.privmsg(tk,slaper)
		elif sman[0:1]!=' ':	
		 connection.privmsg(tk,'Greska u komandi!')
		else:
		 slaper = random.choice(slaps) +sbody.split(' ',1)[1] + random.choice(afts)
		 connection.privmsg(tk,slaper)
		 
	# RSS funkcija omogucena
	if event.arguments() [0].lower().find( '@rss' ) == 0:
		nov_url="http://rss.cnn.com/rss/edition_world.rss"
		feed = feedparser.parse( nov_url )
		for i in range(1,6):
			newestex = feed['items'][i].title
			link = feed['items'][i].link
			feedtext=color["bold"] + newestex+color["bold"]+' Link : '+link
			connection.privmsg(tk,feedtext)
			
	#gdesam
	if event.arguments() [0].lower().find( '@gdesam' ) == 0:
		connection.privmsg(tk,tk)

	# RSS funkcija omogucena Linux.Rs forum
	if event.arguments() [0].lower().find( '@forum' ) == 0:
		nov_url="http://www.linux.rs/forum/feed.php"
		feed = feedparser.parse( nov_url )
		for i in range(0,5):
			newestex = feed['items'][i].title
			link = feed['items'][i].link
			feedtext=color["bold"] + newestex+color["bold"]+' Link : '+link
			ftx=feedtext.encode("utf-8")
			connection.privmsg(tk,ftx)	
	# RSS funkcija omogucena Linux.Rs naslovna
	if event.arguments() [0].lower().find( '@vesti' ) == 0:
		nov_url="http://linux.rs/feed/"
		feed = feedparser.parse( nov_url )
		for i in range(0,5):
			newestex = feed.entries[i].title
			link = feed.entries[i].link
			feedtext=color["bold"] + newestex+color["bold"]+' Link : '+link
			ftx=feedtext.encode("utf-8")
			connection.privmsg(tk,ftx)	
			
		
 
# Kreiraj IRC objekat
irc = irclib.IRC()


irc.add_global_handler ( 'invite', handleInvite ) # Invite
irc.add_global_handler ( 'join', handleJoin ) # Channel join
irc.add_global_handler ( 'privmsg', handlePrivMessage )
irc.add_global_handler ( 'pubmsg', handlePubMessage )


# Konektujmo se 
server = irc.server()
server.connect ( network, port, nick, ircname = name )
server.join ( channel )
server.privmsg('NickServ','identify password')

# Poruka i kanalu i Vama
server.privmsg ( channel, '~Ja sam IRC bot, namenjem patroliranju kanalom linux.rs organizacije . Kreator bota je sphreaz . ( http://sphreaz.blogspot.com) . Pozdrav' )
server.privmsg ( me, 'Poruka za korisnika.' )
# Pokrenimo infinite loop da ne "pukne" bot
irc.process_forever()
