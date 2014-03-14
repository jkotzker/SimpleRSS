import feedparser
import webbrowser
from richxerox import *

def Menu():
	print 'What would you like to do?'
	print ' [1] Parse a feed and show recent entries'
	print ' [2] Parse a feed from the contents of my clipboard'
	print ' [3] Open an entry in a browser'
	print ' [4] Exit the program'
	choice = raw_input()
	choice = int(choice)
	if choice == 1:
		ParseFeed()
	elif choice == 2:
		ParseFromClip()
	elif choice == 3:
		OpenInBrowser()
	elif choice == 4:
		exit()
	else:
		print 'Invalid input'
		Menu()

def Feed():
	print 'What feed are we using?'
	feed = raw_input()
	d = feedparser.parse(feed)
	return d

def ParseFeed():
	d = Feed()
	feedTitle = d['feed']['title']
	subTitle = d.feed.subtitle
	print feedTitle
	print subTitle
	for post in d.entries:
		print post.title + ": " + post.link + "\n"
	Menu()

def ParseFromClip():
	feed = paste(format='text')
	feed = str(feed)
	d = feedparser.parse(feed)
	feedTitle = d['feed']['title']
	subTitle = d.feed.subtitle
	print feedTitle
	print subTitle
	for post in d.entries:
		print post.title + ": " + post.link + "\n"
	Menu()

def OpenInBrowser():
	d = Feed()
	print 'Which article would you like to read? Please input its index number, 0 being the index of the first article.'
	article = raw_input()
	article = int(article)
	webbrowser.open(url = d.entries[article]['link'],new=0)
	Menu()

Menu()