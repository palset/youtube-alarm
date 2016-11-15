import sys
import time
import string
import urllib
import webbrowser
sleeptimesecs=int(sys.argv[1])*60*60
time.sleep( sleeptimesecs )
query=sys.argv[2];
url="https://www.youtube.com/results?search_query="+query
response=urllib.urlopen(url)
html=response.read()
linkbeg=html.find("/watch?v")
linkend=linkbeg+21;
linkbeg=linkbeg+9
html=html[linkbeg:linkend]
finalurl="https://www.youtube.com/watch?v="+html
webbrowser.open(finalurl)
