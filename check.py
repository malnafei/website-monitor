#  -*- coding: utf-8 -*-
#  coded by @magic_coding (icoder@mail.com)
#  Twitter: @magic_coding

from threading import Thread
import requests
import time
import tweepy
import thread

consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# list of sites to track along with twitter account to send the alert
# url should be with http://
# This site (http://downsitecheck.com/) still down you can use it for test.
clients = {"website-url":"twitter-account-id"}
temp_dic = {}

def twitter_acc_sender(input_message, msg_to):
	''' function to send twitter message '''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	print "Authenticated as: %s" % api.me().screen_name
	to = msg_to
	api.send_direct_message(user_id = to, text = input_message)
	print "Aleart message sent!"

def site_up():
	''' function to monitor up time '''
	while True:
		for client, twitter_acc in clients.items():
			try:
				r = requests.get(client)
				code = r.status_code
				print code
				if code == 200:
					print client, "Site is ok"
					time.sleep(60) # sleep for 1 min
				else:
					print client, 'Site first registered as down - added to the "site down" monitoring'
					temp_dic[client]=twitter_acc
					del clients[client]
			except requests.ConnectionError:
				print client, 'Site first registered as down - added to the "site down" monitoring'
				temp_dic[client]=twitter_acc
				del clients[client]

def site_down():
	''' function to monitor site down time '''
	while True:
		time.sleep(900) # sleeps 15 mins
		for client, twitter_acc in temp_dic.items():
			try:
				r = requests.get(client)
				if r.status_code == 200:
					print client, "Site is back up!"
					twitter_acc_sender('Good news🎉\nYour site '+client+' is back up✅\n\n----\nThis program coded by @magic_coding', twitter_acc)
					clients[client]=twitter_acc
					del temp_dic[client]
				else:
					twitter_acc_sender('🚩New Alert🚩\n\nHi Admin,\n\nWe noticed that your site '+client+' was down⚠️\n\n----\nThis program coded by @magic_coding', twitter_acc)
					print client, "Site Currently down - alert sent"
			except requests.ConnectionError:
					twitter_acc_sender('🚩New Alert🚩\n\nHi Admin,\n\nWe noticed that your site '+client+' was down⚠️\n\n----\nThis program coded by @magic_coding', twitter_acc)
					print client, "Site Currently down - alert sent"
t1.start()
t2.start()