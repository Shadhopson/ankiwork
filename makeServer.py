import BaseHTTPServer
import random
import sqlite3
import simplejson

def loadDeck(fileName):
    deck = []
    connect = sqlite3.connect(fileName)
    connect.row_factory= sqlite3.Row
    cur = connect.cursor()
    cur.execute('SELECT * FROM notes')
    for row in cur.fetchall():
	deck.append(note(row['sfld'],row['flds'].split('\x1f')))
    return deck
        
class note:
    def __init__(self, front, back):
	self.front = front
	self.back = back

    def toJson(self):
	return simplejson.dumps({
		'front' : self.front,
		'back' : self.back
	})

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class ankihandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
            ranNum = random.randrange(0, len(deck))
            card = deck[ranNum].toJson()
	    self.wfile.write("""HTTP/1.1 200 ok
content-type:text/html

%s """% card)
deck =loadDeck('/home/shad/Downloads/collection.anki2')
run(handler_class=ankihandler)
