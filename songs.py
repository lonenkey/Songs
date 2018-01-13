#/usr/bin/python3
import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

   
def insert_in_db (insert_name, insert_writer, insert_medium):
    db = client.songs
    db.songs.insert ({'name':insert_name, 'writer':insert_writer, 'medium':insert_medium})
    print(insert_name, insert_writer, insert_medium,' are inserted into.',db)

def main():
 
    print ('Menu:')
    print ('1:  Add a song')
    print ('2:  Search for a song by Title')
    print ('3:  Search for a song by Author')
    print ('4:  List all electric guitar songs')
    print ('5:  List all acousic guitar songs')
    print ('6:  List all songs')

    menu = input ()
    if menu == '1':
        print ('Enter song title')
        name_input = input ()
        print ('Enter the songwriters name')
        writer_input = input ()
        print ('What medium is the song played by, usually acoustic or electric')
        medium_input = input ()
        insert_in_db (name_input, writer_input, medium_input)
        print ('Name = ', name_input, 'Writer = ', writer_input, 'Medium = ', medium_input)


    elif menu == '2':
        print ('Enter title')
        name_input = input()
      
        db = client.songs
        col = db.songs
##        info = db.songs.find( { $text: { $search: name_input} } )
        print (info)
    elif menu == '3':
        print ('Thanks')
        print (menu)
    elif menu == '4':
        print ('Thanks')
        print (menu)
    elif menu == '5':
        print ('Thanks')
        print (menu)
    elif menu == '6':
      
        db = client.songs
        for song in db.songs.find():
            pprint.pprint(song)
##        col = db.songs
##       cur = col.find()
##        for doc in cur:
##            print (doc)
    else: 
        print ('Invalid selection.')

main()
