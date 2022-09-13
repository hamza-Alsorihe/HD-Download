import time
import os
try:
	import pafy
	import requests
except:
	os.system('clear')
	os.system('pip install pafy')
	os.system('pip install youtube-dl')
	os.system('pip install requests')
try:
	os.mkdir('/sdcard/HD-Download/')
	os.mkdir('/sdcard/HD-Download/files/')
	os.mkdir('/sdcard/HD-Download/YouTube')
	os.mkdir('/sdcard/HD-Download/YouTube/video')
	os.mkdir('/sdcard/HD-Download/YouTube/audio')
except:
	print('hsnzs')

############
c = '\033[2;36m' #سماوي
r = '\033[1;91m' #احمر 
b = '\033[1;34m' # ازرق 
gr = '\033[0;32m' #اخضر غامق
g = '\033[0;92m' #اخضر فاتح 
W = '\033[1;37m' #ابيض
BL = '\033[1;30m' #رصاصي
Y = '\033[1;33m' #اصفر
############

os.system('clear')
print(BL+'='*30)
print(Y+'[1] - '+g+'Download '+r+'YouTub\n'+Y+'[2] - '+g+'file')
print(BL+'='*30)
youtub=input(g+'> '+Y)
print(BL+'='*30)
if youtub=='1':
        os.chdir('/sdcard/HD-Download/YouTube')
        print (BL+' ='*30)
        print (r+'     ______________________________________________')
        print (r+'    /                                              \\')
        print (r+'   ||                                              ||')
        print (r+'   ||                ______________                ||')
        print (r+'   ||               //   ______   \\\               ||')
        print (r+'   ||               ||  |      \\\  \\\              ||')
        print (r+'   ||               ||  |      //  //              ||')
        print (r+'   ||               ||  |_____//  //               ||')
        print (r+'   ||               \\____________//                ||')
        time.sleep(1)
        print (r+'   ||                                              ||')
        print (r+'   ||                                              ||')
        print (r+'    \\______________________________________________/')
        time.sleep(1)
        print (BL+' ='*30)
        url =input(b+' enter your url: '+c)
        print(BL+'='*30)
        print(g+' Do you need download\n'+Y+'[1] - '+b+'video\n'+Y+'[2] - '+b+'audio')
        print(BL+'='*30)
        an =input(Y+'> ')
        print(BL+'='*30)
        if an=='1':
                os.chdir('/sdcard/HD-Download/YouTube/video')
                video=pafy.new(url)
                print('Title:',video.title)
                streams=video.streams
                for i in streams:
                	print(i)
                print('='*30)
                print(gr+' enter is '+r+'0 '+b+'or '+r+'1 '+b+'or '+r+'full '+b)
                print('='*30)
                pafy1=int,str(input('enter your andex: '+r))
                if pafy1==0:
                        streams[0].download()
                elif pafy1==1:
                        streams[1].download()
                elif 'FULL':
                        video=pafy.new(url)
                        print('Title:',video.title)
                        best=video.getbest()
                        best.download()
        elif an =='2':
                        os.chdir('/sdcard/HD-Download/YouTube/audio')
                        video=pafy.new(url)
                        print('Title: ',video.title)
                        audiostreams=video.audiostreams
                        for i in audiostreams:
                        	print(i)
                        print('='*30)
                        print(gr+' enter is '+r+'0 '+b+'or '+r+'1'+b)
                        print('='*30)
                        os.chdir('/sdcard/hamza/audio')
                        pafy1=int(input('enter your andex: '+r))
                        if pafy1==0:
                                audiostreams[0].download()
                        elif pafy1==1:
                                audiostreams[1].download()







elif youtub== '2':
                N=input('Do you download files: ')
                if N=='yes':
                        print('download files')
                        url = input('enter your url: ')
                        u=str(input('enter the name file: '))
                        r=requests.get(url)
                        os.chdir('/sdcard/HD-Download/files/')
                        with open(u,'wb') as file:
                            file.write(r.content)
else:
        print('exit')
