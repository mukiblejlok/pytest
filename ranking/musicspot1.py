#get data from Musicspot
#and save it to sqlite

#imports
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import re
import json


######################################
#GET THE DATA FROM URL
#get url (it can be more than one)
urls = [
'http://musicspot.pl/glebogryzarka/940/Top_160_singli_2000-2009_(miejsca_40-1)/',
'http://musicspot.pl/glebogryzarka/937/Top_160_singli_2000-2009_(miejsca_80-41)/',
'http://musicspot.pl/glebogryzarka/934/Top_160_singli_2000-2009_(miejsca_120-81)/',
'http://musicspot.pl/glebogryzarka/933/Top_160_singli_2000-2009_(miejsca_160-121)/']

rank_list = dict()

for url in urls:
	#read it
	connection = urllib.request.urlopen(url)
	html = connection.read()

	#make it a BeatufiulSoup Object
	soup = BeautifulSoup(html, "html.parser")
	html = soup.find_all("div", "post")
	soup = BeautifulSoup(str(html), "html.parser")
	#get all paragraps in a list
	paragraphs = soup.find_all('p')
	#define an initial position
	pos = '0'
	for p in paragraphs:
		#check if it is a link with position and name
		if re.search('>[0-9]+\. ', str(p)): 
			#this is a link with data
			pos = re.findall('>([0-9]+)\. ',str(p))[0]
			href = re.findall('href="(.+)" ',str(p))[0]
			artist = re.findall('>[0-9]+\. (.+) "',str(p.decode(formatter=None)))[0]
			title = re.findall('>[0-9]+\. .+ "(.+)"',str(p.decode(formatter=None)))[0]
			#rank update
			rank_list[pos] = {'href' : href, 'artist': artist, 'title': title, 'desc': ''} 
		#if not with position then with description
		else:
			desc = p.text
			#rank update
			rank_list[pos]['desc'] = desc


print("Retrieved: "+ str(len(rank_list)) + " records.")
connection.close()

###################################################################
#save to sqlite
dbName = 'Afro_Top160'

#make the connection
conn = sqlite3.connect(str(dbName)+'.sqlite')
#set the cursor on the connection
cur = conn.cursor()

#execute the SQL Command
#that removes all tables
cur.execute('DROP TABLE IF EXISTS "Ranking" ')

#Create SQL table Counts
cur.execute('''
CREATE  TABLE "Ranking" 
("ind" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
"position" INTEGER NOT NULL , 
"artist" VARCHAR (200) NOT NULL , 
"title" VARCHAR (200) NOT NULL , 
"href" VARCHAR (200), 
"description" TEXT ) ''')

for el in rank_list:
	cur.execute('INSERT INTO "Ranking" VALUES (NULL, ?, ?, ?, ?, ?)', (el, rank_list[el]['artist'], rank_list[el]['title'], rank_list[el]['href'], rank_list[el]['desc'], ) )
	#print(rank_list[el])


#this is important 
#this actually writes the data to the SQLite database
conn.commit()


#for i in range(5):
#	searchstring = rank_list[str(i+1)]['artist'] + " " + rank_list[str(i+1)]['title'] 
#	serviceurl = 'https://api.spotify.com/v1/search?'
#	url = serviceurl + urllib.parse.urlencode({'q': searchstring, 'type': 'track', 'limit' : 1})
	
#	json_in = urllib.request.urlopen(url).read().decode('UTF-8')
#	result = json.loads(json_in)
	#print (json.dumps(result, indent=4))

#	print(str(result['tracks']['items'][0]['uri']))






