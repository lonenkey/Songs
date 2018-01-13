#/usr/bin/python3
import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

   
def insert_in_db (insert_name, insert_writer, insert_medium):
    db = client.songs
    db.songlist.insert ({'name':insert_name, 'writer':insert_writer, 'medium':insert_medium})
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
        info = db.songlist.find_one({"name":name_input})
        print (info)

    elif menu == '3':
        print ('Enter the songwriters name')
        writer_input = input ()
        db = client.songs
        collection = client.songlist
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
        for song in db.songlist.find():
            pprint.pprint(song)
    else: 
        print ('Invalid selection.')

main()
