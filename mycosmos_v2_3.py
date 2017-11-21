#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 2 has the programm as a function
# V.2.1 has a GUI too !!!!!

# sudo pip install --upgrade pip
import mechanize  #sudo pip install mechanize
import cookielib
import os

############# OUR FUNCTION ###############
def mycosmos_send_sms(login,password,recepient,msg):
	br = mechanize.Browser()
	br.set_handle_robots(False) 
	br.set_handle_refresh(False)
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	
	br.open('https://www.mycosmos.gr/')
	
	br.select_form(name="form")
	br['_user']=login
	br['_pass']=password 
	br.submit()
	# print br.title() # now I have logged IN !!!
	response = br.open('https://www.mycosmos.gr/?_task=websms&_action=plugin.websms')
	# print br.title() 
	
	req = br.click_link(text='Compose message')
	br.open(req)
	# print br.title() 
	
	br.select_form(nr=1)
	br['_to']=recepient
	br['_message']=msg 
	br.submit()
	print 'Your message should have been send normally !!' 
#########################################



############# LOAD CREDENTIALS ###############
path_here =  os.path.dirname(os.path.realpath(__file__))
credentials = open(path_here+os.path.sep+'mycosmos_logins.txt').readlines()
login = credentials[0]
password = credentials[1]
recepient = '6911111111'
msg = 'test SMS'

##############################################
'''
import wx
app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()
'''

def test_command(msg):
	print 'test_command function now runs!!!!'
	print msg


############## GUI ! ###############


from Tkinter import *

def show_entry_fields():
	# print("Recipient: %s\nMessage: %s" % (e1.get(), area.get("1.0",END)))
	path_here =  os.path.dirname(os.path.realpath(__file__))
	credentials = open(path_here+os.path.sep+'mycosmos_logins.txt').readlines()
	login = credentials[0]
	password = credentials[1]
	recepient = e1.get()
	msg = area.get("1.0",END)
	print("Recipient: %s\nMessage: %s" % (recepient, msg))
	#print 'type recepient = '+type(recepient)
	mycosmos_send_sms(login,password,recepient,msg)
	print 'Message was sent'
	master.quit()
	#root.quit()

master = Tk()
master.geometry("420x370")
Label(master, text="Recepient").grid(row=0)
Label(master, text="Message").grid(row=1)

e1 = Entry(master)
# e2 = Entry(master)

e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

area = Text(master)
area.grid(row=4, column=0,  #where it starts
	columnspan=2, # rowspan=2, 
	padx=2,pady=2, sticky=E+W+S+N)

# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(master, text='Send & Quit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Send & Quit', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
mainloop( )