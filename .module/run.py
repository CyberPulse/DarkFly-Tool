#!/usr/bin/python
# author: Ms.ambari

import os
import sys
import random
import time
import re
import urllib2, urllib

def start():
	os.system('clear')
	print '\a#-------[ installing ]'
def done():
	print '\aDone!'
	d = raw_input('[*] Back or Exit [b/e] : >>> ')
	if d == 'b':
		os.system('DarkFly')
	elif d == 'e':
		print '\033[0;00m'
	else:
		print '\aSALAH NGENTOOTTTTT'
		time.sleep(0.8)
		os.system('DarkFly')

def sqlmap():
	start()
	os.system('git clone https://github.com/sqlmapproject/sqlmap && mv sqlmap $HOME')
	done()

def redhawk():
	start()
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK && mv RED_HAWK $HOME')
	done()

def dtect():
	start()
	os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT && mv D-TECT $HOME')
	done()

def litespam():
	start()
	os.system('git clone https://github.com/4L13199/LITESPAM.git && mv LITESPAM $HOME')
	done()

def hakku():
	start()
	os.system('git clone https://github.com/4shadoww/hakkuframework && mv hakkuframework $HOME')
	done()

def visql():
	start()
	os.system('git clone https://github.com/blackvkng/viSQL.Git && mv viSQL $HOME')
	done()

def atscan():
	start()
	os.system('git clone https://github.com/AlisamTechnology/ATSCAN.git && mv ATSCAN $HOME')
	done()

def hunner():
	start()
	os.system('git clone https://github.com/b3-v3r/Hunner.git && mv Hunner $HOME')
	done()

def weeman():
	start()
	os.system('git clone https://github.com/evait-security/weeman.git && mv weeman $HOME')
	done()

def hashbuster():
	start()
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster/ hash-b/ && mv hash-b $HOME')
	done()

def websploit():
	start()
	os.system('git clone https://github.com/The404Hacking/websploit.git && mv websploit $HOME')
	done()

def hatclound():
	start()
	os.system('git clone https://github.com/HatBashBR/HatCloud && mv HatCloud $HOME')
	done()

def brutal():
	start()
	os.system('git clone https://github.com/Screetsec/Brutal.git && mv Brutal $HOME')
	done()

def metasploit():
	start()
	os.system('curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
	done()

def xerxes():
	start()
	os.system('git clone https://github.com/zanyarjamal/xerxes.git && mv xerxes $HOME')
	done()

def hammer():
	start()
	os.system('git clone https://github.com/cyweb/hammer && mv hammer $HOME')
	done()

def hulk():
	start()
	os.system('git clone https://github.com/grafov/hulk.git && mv hulk $HOME')
	done()

def ilucky():
	os.system('python2 etc/__.py')
	done()

def pentmenu():
	start()
	os.system('git clone https://github.com/GinjaChris/pentmenu.git && mv pentmenu $HOME')
	done()

def torshammer():
	start()
	os.system('git clone https://github.com/dotfighter/torshammer.git && mv torshammer $HOME')
	done()

def goldeneye():
	start()
	os.system('git clone https://github.com/jseidl/GoldenEye.git && mv GoldenEye $HOME')
	done()

def katoolin():
	start()
	os.system('git clone https://github.com/LionSec/katoolin.git && mv katoolin $HOME')
	done()

def wpseku():
	start()
	os.system('git clone https://github.com/m4ll0k/WPSeku && mv WPSeku $HOME')
	done()

def inurlbr():
	start()
	os.system('git clone https://github.com/googleinurl/SCANNER-INURLBR && mv SCANNER-INURLBR $HOME')
	done()

def clonemaster():
	start()
	os.system('git clone https://github.com/Abdulraheem30042/Cl0neMast3r && mv Cl0neMast3r $HOME')
	done()

def pybelt():
	start()
	os.system('git clone https://github.com/Ekultek/Pybelt.git && mv Pybelt $HOME')
	done()

def wifite():
	start()
	os.system('git clone https://github.com/derv82/wifite && mv wifite $HOME')
	done()

def recondog():
	start()
	os.system('git clone https://github.com/UltimateHackers/ReconDog && mv ReconDog $HOME')
	done()

def mbf():
	start()
	os.system('git clone https://github.com/pirmansx/mbf && mv mbf $HOME')
	done()

def ipgeolocation():
  start()
  os.system('git clone https://github.com/maldevel/IPGeolocation')
  os.system('mv IPGeolocation $HOME')
  done()

def termuxsudo():
	start()
	os.system('git clone https://github.com/st42/termux-sudo && mv termux-sudo $HOME')
	done()

def instahack():
	start()
	os.system('git clone https://github.com/avramit/Instahack.git mv instahack $HOME')
	done()

def termuxubuntu():
	start()
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu.git && mv termux-ubuntu $HOME')
	done()

def nmap():
	start()
	os.system('apt-get install nmap -y')
	print 'done install nmap'
	print 'usage > nmap'
	done()

def arat():
	start()
	os.system('git clone https://github.com/Xi4u7/A-Rat.git && mv A-Rat $HOME')
	done()

def santet():
	start()
	os.system('git clone https://github.com/Gameye98/santet-online.git && mv santet-online $HOME')
	done()

def liteddos():
	start()
	os.system('git clone https://github.com/4L13199/LITEDDOS && mv LITEDDOS $HOME')
	done()

def googledork():
	start()
	os.system('git clone https://github.com/p5s4/dork && mv dork $HOME')
	done()

def adminfinder():
	os.system('python2 etc/af.py')
	start()

def gmailbrute():
	os.system('apt-get install hydra -y')
	os.system('clear')
	print '\a'
	email = raw_input('[+] enter the target email : ')
	passw = raw_input('[+] wordlist path : ')
	os.system('hydra -l %s -P %s -s 465 -S -v -V -t 1 smtp://smtp.gmail.com' % (email, passw,))
	done()

def cmsmap():
	start()
	os.system('git clone https://github.com/Dionach/CMSmap.git && mv CMSmap $HOME')
	done()

def instabot():
	start()
	os.system('git clone https://github.com/instagrambot/instabot/ igbot/ && mv igbot $HOME')
	done()

def thefatrat():
	start()
	os.system('git clone https://github.com/Screetsec/TheFatRat.git && mv TheFatRat $HOME')
	done()

def webdav():
	start()
	os.system('git clone https://github.com/amrelsadane123/exploit-WebDav-.git && mv exploit-WebDav- $HOME')
	done()

def netattack():
	start()
	os.system('git clone https://github.com/DDR1-404/netattack && mv netattack $HOME')
	done()

def netattackdua():
	start()
	os.system('git clone https://github.com/chrizator/netattack2.git && mv netattack2 $HOME')
	done()

def pybozocrack():
	start()
	os.system('git clone https://github.com/ikkebr/PyBozoCrack.git && mv PyBozoCrack $HOME')
	done()

def slowloris():
	start()
	os.system('git clone https://github.com/gkbrk/slowloris.git && mv slowloris $HOME')
	done()

def wem():
	os.system('apt-get install w3m -y')
	done()

def jembod():
	print "peler"
	time.sleep(2.0)
	os.system('python2 .ambari')

def yahoobrute():
	os.system('apt-get install hydra -y')
	os.system('clear')
	print '\a'
	yahoo = raw_inputa('[+] enter the target yahoo : ')
	passw = raw_input('[+] wordlist path : ')
	os.system('hydra -l %s -P %s -s 465 -S -v -V -t 1 smtp://smtp.mail.yahoo.com' % (yahoo, passw,))

def mailbrute():
	os.system('apt-get install hydra -y')
	os.system('clear')
	mail = raw_input('[+] mail : ')
	passw = raw_input('[+} wordlist path : ')
	os.system('hydra -l %s -P %s -s 587 -S -v -V -t 1 smtp://smtp.mail.com' % (mail, passw,))

def hotmail():
	os.system('apt-get install hydra -y')
	os.system('clear')
	hotmail = raw_input('[+] hotmail/email : ')
	passsw = raw_input('[+} wordlist path : ')
	os.system('hydra -l %s -P %s -s 587 -S -v -V -t 1 smtp://smtp.live.com' % (hotmail, passw,))

def nikto():
	start()
	os.system('git clone https://github.com/sullo/nikto && mv nikto $HOME')
	done()

def blackhydra():
	start()
	os.system('git clone https://github.com/Gameye98/Black-Hydra/ b-hydra/ && mv b-hydra $HOME')
	done()

def auxscan():
		start()
		os.system('git clone https://github.com/Gameye98/Auxscan2.0.git && mv Auxscan2.0 $HOME')
		done()

def xshell():
		start()
		os.system('git clone https://github.com/Ubaii/xshell && mv xshell $HOME')
		done()

def cupp():
		start()
		os.system('git clone https://github.com/Mebus/cupp && mv cupp $HOME')
		done()

def blackbox():
		start()
		os.system('git clone https://github.com/jothatron/blackbox.git && mv blackbox $HOME')
		done()

def kodork():
		os.system('python2 lib/dK.py')
		done()

def hostchecker():
		start()
		os.system('git clone https://github.com/pirmansx/hostchecker.git && mv hostchecker $HOME')
		done()

def fbbrute():
		os.system('python2 lib/stlib.py')
		done()

def wascan():
		start()
		os.system('git clone https://github.com/m4ll0k/WAScan/ wascan/ && mv wascan $HOME')
		done()

def oray():
		os.system('python2 lib/_0_.py')

def spamhooqtv():
		os.system('php lib/hac.php')

def spazsms():
		start()
		os.system('git clone https://github.com/Gameye98/SpazSMS && mv SpazSMS $HOME')
		done()

def wfdroid():
		start()
		os.system('git clone https://github.com/bytezcrew/wfdroid-termux.git && mv wfdroid-termux $HOME')
		done()

def ngrok():
		start()
		os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip && mv ngrok-stable-linux-arm.zip $HOME')
		done()

def wordpresbrute():
		start()
		os.system('git clone https://github.com/cyberscry/wpbf-perl.git && mv wpbf-perl $HOME')
		done()

def spyder():
		start()
		os.system('git clone https://github.com/Cvar1984/Spyder && mv Spyder $HOME')
		done()

def lokomedia():
		os.system('php lib/lokmed.php')

def vim():
		start()
		os.system('apt-get install vim -y')
		os.system('vim')

def fsociety():
		start()
		os.system('git clone https://github.com/Manisso/fsociety.git && mv fsociety $HOME')
		done()

def devploit():
		start()
		os.system('git clone https://github.com/joker25000/devploit && mv devploit $HOME')
		done()

def dirsearch():
		start()
		os.system('git clone https://github.com/maurosoria/dirsearch.git && mv dirsearch $HOME')
		done()

def toolsboxexploiter():
		start()
		os.system('git clone https://github.com/mrcakil/ToolsBox-Exploiter && mv ToolsBox-Exploiter $HOME')
		done()

def buemaho():
		start()
		os.system('git clone https://github.com/zenware/bluemaho.git && mv bluemaho $HOME')
		done()

def browsing():
		start()
		os.system('apt-get install lynx -y')
		print 'Done!'
		print 'usage > lynx example.com'
		done()

def botfbbangdjon():
		start()
		os.system('git clone https://github.com/Senitopeng/BotFbBangDjon.git && mv BotFbBangDjon $HOME')
		done()

def spammergrab():
		start()
		os.system('git clone http://github.com/p4kl0nc4t/Spammer-Grab && mv Spammer-Grab $HOME')
		done()

def diejoubu():
		start()
		os.system('git clone https://github.com/alintamvanz/diejoubu && mv diejoubu $HOME')
		done()

def igprivate():
		start()
		os.system('git clone https://github.com/anadhelf/ig && mv ig $HOME')
		done()

def blazy():
		start()
		os.system('git clone https://github.com/UltimateHackers/Blazy && mv Blazy $HOME')
		done()

def termuxfedora():
		start()
		os.system('git clone https://github.com/nmilosev/termux-fedora.git && mv termux-fedora $HOME')
		done()

def meisha():
		start()
		os.system('git clone https://github.com/Gameye98/Meisha.git && mv Meisha $HOME')
		done()

def airgedon():
		start()
		os.system('git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git && mv airgeddon $HOME')
		done()

def angryfuzzer():
  start()
  os.system('git clone https://github.com/ihebski/angryFuzzer.git')
  os.system('mv angryFuzzer $HOME')
  done()

def brutexss():
		start()
		os.system('git clone https://github.com/shawarkhanethicalhacker/BruteXSS.git && mv BruteXSS $HOME')
		done()

def webpwneer():
		start()
		os.system('git clone https://github.com/zigoo0/webpwn3r && mv webpwn3r $HOME')
		done()

def killchain():
		start()
		os.system('git clone https://github.com/ruped24/killchain.git && mv killchain $HOME')
		done()

def dedsploit():
		start()
		os.system('git clone https://github.com/ex0dus-0x/dedsploit.git && mv dedsploit $HOME')
		done()

def crips():
		start()
		os.system('wget https://raw.githubusercontent.com/Manisso/Crips/master/crips.py && mv crips.py $HOME')
		done()

def xsstrike():
		start()
		os.system('git clone https://github.com/UltimateHackers/XSStrike && mv XSStrike $HOME')
		done()

def cyberscan():
		start()
		os.system('git clone https://github.com/medbenali/CyberScan && mv CyberScan $HOME')
		done()

def egyptian():
		start()
		os.system('git clone https://github.com/WazeHell/Egyptian-SMS-Spammer.git && mv Egyptian-SMS-Spammer $HOME')
		done()

def setoolkit():
		start()
		os.system('curl -LO https://raw.githubusercontent.com/Techzindia/setoolkit-for-termux/master/setoolkit.sh && mv setoolkit.sh $HOME')
		done()

def wifresti():
		start()
		os.system('git clone https://github.com/LionSec/wifresti.git && mv wifresti $HOME')
		done()

def striker():
		start()
		os.system('git clone https://github.com/UltimateHackers/Striker && mv Striker $HOME')
		done()

def qrljacking():
		start()
		os.system('git clone https://github.com/OWASP/QRLJacking.git && mv QRLJacking $HOME')
		done()

def termuxarchlinux():
		start()
		os.system('git clone https://github.com/sdrausty/termux-archlinux && mv termux-archlinux $HOME')
		done()

def hacktronian():
		start()
		os.system('git clone https://github.com/thehackingsage/hacktronian && mv hacktronian $HOME')
		done()

def gasmask():
		start()
		os.system('git clone https://github.com/twelvesec/gasmask && mv gasmask $HOME')
		done()

def cookiestealer():
		start()
		os.system('git clone https://github.com/Xyl2k/Cookie-stealer.git && mv Cookie-stealer $HOME')
		done()

def wpscan():
		start()
		os.system('git clone https://github.com/wpscanteam/wpscan/ && mv wpscan $HOME')
		done()

def creednmap():
		start()
		os.system('git clone https://github.com/lightos/credmap.git && mv credmap $HOME')
		done()

def python():
		start()
		os.system('apt-get install python2 -y && apt-get install python -y')
		done()

def trity():
		start()
		os.system('git clone https://github.com/toxic-ig/Trity.git && mv Trity $HOME')
		done()

def badmod():
		start()
		os.system('git clone https://github.com/Lexiie/BadMod.git && mv BadMod $HOME')
		done()

def wifiphister():
		start()
		os.system('git clone https://github.com/wifiphisher/wifiphisher.git && mv wifiphisher $HOME')
		done()

def theinspector():
		start()
		os.system('git clone https://github.com/Moham3dRiahi/Th3inspector.git && mv Th3inspector $HOME')
		done()

def twitersniper():
		start()
		os.system('git clone https://github.com/abdallahelsokary/TwitterSniper.git && mv TwitterSniper $HOME')
		done()

def routersploit():
		start()
		os.system('git clone https://github.com/reverse-shell/routersploit.git && mv routersploit $HOME')
		done()

def hydra():
		start()
		os.system('apt-get install hydra -y')
		done()

def txtool():
		start()
		os.system('git clone https://github.com/kuburan/txtool.git && mv txtool $HOME')
		done()

def termuxapi():
		start()
		os.system('apt-get install termux-api -y')
		done()

def emailbomber():
		start()
		os.system('git clone https://github.com/zanyarjamal/Email-bomber.git && mv Email-bomber $HOME')
		done()

def gcospam():
		start()
		os.system('git clone https://github.com/Amriez/gcospam && mv gcospam $HOME')
		done()

def autopixiewps():
		start()
		os.system('git clone https://github.com/nxxxu/AutoPixieWps.git && mv AutoPixieWps $HOME')
		done()

def thefake():
		start()
		os.system('git clone https://github.com/soracyberteam/the-fake.git && mv the-fake $HOME')
		done()

def anonhackertools():
		start()
		os.system('git clone https://github.com/AnonHackerr/toolss.git && mv toolss $HOME')
		done()

def crewbot():
		start()
		os.system('git clone https://github.com/Xeit666h05t/CrewBot && mv CrewBot $HOME')
		done()
def sqliv():
		start()
		os.system('git clone https://github.com/Lexiie/sqliv.git && mv sqliv $HOME')
		done()

def newspammer():
		start()
		os.system('git clone https://github.com/haijuga7/New-Spammer && mv New-Spammer $HOME')
		done()

def emailaccount():
		start()
		os.system('git clone https://github.com/x-xsystm/account && mv account $HOME')
		done()

def fbautoreaction():
		start()
		os.system('git clone https://github.com/tomiashari/fb-autoreaction.git && mv fb-autoreaction $HOME')
		done()

def socialfish():
		start()
		os.system('git clone https://github.com/UndeadSec/SocialFish/socialfish/ && mv socialfish $HOME')
		done()

def sniper():
		start()
		os.system('git clone https://github.com/1N3/Sn1per && mv Sn1per $HOME')
		done()

def shellstack():
		start()
		os.system('git clone https://github.com/Tuhinshubhra/shellstack && mv shellstack $HOME')
		done()

def breacher():
		start()
		os.system('git clone https://github.com/UltimateHackers/Breacher.git && mv Breacher $HOME')
		done()

def tcpdump():
		start()
		os.system('wget https://www.androidtcpdump.com/download/4.9.2/tcpdump && mv tcpdump $HOME')
		done()

def sodan():
		start()
		os.system('pip2 install sodan')
		print 'usage > shodan init copas-api-shodan'
		done()

def umbrella():
		start()
		os.system('git clone https://github.com/4w4k3/Umbrella.git && mv Umbrella $HOME')
		done()

def archlinuxsetup():
	start()
	os.system('wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh && mv setupTermuxArch $HOME')

def weevely():
    	start()
    	os.system('git clone https://github.com/epinna/weevely3 && mv weevely3 $HOME')
    	done()

def wifibrutecrack():
    	start()
    	os.system('git clone https://github.com/cinquemb/WifiBruteCrack.git && mv WifiBruteCrack $HOME')
    	done()

def wifipumkin():
    	start()
    	os.system('git clone https://github.com/P0cL4bs/WiFi-Pumpkin.git && mv WiFi-Pumpkin $HOME')
    	done()

def wirespy():
    	start()
    	os.system('git clone https://github.com/AresS31/wirespy.git && mv wirespy $HOME')
    	done()

def pemulungbtc():
    	start()
    	os.system('git clone https://github.com/Cvar1984/pemulungBTC.git && mv pemulungBTC $HOME')
    	done()

def chrootetermux():
    	start()
    	os.system('git clone https://github.com/Neo-Oli/chrooted-termux.git && mv chrooted-termux $HOME')
    	done()

def nano():
    	start()
    	os.system('apt-get install nano -y')
    	print 'usage > nano example.py'
    	done()

def pydictor():
    	start()
    	os.system('git clone https://github.com/LandGrey/pydictor.git && mv pydictor $HOME')
    	done()

def owscan():
    	start()
    	os.system('git clone https://github.com/Gameye98/OWScan.git && mv OWScan $HOME')
    	done()

def astranmap():
    	start()
    	os.system('git clone https://github.com/Gameye98/AstraNmap.git && mv AstraNmap $HOME')
    	done()

def tembakxl():
    	start()
    	os.system('git clone https://github.com/joss24242/xl-py && mv xl-py $HOME')
    	done()

def indowordlist():
    	start()
    	os.system('apt-get install nano -y')
    	os.system('nano lib/pass.txt')

def thefuck():
    	start()
    	os.system('pip install thefuck')
    	done()

def vim():
    	start()
    	os.system('apt-get install vim -y && vim')
    	done()

def sqlmate():
    	start()
    	os.system('git clone https://github.com/UltimateHackers/sqlmate && mv sqlmate $HOME')
    	done()

def ftp():
    	start()
    	os.system('git clone https://github.com/beerecca/ftf.git && mv ftf $HOME')
    	done()

def elpscrk():
    	start()
    	os.system('git clone https://github.com/D4Vinci/elpscrk.git && mv elpscrk $HOME')
    	done()

def golbin():
    	start()
    	os.system('git clone https://github.com/UndeadSec/GoblinWordGenerator.git && mv GoblinWordGenerator $HOME')
    	done()

def evilurl():
    	start()
    	os.system('git clone https://github.com/UndeadSec/EvilURL.git && mv EvilURL $HOME')
    	done()

def hash():
    	start()
    	os.system('git clone https://github.com/Gameye98/1337Hash.git && mv 1337Hash $HOME')
    	done()

def passgen():
    	start()
    	os.system('git clone https://github.com/TechnicalMujeeb/PassGen.git && mv PassGen $HOME')
    	done()

def wtf():
    	start()
    	os.system('git clone https://github.com/Xi4u7/wtf && mv wtf $HOME')
    	done()

def planetworkddos():
    	start()
    	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS.git && mv Planetwork-DDOS $HOME')
    	done()

def spiderbot():
       	start()
    	os.system('git clone https://github.com/Cvar1984/SpiderBot.git && mv SpiderBot $HOME')
    	done()

def nethunterintermux():
    	start()
    	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux.git && mv Nethunter-In-Termux $HOME')
    	done()

def floodflood():
    	start()
    	os.system('wget http://override.waper.co/files/fl00d.apk')
    	os.system('wget http://override.waper.co/files/fl00d2.apk')
    	os.system('mv fl00d.apk $HOME')
    	os.system('mv fl00d2.apk $HOME')
    	done()

def harvester():
    	start()
    	os.system('git clone https://github.com/laramies/theHarvester && mv theHarvester $HOME')
    	done()

def xnmap():
    	start()
    	os.system('git clone https://github.com/Ranginang67/Xnmap.git && mv Xnmap $HOME')
    	done()

def kalitermux():
    	start()
    	os.system('git clone https://github.com/Ranginang67/kali-termux.git && mv kali-termux $HOME')
    	done()

def fbook():
    	start()
    	os.system('git clone https://github.com/Ranginang67/Fbook.git && mv Fbook $HOME')
    	done()

def tor():
    	start()
    	os.system('apt-get install tor -y')
    	done()

def wifihacker():
    	start()
    	os.system('git clone https://github.com/esc0rtd3w/wifi-hacker && mv wifi-hacker $HOME')
    	done()

def termuxwebscan():
    	start()
    	os.system('git clone https://github.com/silverhat007/termux_webscan && mv termux_webscan $HOME')
    	done()

def xplsearch():
    	start()
    	os.system('git clone https://github.com/r00tmars/XPL-SEARCH.git && mv XPL-SEARCH $HOME')
    	done()

def commix():
    	start()
    	os.system('git clone https://github.com/commixproject/commix && mv commix $HOME')
    	done()

def webcode():
    	start()
    	os.system('git clone https://github.com/Ranginang67/webcode.git && mv webcode $HOME')
    	done()

def infoga():
    	start()
    	os.system('git clone https://github.com/m4ll0k/infoga && mv infoga $HOME')
    	done()

def onioff():
    	start()
    	os.system('git clone https://github.com/k4m4/onioff && mv onioff $HOME')
    	done()

def peepdf():
    	start()
    	os.system('git clone https://github.com/jesparza/peepdf.git && mv peepdf $HOME')
    	done()

def trackip():
    	start()
    	os.system('git clone https://github.com/Ranginang67/track-ip.git && mv track-ip $HOME')
    	done()

def zarp():
    	start()
    	os.system('git clone https://github.com/hatRiot/zarp.git && mv zarp $HOME')
    	done()

def autobackup():
    	start()
    	os.system('git clone https://github.com/UmutAlihan/autobackup.git && mv autobackup $HOME')
    	done()

def bottgpersonal():
    	start()
    	os.system('git clone https://github.com/UmutAlihan/bot-tg-personal.git && mv bot-tg-personal $HOME')
    	done()
def ipthrower():
    	start()
    	os.system('git clone https://github.com/UmutAlihan/ip-thrower.git && mv ip-thrower $HOME')
    	done()
def manishlinebot():
    	start()
    	os.system('git clone https://github.com/kumarmanish511/ManishLineBot.git && mv ManishLineBot $HOME')
    	done()
def botlinepytiga():
    	start()
    	os.system('git clone https://github.com/kumarmanish511/BotLinePython3.git && mv BotLinePython3 $HOME')
    	done()
def koplax():
    	start()
    	os.system('git clone https://github.com/kumarmanish511/Koplaxs5Bot.git && mv Koplaxs5Bot $HOME')
    	done()
def termuxcreatepackage():
    	start()
    	os.system('git clone https://github.com/Grimler91/termux-create-package.git && mv termux-create-package $HOME')
    	done()
def randomwebsearch():
    	start()
    	os.system('git clone https://github.com/xxRMxx/RandomWebSearch.git && mv RandomWebSearch $HOME')
    	done()
def ipfy():
    	start()
    	os.system('git clone https://github.com/T4P4N/IP-FY.git && mv IP-FY $HOME')
    	done()
def randomchuck():
    	start()
    	os.system('git clone https://github.com/T4P4N/Random-Chuck-Norris-Facts.git && mv Random-Chuck-Norris-Facts $HOME')
    	done()
def facebookbruteforce():
    	start()
    	os.system('git clone https://github.com/themastersunil/facebook-brute-force.git && mv facebook-brute-force $HOME')
    	done()
def scrape():
    	start()
    	os.system('git clone https://github.com/thisisayush/scrape.git && mv scrape $HOME')
    	done()
def scripttools():
    	start()
    	os.system('git clone https://github.com/Xeit666h05t/CripTOOLs.git && mv CripTOOLs $HOME')
    	done()
def boxcoder():
    	start()
    	os.system('git clone https://github.com/Xeit666h05t/BoxCoder.git && mv BoxCoder $HOME')
    	done()
def boxcoderversidua():
    	start()
    	os.system('git clone https://github.com/Xeit666h05t/BoxCoderV.2.git && mv BoxCoderV.2 $HOME')
    	done()
def boxspam():
    	start()
    	os.system('git clone https://github.com/Xeit666h05t/BoxSpam.git && mv BoxSpam $HOME')
    	done()
def termuxboxes():
    	start()
    	os.system('git clone https://github.com/remo7777/termux-boxes.git && mv termux-boxes $HOME')
    	done()
def bulltools():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Bulltools.git && mv Bulltools $HOME')
    	done()
def bullkattack():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Bull-Attack.git && mv Bull-Attack $HOME')
    	done()
def kalilinuxontermux():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Kali-Linux.git && mv Kali-Linux $HOME')
    	done()
def termuxbaner():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Termux-Banner.git && mv Termux-Banner $HOME')
    	done()
def ipattack():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Ip-Attack.git && mv Ip-Attack $HOME')
    	done()
def termuxos():
    	start()
    	os.system('git clone https://github.com/Bhai4You/Termux-Os.git && mv Termux-Os $HOME')
    	done()
def indonesianplayground():
    	start()
    	os.system('git clone https://github.com/geovedi/indonesian-nlp-playground.git && mv indonesian-nlp-playground $HOME')
    	done()
def sontekan():
    	start()
    	os.system('git clone https://github.com/geovedi/sontekan.git && mv sontekan $HOME')
    	done()
def givemeakey():
    	start()
    	os.system('git clone https://github.com/geovedi/givemeakey.git && mv givemeakey $HOME')
    	done()
def ddosscript():
    	start()
    	os.system('git clone https://github.com/FreelancePentester/ddos-script.git && mv ddos-script $HOME')
    	done()
def backdoorapk():
    	start()
    	os.system('git clone https://github.com/FreelancePentester/backdoor-apk.git && mv backdoor-apk $HOME')
    	done()
def termuxscript():
    	start()
    	os.system('git clone https://github.com/vaites/termux-scripts.git && mv termux-scripts $HOME')
    	done()
def pythontwitervot():
    	start()
    	os.system('git clone https://github.com/gauravssnl/Python-Twitter-Bot.git && mv Python-Twitter-Bot $HOME')
    	done()
def niktosymfix():
    	start()
    	os.system('git clone https://github.com/bensh4/nikto-sym-fix.git && mv nikto-sym-fix $HOME')
    	done()
def swapcli():
    	start()
    	os.system('git clone https://github.com/WahyuHidayattz/Swapcli.git && mv Swapcli $HOME')
    	done()
def fbrute():
    	start()
    	os.system('git clone https://github.com/p4kl0nc4t/f609-brute.git && mv f609-brute $HOME')
    	done()
def adfin():
    	start()
    	os.system('git clone https://github.com/p4kl0nc4t/AdFin.git && mv AdFin $HOME')
    	done()
def defidnotifer():
    	start()
    	os.system('git clone https://github.com/p4kl0nc4t/defid_notifier.git && mv defid_notifier $HOME')
    	done()
def pythem():
    	start()
    	os.system('git clone https://github.com/zone-h/PytheM.git && mv PytheM $HOME')
    	done()
def sqlimaker():
    	start()
    	os.system('git clone https://github.com/dalpan/sqlimaker.git && mv sqlimaker $HOME')
    	done()
def autoxjomla():
    	start()
    	os.system('git clone https://github.com/dalpan/autoxjoomla.git && mv autoxjoomla $HOME')
    	done()
def penbox():
    	start()
    	os.system('git clone https://github.com/dalpan/PenBox.git && mv PenBox $HOME')
    	done()
def smsidgo():
    	start()
    	os.system('git clone https://github.com/amsitlab/smsid-go.git && mv smsid-go $HOME')
    	done()
def grepmail():
    	start()
    	os.system('git clone https://github.com/x1n73ct/grepmail.git && mv grepmail $HOME')
    	done()
def mdlimacrack():
    	start()
    	os.system('git clone https://github.com/CiKu370/md5-crack.git && mv md5-crack $HOME')
    	done()
def mamangkey():
    	start()
    	os.system('git clone https://github.com/Amriez/MamangKey && mv MamangKey $HOME')
    	done()
def myenc():
    	start()
    	os.system('git clone https://github.com/pirmansx/myenc && mv myenc $HOME')
    	done()
def hashzer():
    	start()
    	os.system('git clone https://github.com/Anb3rSecID/Hashzer && mv Hashzer $Hashzer')
    	done()
def errorcybertool():
    	start()
    	os.system('git clone https://github.com/MrKeepSmile/errorcybertool.git && mv errorcybertool $HOME')
    	done()
def termuxgo():
    	start()
    	os.system('git clone https://github.com/rafalgolarz/termux-go && mv termux-go $HOME')
    	done()
def bolang():
    	start()
    	os.system('git clone https://github.com/Amriez/Bolang && mv Bolang $HOME')
    	done()
def metainstall():
    	start()
    	os.system('git clone https://github.com/4L13199/meTAInstall && mv meTAInstall $HOME')
    	done()
def ipscan():
    	start()
        os.system('git clone https://github.com/sysadminteam/IPscan && mv IPscan $HOME')
        done()
def spammersys():
    	start()
        os.system('git clone https://github.com/sysadminteam/spammer.sys && mv spammer.sys $HOME')
        done()
def androidpincrack():
    	start()
    	os.system('git clone https://github.com/PentesterES/AndroidPINCrack.git && mv AndroidPINCrack $HOME')
    	done()
def sir():
    	start()
        os.system('git clone https://github.com/AeonDave/sir && mv sir $HOME')
        done()
def zones():
    	start()
        os.system('git clone https://github.com/Cvar1984/zones && mv zones $HOME')
        done()
def sheell():
    	start()
        os.system('git clone https://github.com/LOoLzeC/SH33LL && mv SH33LL $HOME')
        done()
def reaverwps():
    	start()
        os.system('git clone https://github.com/t6x/reaver-wps-fork-t6x.git && mv reaver-wps-fork-t6x $HOME')
        done()
def fluxion():
    	start()
        os.system('git clone https://github.com/thehackingsage/Fluxion.git && mv Fluxion $HOME')
        done()
def phisinggame():
    	start()
        os.system('git clone https://github.com/senitopeng/PhisingGame.git && mv PhisingGame $HOME')
        done()
def anrspam():
    	start()
        os.system('git clone https://github.com/Amriez/ANRspam && mv ANRspam $HOME')
        done()
def avarspam():
    	start()
    	os.system('git clone https://github.com/ALX-04/AVARspam && mv AVARspam $HOME')
    	done()
def genscript():
    	start()
        os.system('git clone https://github.com/x-xsystm/genscript.git && mv genscript $HOME')
        done()
def ipmux():
    	start()
        os.system('git clone https://github.com/Amriez/ipmux && mv ipmux $HOME')
        done()
def inmux():
    	start()
        os.system('git clone https://github.com/Amriez/inmux && mv inmux $HOME')
        done()
def sqlscan():
    	start()
        os.system('git clone http://www.github.com/Cvar1984/sqlscan && mv $HOME')
        done()
def aocdeface():
    	start()
        os.system('git clone https://github.com/Amriez/AOCDEFACE && mv AOCDEFACE $HOME')
        done()
def greenreaper():
    	start()
    	os.system('git clone https://github.com/Amriez/GreenReaper && mv GreenReaper $HOME')
    	done()
def kawaibotnet():
    	start()
    	os.system('git clone https://github.com/Cvar1984/Kawai-Botnet && mv Kawai-Botnet $HOME')
    	done()
def ihst():
    	start()
    	os.system('git clone https://github.com/CiKu370/lhst && mv 1hst $HOME')
    	done()
def joomscan():
    	start()
    	os.system('git clone https://github.com/rezasp/joomscan.git && mv joomscan $HOME')
    	done()
def shellnoob():
    	start()
    	os.system('git clone https://github.com/reyammer/shellnoob.git && mv shellnoob $HOME')
    	done()
def fbupvdua():
    	start()
    	os.system('git clone https://github.com/mrSilent0598/FBUPv2 && mv FBUPv2 $HOME')
    	done()
def ufonett():
    	start()
    	os.system('git clone https://github.com/epsylon/ufonett && mv ufonett $HOME')
    	done()
def dssst():
    	start()
    	os.system('git clone https://github.com/stamparm/DSSSt && mv DSSSt $HOME')
    	done()
def routersploitsn():
    	start()
    	os.system('git clone https://github.com/reverse-shell/routersploitsn && mv routersploitsn $HOME')
    	done()
def findmyhash():
    	start()
    	os.system('git clone https://github.com/frdmn/findmyhash.git && mv findmyhash $HOME')
    	done()
def portwitness():
    	start()
    	os.system('git clone https://github.com/viperbluff/PortWitness.git && mv PortWitness $HOME')
    	done()
def icloud():
    	start()
    	os.system('wget https://raw.githubusercontent.com/m4ll0k/iCloudBrutter/master/icloud.py && mv icloud.py $HOME')
    	done()
def gshtoolbox():
    	start()
    	os.system('git clone https://github.com/Yoshieichiro01/GSH-ToolBox-V.1.git && mv GSH-ToolBox-V.1 $HOME')
    	done()
def termuxalpine():
    	start()
    	os.system('git clone https://github.com/Hax4us/TermuxAlpine.git && mv TermuxAlpine $HOME')
    	done()
def tmuxbunch():
    	start()
    	os.system('git clone https://github.com/Hax4us/Tmux-Bunch.git && mv Tmux-Bunch $HOME')
    	done()
def instagrambot():
    	start()
    	os.system('git clone https://github.com/fabioazedo120/InstagramBOT.git && mv InstagramBOT $HOME')
    	done()
def freefote():
    	start()
    	os.system('git clone https://github.com/fabioazedo120/FreeVote.git && mv FreeVote $HOME')
    	done()
def liteddos():
    	start()
    	os.system('git clone https://github.com/4L13199/LITEDDOS.git && mv LITEDDOS $HOME')
    	done()
def myserver():
    	start()
    	os.system('git clone https://github.com/Rajkumrdusad/MyServer.git && mv MyServer $HOME')
    	done()
def cookiestealer():
    	start()
    	os.system('git clon ehttps://github.com/Xyl2k/Cookie-stealer && mv Cookie-stealer $HOME')
    	done()
def litefont():
    	start()
    	os.system('git clone https://github.com/4L13199/LITEFONT.git && mv LITEFONT $HOME')
    	done()
def litescript():
    	start()
    	os.system('git clone https://github.com/4L13199/LITESCRIPT.git && mv LITESCRIPT $HOME')
    	done()
def lolzrat():
    	start()
    	os.system('git clone https://github.com/mrcakil/Lolz_RAT.git && mv Lolz_RAT $HOME')
    	done()
def awsectools():
    	start()
    	os.system('git clone https://github.com/aryanrtm/4wsectools && mv 4wsectools $HOME')
    	done()
def termuxlazysqlmap():
    	start()
    	os.system('git clone https://github.com/verluchie/termux-lazysqlmap.git && mv termuxlazysqlmap $HOME')
    	done()
def iesdeface():
    	start()
    	os.system('git clone https://github.com/ALX-04/iesDEFACE && mv iesDEFACE $HOME')
    	done()
def camstream():
    	start()
    	os.system('git clone https://github.com/avramit/CamStream-V3 && mv CamStream-V3 $HOME')
    	done()
def xeitcyber():
    	start()
    	os.system('git clone https://github.com/DaffaTakarai/XEIT_Cyber && mv XEIT_Cyber $HOME')
    	done()
def phpbackconector():
    	start()
    	os.system('git clone https://github.com/shawarkhanethicalhacker/PHP-BackConnector && mv PHP-BackConnector $HOME')
    	done()
def csrfpocmaker():
    	start()
    	os.system('git clone https://github.com/shawarkhanethicalhacker/csrfpocmaker && mv csrfpocmaker $HOME')
    	done()
def thanatosarcher():
    	start()
    	os.system('git clone https://github.com/4shadoww/thanatos-archer && mv thanatos-archer $HOME')
    	done()
def darksploit():
    	start()
    	os.system('git clone https://github.com/LOoLzeC/DarkSploit && mv DarkSploit $HOME')
    	done()
def knock():
    	start()
    	os.system('git clone https://github.com/guelfoweb/knock.git && mv knock $HOME')
    	done()
def aduasv():
    	start()
    	os.system('git clone https://github.com/hahwul/a2sv && mv a2sv $HOME')
    	done()
def optiviaframework():
    	start()
    	os.system('git clone https://github.com/joker25000/Optiva-Framework && mv Optiva-Framework $HOME')
    	done()
def dostattack():
    	start()
    	os.system('git clone https://github.com/verluchie/dost-attack && mv dost-attack $HOME')
    	done()
def heartbleed():
    	start()
    	os.system('git clone https://github.com/TechnicalMujeeb/HeartBleed.git && mv HeartBleed $HOME')
    	done()
def checkurl():
    	start()
    	os.system(' git clone https://github.com/UndeadSec/checkURL && mv checkURL $HOME')
    	done()
def debinject():
    	start()
    	os.system('git clone https://github.com/UndeadSec/Debinject.git && mv Debinject $HOME')
    	done()
def clickjackingtester():
    	start()
    	os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester && mv Clickjacking-Tester $HOME')
    	done()
def androbugsframework():
    	start()
    	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework && mv AndroBugs_Framework $HOME')
    	done()
def termuxspeak():
    	start()
    	os.system('git clone https://github.com/TechnicalMujeeb/Termux-speak && mv Termux-speak $HOME')
    	done()
def tmvenom():
    	start()
    	os.system('git clone https://github.com/TechnicalMujeeb/tmvenom && mv tmvenom $HOME')
    	done()
def termuxlazyscript():
    	start()
    	os.system('git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git && mv Termux-Lazyscript $HOME')
    	done()
def gloomframework():
    	start()
    	os.system('git clone https://github.com/StreetSec/Gloom-Framework.git && mv Gloom-Framework $HOME')
    	done()
def brutespray():
    	start()
    	os.system('git clone https://github.com/x90skysn3k/brutespray && mv brutespray $HOME')
    	done()
def sublister():
    	start()
    	os.system('git clone https://github.com/aboul3la/Sublist3r && mv Sublist3r $HOME')
    	done()
def fhxhashkiller():
    	start()
    	os.system('git cone https://github.com/FajriHidayat088/FHX-Hash-Killer/ && mv FHX-Hash-Killer $HOME')
    	done()
def wsltools():
    	start()
    	os.system('git clone https://github.com/AnonHackerr/WSLTools && mv WSLTools $HOME')
    	done()
def termuxpackages():
    	start()
    	os.system('git clone https://github.com/kuburan/termux-packages.git && mv termux-packages $HOME')
    	done()
def contexploit():
    	start()
    	os.system('git clone https://github.com/kuburan/contexploit.git && mv contexploit $HOME')
    	done()
def spamtest():
		start()
		os.system('git clone https://github.com/haijuga7/spam-test && mv spam-test $HOME')
		done()
def enigma():
		start()
		os.system('git clone https://github.com/UndeadSec/Enigma.git && mv Enigma $HOME')
		done()
def credover():
		start()
		os.system('git clone https://github.com/UndeadSec/Cr3dOv3r.git && mv Cr3dOv3r $HOME')
		done()
def allinwan():
		start()
		os.system('git clone https://github.com/verluchie/allinwan.git && mv allinwan $HOME')
		done()
def evilcreateframework():
		start()
		os.system('git clone https://github.com/LOoLzeC/Evil-create-framework.git && mv Evil-create-framework $HOME')
		done()
def gabutz():
		start()
		os.system('git clone https://github.com/LOoLzeC/gabutz.git && mv gabutz $HOME')
		done()
def iwpam():
		start()
		os.system('git clone https://github.com/guelfoweb/iwmap.git && mv iwmap $HOME')
		done()
def peframe():
		start()
		os.system('git clone https://github.com/guelfoweb/peframe.git && mv peframe $HOME')
		done()
def fbid():
		start()
		os.system('git clone https://github.com/guelfoweb/fbid.git && mv fbid $HOME')
		done()
def reconraven():
		start()
		os.system('git clone https://github.com/hahwul/recon-raven.git && mv recon-raven $HOME')
		done()
def hbxss():
		start()
		os.system('git clone https://github.com/hahwul/hbxss.git && mv hbxss $HOME')
		done()
def photon():
		start()
		os.system('git clone https://github.com/s0md3v/Photon.git && mv Photon $HOME')
		done()
def hue():
		start()
		os.system('git clone https://github.com/s0md3v/hue.git && mv hue $HOME')
		done()
def routerpi():
		start()
		os.system('git clone https://github.com/vay3t/router-pi.git && mv router-pi $HOME')
		done()
def apkbinder():
		start()
		os.system('git clone https://github.com/vay3t/apkbinder.git && mv apkbinder $HOME')
		done()
def haxorpi():
		start()
		os.system('git clone https://github.com/vay3t/hax0rpi.git && mv hax0rpi $HOME')
		done()
def nethunterlrt():
		start()
		os.system('git clone https://github.com/vay3t/nethunter-LRT.git && mv nethunter-LRT $HOME')
		done()
def awselbloganalyer():
		start()
		os.system('git clone https://github.com/jonascheng/AwsElbLogAnalyer.git && mv AwsElbLogAnalyer $HOME')
		done()
def dockervernemq():
		start()
		os.system('git clone https://github.com/jonascheng/docker-vernemq.git && mv docker-vernemq $HOME')
		done()
def kekescan():
		start()
		os.system('git clone https://github.com/xiaoxiaoleo/kekescan.git && mv kekescan $HOME')
		done()
def ctftool():
		start()
		os.system('git clone https://github.com/jfarriagada/ctftool.git && mv ctftool $HOME')
		done()
def cornershop():
		start()
		os.system('git clone https://github.com/jfarriagada/cornershop.git && mv cornershop $HOME')
		done()
def prex():
		start()
		os.system('git clone https://github.com/telekomancer/prex.git && mv prex $HOME')
		done()
def jdvd():
		start()
		os.system('git clone https://github.com/telekomancer/jdvd.git && mv jdvd $HOME')
		done()
def securityscripts():
		start()
		os.system('git clone https://github.com/vikingore/security-scripts.git && mv security-scripts $HOME')
		done()
def simplefilefinder():
		start()
		os.system('git clone https://github.com/hck1army/simplefilefinder.git && mv simplefilefinder $HOME')
		done()
def linset():
		start()
		os.system('git clone https://github.com/robertomonges/linset.git && mv linset $HOME')
		done()
def mitmf():
		start()
		os.system('git clone https://github.com/byt3bl33d3r/MITMf.git && mv MITMf $HOME')
		done()
def crackmapexec():
		start()
		os.system('git clone https://github.com/byt3bl33d3r/CrackMapExec.git && mv CrackMapExec $HOME')
		done()
def deathstart():
		start()
		os.system('git clone https://github.com/byt3bl33d3r/DeathStar.git && mv DeathStar $HOME')
		done()
def gcat():
		start()
		os.system('git clone https://github.com/byt3bl33d3r/gcat.git && mv gcat $HOME')
		done()
def rocketman():
		start()
		os.system('git clone https://github.com/binkybear/rock3tman.git && mv rock3tman $HOME')
		done()
def honeypi():
		start()
		os.system('git clone https://github.com/binkybear/HoneyPi.git && mv HoneyPi $HOME')
		done()
def captipper():
		start()
		os.system('git clone https://github.com/najashark/CapTipper.git && mv CapTipper $HOME')
		done()
def unifivouchergenerator():
		start()
		os.system('git clone https://github.com/songhanpoo/unifi-voucher-generator.git && mv unifi-voucher-generator $HOME')
		done()
def wplue():
		start()
		os.system('git clone https://github.com/luenix/WP-Lue.git && mv WP-Lue $HOME')
		done()
def sescan():
		start()
		os.system('git clone https://github.com/abhn/S3Scan.git && mv S3Scan $HOME')
		done()
def cantoolz():
		start()
		os.system('git clone https://github.com/kevins1022/CANToolz.git && mv CANToolz $HOME')
		done()
def weaf():
		start()
		os.system('git clone https://github.com/kevins1022/w3af.git && mv w3af $HOME')
		done()
def pythonlearning():
		start()
		os.system('git clone https://github.com/andr3w-hilton/Python_Learning.git && mv Python_Learning $HOME')
		done()
def cooker():
		start()
		os.system('git clone https://github.com/jmutkawoa/cooker.git && mv cooker $HOME')
		done()
def ghostupdater():
		start()
		os.system('git clone https://github.com/victordzmr/ghost-updater.git && mv ghost-updater $HOME')
		done()
def dockerwordpress():
		start()
		os.system('git clone https://github.com/akushal/docker-wordpress.git && mv docker-wordpress $HOME')
		done()
def autotweet():
		start()
		os.system('git clone https://github.com/akushal/autotweet.git && mv autotweet $HOME')
		done()
def pantesttools():
		start()
		os.system('git clone https://github.com/St0rn/Pentest_tools.git && mv Pentest_tools $HOME')
		done()
def exploit():
		start()
		os.system('git clone https://github.com/St0rn/Exploit.git && mv Exploit $HOME')
		done()
def pydeletepdfpages():
		start()
		os.system('git clone https://github.com/Mebus/pyDeletePdfPages && mv pyDeletePdfPages $HOME')
		done()
def pythonblackhat():
		start()
		os.system('git clone https://github.com/semvak024/Python-BlackHat.git && mv Python-BlackHat $HOME')
		done()
def pythonpenetrationtestingcookbook():
		start()
		os.system('git clone https://github.com/PacktPublishing/Python-Penetration-Testing-Cookbook.git && mv Python-Penetration-Testing-Cookbook $HOME')
		done()
def termuxmpv():
	start()
	os.system('git clone https://github.com/Neo-Oli/Termux-Mpv.git && mv Termux-Mpv $HOME')
	done()
def tuyulbtn():
	start()
	os.system('git clone https://github.com/Senitopeng/TuyulBtn && mv TuyulBtn $HOME')
	done()
def gadogado():
	start()
	os.system('git clone https://github.com/Senitopeng/GadoGado.git && mv GadoGado $HOME')
	done()
def cokrat():
	start()
	os.system('git clone https://github.com/mrcakil/cok-Rat && mv cok-Rat $HOME')
	done()
def iesinstal():
	start()
	os.system('git clone https://github.com/ALX-04/iesInstall && mv iesInstall $HOME')
	done()
def ffont():
	start()
	os.system('git clone https://github.com/4L13199/ffont && mv ffont $HOME')
	done()
def reconng():
	start()
	os.system('git clone https://github.com/jorik041/recon-ng.git && mv recon-ng $HOME')
	done()
def kickthemeout():
	start()
	os.system('git clone https://github.com/k4m4/kickthemout.git && mv kickthemout $HOME')
	done()
def fuxploider():
	start()
	os,system('git clone https://github.com/almandin/fuxploider.git && mv fuxploider $HOME')
	done()
def evilginx():
	start()
	os.system('git clone https://github.com/kgretzky/evilginx.git && mv evilginx $HOME')
	done()
def alienhost():
	start()
	os.system('git clone https://github.com/Bhai4You/Alien-Host.git && mv Alien-Host $HOME')
	done()
def exploitoncli():
	start()
	os.system('git clone https://github.com/r00tmars/ExploitOnCLI.git && mv ExploitOnCLI $HOME')
	done()
def uidsploit():
	start()
	os.system('git clone https://github.com/siruidops/uidsploit.git && mv uidsploit $HOME')
	done()
def trape():
	start()
	os.system('git clone https://github.com/boxug/trape.git && mv trape $HOME')
	done()
def saint():
	start()
	os.system('git clone https://github.com/tiagorlampert/sAINT.git && mv sAINT $HOME')
	done()

os.system('bash menu.bash')
k = raw_input('[*] hajar kong : ')

if k == '01' or k == '1':
	sqlmap()
elif k == '02' or k == '2':
	redhawk()
elif k == '03' or k == '3':
	dtect()
elif k == '04' or k == '4':
	litespam()
elif k == '05' or k == '5':
	hakku()
elif k == '06' or k == '6':
	visql()
elif k == '07' or k == '7':
	atscan()
elif k == '08' or k == '8':
	hunner()
elif k == '09' or k == '9':
	weeman()
elif k == '10':
	hashbuster()
elif k == '11':
	websploit()
elif k == '12':
	hatclound()
elif k == '13':
	brutal()
elif k == '14':
	metasploit()
elif k == '15':
	xerxes()
elif k == '16':
	hammer()
elif k == '17':
	hulk()
elif k == '18':
	ilucky()
elif k == '19':
	pentmenu()
elif k == '20':
	torshammer()
elif k == '21':
	goldeneye()
elif k == '22':
	katoolin()
elif k == '23':
	wpseku()
elif k == '24':
	inurlbr()
elif k == '25':
	clonemaster()
elif k == '26':
	pybelt()
elif k == '27':
	wifite()
elif k == '28':
	recondog()
elif k == '29':
	mbf()
elif k == '30':
	ipgeolocation()
elif k == '31':
	termuxsudo()
elif k == '32':
	instahack()
elif k == '33':
	termuxubuntu()
elif k == '34':
	nmap()
elif k == '35':
	arat()
elif k == '36':
	santet()
elif k == '37':
	liteddos()
elif k == '38':
	googledork()
elif k == '39':
	adminfinder()
elif k == '40':
	gmailbrute()
elif k == '41':
	cmsmap()
elif k == '42':
	instabot()
elif k == '43':
	thefatrat()
elif k == '44':
	webdav()
elif k == '45':
	netattack()
elif k == '46':
	netattackdua()
elif k == '47':
	pybozocrack()
elif k == '48':
	slowloris()
elif k == '49':
	wem()
elif k == '50':
	jembod()
elif k == '51':
	yahoobrute()
elif k == '52':
	mailbrute()
elif k == '53':
	hotmail()
elif k == '54':
	nikto()
elif k == '55':
	blackhydra()
elif k == '56':
	auxscan()
elif k == '57':
	xshell()
elif k == '58':
	cupp()
elif k == '59':
	blackbox()
elif k == '60':
	kodork()
elif k == '61':
	hostchecker()
elif k == '62':
	fbbrute()
elif k == '63':
	wascan()
elif k == '64':
    oray()
elif k == '65':
    spamhooqtv()
elif k == '66':
	spazsms()
elif k == '67':
	wfdroid()
elif k == '68':
	ngrok()
elif k == '69':
	wordpresbrute()
elif k == '70':
	spyder()
elif k == '71':
	lokomedia()
elif k == '72':
	vim()
elif k == '73':
	fsociety()
elif k == '74':
	devploit()
elif k == '75':
	dirsearch()
elif k == '76':
	toolsboxexploiter()
elif k == '77':
	bluemaho()
elif k == '78':
	browsing()
elif k == '79':
	botfbbangdjon()
elif k == '80':
	spammergrab()
elif k == '81':
	diejoubu()
elif k == '82':
	igprivate()
elif k == '83':
	blazy()
elif k == '84':
	termuxfedora()
elif k == '85':
	meisha()
elif k == '86':
	airgedon()
elif k == '87':
	angryfuzzer()
elif k == '88':
	brutexss()
elif k == '89':
	webpwneer()
elif k == '90':
	killchain()
elif k == '91':
	dedsploit()
elif k == '92':
	crips()
elif k == '93':
	xsstrike()
elif k == '94':
	cyberscan()
elif k == '95':
	egyptian()
elif k == '96':
	setoolkit()
elif k == '97':
	wifresti()
elif k == '98':
	striker()
elif k == '99':
	qrljacking()
elif k == '100':
	termuxarchlinux()
elif k == '101':
	hacktronian()
elif k == '102':
	gasmask()
elif k == '103':
	cookiestealer()
elif k == '104':
	wpscan()
elif k == '105':
	creednmap()
elif k == '106':
	python()
elif k == '107':
	trity()
elif k == '108':
	badmod()
elif k == '109':
	wifiphisher()
elif k == '110':
	theinspector()
elif k == '111':
	twitersniper()
elif k == '112':
	routersploit()
elif k == '113':
	hydra()
elif k == '114':
	txtool()
elif k == '115':
	termuxapi()
elif k == '116':
	emailbomber()
elif k == '117':
	gcospam()
elif k == '118':
	autopixiewps()
elif k == '119':
	thefake()
elif k == '120':
	anonhackertools()
elif k == '121':
	crewbot()
elif k == '122':
	sqliv()
elif k == '123':
	newspammer()
elif k == '124':
	emailaccount()
elif k == '125':
	fbautoreaction()
elif k == '126':
	socialfish()
elif k == '127':
	sniper()
elif k == '128':
	shellstack()
elif k == '129':
	breacher()
elif k == '130':
	tcpdump()
elif k == '131':
	sodan()
elif k == '132':
	umbrella()
elif k == '133':
	archlinuxsetup()
elif k == '134':
	weevely()
elif k == '135':
	wifibrutecrack()
elif k == '136':
	wifipumkin()
elif k == '137':
	wirespy()
elif k == '138':
	pemulungbtc()
elif k == '139':
	chrootetermux()
elif k == '140':
	nano()
elif k == '141':
	pydictor()
elif k == '142':
	owscan()
elif k == '143':
	astranmap()
elif k == '144':
	tembakxl()
elif k == '145':
	indowordlist()
elif k == '146':
	thefuck()
elif k == '147':
	vim()
elif k == '148':
	sqlmate()
elif k == '149':
	ftp()
elif k == '150':
	elpscrk()
elif k == '151':
	golbin()
elif k == '152':
	evilurl()
elif k == '153':
	hash()
elif k == '154':
	passgen()
elif k == '155':
	wtf()
elif k == '156':
	planetworkddos()
elif k == '157':
	spiderbot()
elif k == '158':
	nethunterintermux()
elif k == '159':
	floodflood()
elif k == '160':
	harvester()
elif k == '161':
	xnmap()
elif k == '162':
	kalitermux()
elif k == '163':
	fbook()
elif k == '164':
	tor()
elif k == '165':
	wifihacker()
elif k == '166':
	termuxwebscan()
elif k == '167':
	xplsearch()
elif k == '168':
	commix()
elif k == '169':
	webcode()
elif k == '170':
	infoga()
elif k == '171':
	onioff()
elif k == '172':
	peepdf()
elif k == '173':
	trackip()
elif k == '174':
	zarp()
elif k == '175':
	autobackup()
elif k == '176':
	bottgpersonal()
elif k == '177':
	ipthrower()
elif k == '178':
	manishlinebot()
elif k == '179':
	botlinepytiga()
elif k == '180':
	koplax()
elif k == '181':
	termuxcreatepackage()
elif k == '182':
	randomwebsearch()
elif k == '183':
	ipfy()
elif k == '184':
	randomchuck()
elif k == '185':
	facebookbruteforce()
elif k == '186':
	scrape()
elif k == '187':
	scripttools()
elif k == '188':
	boxcoder()
elif k == '189':
	boxcoderversidua()
elif k == '190':
	boxspam()
elif k == '191':
	termuxboxes()
elif k == '192':
	bulltools()
elif k == '193':
	bullkattack()
elif k == '194':
	kalilinuxontermux()
elif k == '195':
	termuxbaner()
elif k == '196':
	ipattack()
elif k == '197':
	termuxos()
elif k == '198':
	indonesianplayground()
elif k == '199':
	sontekan()
elif k == '200':
	givemeakey()
elif k == '201':
	ddosscript()
elif k == '202':
	backdoorapk()
elif k == '203':
	termuxscript()
elif k == '204':
	pythontwitervot()
elif k == '205':
	niktosymfix()
elif k == '206':
	swapcli()
elif k == '207':
	fbrute()
elif k == '208':
	adfin()
elif k == '209':
	defidnotifer()
elif k == '220':
	pythem()
elif k == '221':
	sqlimaker()
elif k == '222':
	autoxjomla()
elif k == '223':
	penbox()
elif k == '224':
	smsidgo()
elif k == '225':
	grepmail()
elif k == '226':
	mdlimacrack()
elif k == '227':
	mamangkey()
elif k == '228':
	myenc()
elif k == '229':
	hashzer()
elif k == '230':
	errorcybertool()
elif k == '231':
	termuxgo()
elif k == '232':
	bolang()
elif k == '233':
	metainstall()
elif k == '234':
	ipscan()
elif k == '235':
	spammersys()
elif k == '236':
	androidpincrack()
elif k == '237':
	sir()
elif k == '238':
	zones()
elif k == '239':
	sheell()
elif k == '240':
	reaverwps()
elif k == '241':
	fluxion()
elif k == '242':
	phisinggame()
elif k == '243':
	anrspam()
elif k == '244':
	avarspam()
elif k == '245':
	genscript()
elif k == '246':
	ipmux()
elif k == '247':
	inmux()
elif k == '248':
	sqlscan()
elif k == '249':
	aocdeface()
elif k == '250':
	greenreaper()
elif k == '251':
	kawaibotnet()
elif k == '252':
	ihst()
elif k == '253':
	joomscan()
elif k == '254':
	shellnoob()
elif k == '255':
	fbupvdua()
elif k == '256':
	ufonett()
elif k == '257':
	dssst()
elif k == '258':
	routersploitsn()
elif k == '259':
	findmyhash()
elif k == '260':
	portwitness()
elif k == '261':
	icloud()
elif k == '262':
	gshtoolbox()
elif k == '263':
	termuxalpine()
elif k == '264':
	tmuxbunch()
elif k == '265':
	instagrambot()
elif k == '266':
	freefote()
elif k == '267':
	liteddos()
elif k == '268':
	myserver()
elif k == '269':
	cookiestealer()
elif k == '270':
	litefont()
elif k == '271':
	litescript()
elif k == '272':
	lolzrat()
elif k == '273':
	awsectools()
elif k == '274':
	termuxlazysqlmap()
elif k == '275':
	iesdeface()
elif k == '276':
	camstream()
elif k == '277':
	xeitcyber()
elif k == '278':
	phpbackconector()
elif k == '279':
	csrfpocmaker()
elif k == '280':
	thanatosarcher()
elif k == '281':
	darksploit()
elif k == '282':
	knock()
elif k == '283':
	aduasv()
elif k == '284':
	optiviaframework()
elif k == '285':
	dostattack()
elif k == '286':
	heartbleed()
elif k == '287':
	checkurl()
elif k == '288':
	debinject()
elif k == '289':
	clickjackingtester()
elif k == '290':
	androbugsframework()
elif k == '291':
	termuxspeak()
elif k == '292':
	tmvenom()
elif k == '293':
	termuxlazyscript()
elif k == '294':
	gloomframework()
elif k == '295':
	brutespray()
elif k == '296':
	sublister()
elif k == '297':
	fhxhashkiller()
elif k == '298':
	wsltools()
elif k == '299':
	termuxpackages()
elif k == '300':
	contexploit()
elif k == '301':
	spamtest()
elif k == '302':
	enigma()
elif k == '303':
	credover()
elif k == '304':
	allinwan()
elif k == '305':
	evilcreateframework()
elif k == '306':
	gabutz()
elif k == '307':
	iwpam()
elif k == '308':
	peframe()
elif k == '309':
	fbid()
elif k == '310':
	reconraven()
elif k == '311':
	hbxss()
elif k == '312':
	photon()
elif k == '313':
	hue()
elif k == '314':
	routerpi()
elif k == '315':
	apkbinder()
elif k == '316':
	haxorpi()
elif k == '317':
	nethunterlrt()
elif k == '318':
	awselbloganalyer()
elif k == '319':
	dockervernemq()
elif k == '320':
	kekescan()
elif k == '321':
	ctftool()
elif k == '322':
	cornershop()
elif k == '323':
	prex()
elif k == '324':
	jdvd()
elif k == '325':
	securityscripts()
elif k == '326':
	simplefilefinder()
elif k == '327':
	linset()
elif k == '328':
	mitmf()
elif k == '329':
	crackmapexec()
elif k == '330':
	deathstart()
elif k == '331':
	gcat()
elif k == '332':
	rocketman()
elif k == '333':
	honeypi()
elif k == '334':
	captipper()
elif k == '335':
	unifivouchergenerator()
elif k == '336':
	wplue()
elif k == '337':
	sescan()
elif k == '338':
	cantoolz()
elif k == '339':
	weaf()
elif k == '340':
	pythonlearning()
elif k == '341':
	cooker()
elif k == '342':
	ghostupdater()
elif k == '343':
	dockerwordpress()
elif k == '344':
	autotweet()
elif k == '345':
	pantesttools()
elif k == '346':
	exploit()
elif k == '347':
	pydeletepdfpages()
elif k == '348':
	pythonblackhat()
elif k == '349':
	pythonpenetrationtestingcookbook()
elif k == '350':
	termuxmpv()
elif k == '351':
	tuyulbtn()
elif k == '352':
	gadogado()
elif k == '353':
	cokrat()
elif k == '354':
	iesinstal()
elif k == '355':
	ffont()
elif k == '356':
	reconng()
elif k == '357':
	kickthemout()
elif k == '358':
	fuxploider()
elif k == '359':
	evilginx()
elif k == '360':
	alienhost()
elif k == '361':
	exploitoncli()
elif k == '362':
	uidsploit()
elif k == '363':
	trape()
elif k == '364':
	saint()
elif k == 'ABC' or k == 'abc':
	os.system('DarkFly')
else:
	print '[X] Sorry wrong input...'
	time.sleep('0.7')
	os.system('DarkFly')