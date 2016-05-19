# <img src="https://ee5817f8e2e9a2e34042-3365e7f0719651e5b8d0979bce83c558.ssl.cf5.rackcdn.com/python.png" width="48"><img src="http://s32.postimg.org/ujg7qagp1/monitoring_icon.png" width="48">website-monitor
Python program to monitor site uptime and send alert via twitter using tweepy library.

coded by http://www.twitter.com/magic_coding


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

1. [Download](https://github.com/magic-coding/url-scanner/archive/master.zip) & Extract website-monitor.zip file.
2. Edit `check.py` file using any code editor.
3. You will need to create an app account on https://dev.twitter.com/apps
	1. Sign in with your Twitter account
	2. Create a new app account
	3. Modify the settings for that app account to allow read & write
	4. Generate a new OAuth token with those permissions

4. Following these steps will create 4 tokens that you will need to place in the check.py file:
```
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxx"
```
5. on line 19 add your website url with http:// and your twitter account id "Get twitter account id from here" [http://gettwitterid.com](http://gettwitterid.com)
```
clients = {"website-url":"twitter-account-id"}
```
6. Save check.py file and enjoy.


**Have a problem?**

If you're having issues with or have questions about the program Please open new issue or contact with me via Twitter [@magic_coding](http://www.twitter.com/magic_coding)


**Conclusion**

In Conclusion hope you enjoy with this small programe and don't forget to follow me to get more free open source programes.

**License:**

As of May 19, 2016 url-scanner is licensed under the GPLv3+: http://choosealicense.com/licenses/gpl-3.0
