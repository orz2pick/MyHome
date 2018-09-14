# coding=utf8
# 颜色控制：https://www.cnblogs.com/hellojesson/p/5961570.html
import urllib
import re
import platform 
from skimage import io,data
import os
import time
import matplotlib.pyplot as plt
import requests
response =  urllib.urlopen('https://orz2pick.github.io/MyHome/worddatabase/db.txt')  
words = response.read()
data=[]
for s in words.split('\n'):
	ind=[]
	for j in s.split(','):
		ind.append(j)
	data.append(ind)
head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Referer': 'http://www.mzitu.com/37288/3'}
score=0
proficiency=[]

path='./'
name=''
def clear():
	OS = platform.system()
	#clear screen
	if OS[0]=='D' or OS[0]=='L':
		os.system('clear')
	else:
		os.system('cls')
def show(li):

	n=1
	for i in li:
		print n,data[i][0],'\t',data[i][1],'\t',data[i][2]
		n+=1
def check(s):
	print 'Congratulations!'
def random_choose(p):
	return [1,2]
def level(scores):
	return u'青铜'
def init():
	print 1

def update():
	global name
	global score
	OS = platform.system()
	#clear screen
	
	clear()

	print 'Dear Warrior '+name+'! Your score is:',score
	print 'Brave Warrior '+name+'! Your level is:',level(score)
	print '\n'*3
	while True:
		clear()
		print 'Dear Warrior '+name+'! Your score is:',score
		print 'Brave Warrior '+name+'! Your level is:',level(score)
		print '\n'*3
		rdmlist = random_choose(proficiency)
		show(rdmlist)
		data2=[]
		for i in rdmlist:
			data2.append(data[i])
		flag = raw_input("Tell me which words you are already proficient in(if there isn't ,type 0):")
		
		if flag == '0':
			clear()
			print 'Dear Warrior '+name+'! Your score is:',score
			print 'Brave Warrior '+name+'! Your level is:',level(score)
			print '\n'*3
			for i in [0,1]:
				clear()
				print 'Dear Warrior ' +name+'! Your score is:',score
				print 'Brave Warrior '+name+'! Your level is:',level(score)
				print '\n'*3
			#for i in [3,1,5,4,0,2]:
				print data2[i][2]
				know=raw_input("Tell me the word in English(Or type 1 to find help): ")
				
				if know=='1':
					print data2[i][1]
					know2=raw_input("Tell me the word in English(There is no help ^-^): ")
					if data2[i][0]==know:
						print 'Yes,you are right, I will plus your score by one.'
						score+=1
						check(score)
					else:
						print 'Sorry, you are wrong, the correct version is:',data2[i][0]
						score-=0.66
				elif data2[i][0]==know:
					print 'Yes,you are right, I will \033[4;31;43mplus your score by one.\033[0m'
					score+=1
					check(score)
				else:
					print("\033[4;31;43m%s\033[0m%s\033[1;34;46m%s\033[0m" % ("Sorry, you are wrong,"," the correct version is:",data2[i][0]))
					score-=0.34
					#print '\033[4;31;43mSorry, you are wrong,\033[0m the correct version i',data2[i][0]
				time.sleep(1)
def welcome():
	global path 
	global name
	print 'Brave Warrior,Welcome to "Dragon-Words" game!'
	flag = raw_input("Do you wanna to read rules?(type y/n)")
	if flag == 'y':
		img=io.imread("https://orz2pick.github.io/MyHome/Photos/a.jpg")
		io.imshow(img)
		io.show()
	usrname=raw_input('Please tell me your usrname(MUST In English):')
	path+=usrname
	name=usrname
	init()
	while True:
		update()
welcome()
