# <img src="https://ee5817f8e2e9a2e34042-3365e7f0719651e5b8d0979bce83c558.ssl.cf5.rackcdn.com/python.png" width="48"><img src="http://s32.postimg.org/ujg7qagp1/monitoring_icon.png" width="48">website-monitor
Python program to monitor site uptime and send alert via twitter using tweepy library.

<img src="https://pbs.twimg.com/profile_images/709093757854072832/_m_AHgyP_400x400.jpg" width="100">

Coded by [@magic_coding](http://www.twitter.com/magic_coding)

**Installation:**

- python2.7 [Download link](https://www.python.org/download/releases/2.7/)
- You will need to install Python's tweepy & requests library:

Tweepy library
```
pip install tweepy
```
Requests library
```
pip install requests
```

**How to use?**

1. [Download](https://github.com/magic-coding/website-monitor/archive/master.zip) & Extract `website-monitor.zip` file.
2. Edit `check.py` file using any code editor.
3. You will need to create an app account on https://dev.twitter.com/apps
	1. Sign in with your Twitter account
	2. Create a new app account
	3. Modify the settings for that app account to allow read & write
	4. Generate a new OAuth token with those permissions

4. Following these steps will create 4 tokens that you will need to place in the `check.py` file:
```
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxx"
```
5.on `line 22` add your website url with `http://` or `https://` and your twitter account id "[Get twitter account id from here](http://gettwitterid.com)"
```
clients = {"website-url":"twitter-account-id"}
```
6.Save `check.py` file and enjoy.

**How it works?**

The function `site_up()`, runs through the sites you list and checks each one looking for a 200 status response code, if it receives anything else, it passes it on to a temporary dictionary that the second function is watching and deletes it from the main dictionary, after `15 minutes` of being sat in the temporary dictionary it checks it again, if it is still returning anything other that a 200 response then it fires direct message to the twitter account (ID) alerting you there is an issue.

Every `15 minutes` it checks whether it is back up or not, each time sending direct message, once it is back up it fires another direct message saying the site is once again live - it deletes it from the temporary dictionary and adds the site back into the main pool.

You can change the time of checker from here `time.sleep(900) # sleeps 15 mins`:

```
def site_down():
	''' function to monitor site down time '''
	while True:
		time.sleep(900) # sleeps 15 mins
		for client, twitter_acc in temp_dic.items():
		......
		.....
```
it set to `900` and that's mean `15 mins`.

**Add more website to monitor**

If you have clients site and you decided to add them in the monitor please edit `line 22` to be like this:

```
clients = {"website-url1":"twitter-account-id1", "website-url2":"twitter-account-id2", "website-url3":"twitter-account-id3"}
```

**Have a problem?**

If you're having issues with or have questions about the program Please open new issue or contact with me via Twitter [@magic_coding](http://www.twitter.com/magic_coding)


**Conclusion**

In Conclusion hope you enjoy with this small programe and don't forget to follow me to get more free open source programes.

**License:**

As of May 19, 2016 website-monitor is licensed under the GPLv3+: http://choosealicense.com/licenses/gpl-3.0
