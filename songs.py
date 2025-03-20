#/usr/bin/python3
import pymongo
import pprint
import os
import re
from pymongo import MongoClient

client = MongoClient()
menu = '0'

   
def insert_in_db (insert_name, insert_writer, insert_medium):
    db = client.songs
    db.songlist.insert_one ({'name':insert_name, 'writer':insert_writer, 'medium':insert_medium})
    print(insert_name, insert_writer, insert_medium,' are inserted into.',db)

def main(): 
    menu = '0'
    while menu != 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Hi!  This is a database of all songs that can be played by Lon Andrew Enkey')
        print (' ')
        print ('Menu:')
        print ('1:  Add a song')
        print ('2:  Search for a song by Title')
        print ('3:  Search for a song by Author')
        print ('4:  List all electric guitar songs')
        print ('5:  List all acousic guitar songs')
        print ('6:  List all songs')
        print ('7:  Total number of songs')
        print ('q:  To quit')

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
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()


        elif menu == '2':
            print ('Enter title')
            name_input = input()
            db = client.songs
            collection = client.songlist
            by_title = db.songlist.find({'name':{'$regex':'.*' + name_input + '.*','$options': 'i'}})
            for song in by_title:
                pprint.pprint (song['name'] + ' (by ' + song['writer'] + ', on ' + song['medium'] + ')')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()
  
        elif menu == '3':
            print ('Enter the songwriters name')
            writer_input = input ()
            db = client.songs
            collection = client.songlist
            by_songwriter = db.songlist.find({'writer':{'$regex':'.*' + writer_input + '.*' ,'$options':'i'}})
            for song in by_songwriter:
                pprint.pprint (song['name'] + ' (by ' + song['writer'] + ', on ' + song['medium'] + ')')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

        elif menu == '4':
            db = client.songs
            collection = client.songlist
            all_electric = db.songlist.find({'medium':{'$regex': '.*' + 'E' + '.*','$options':'i'}})
            for song in all_electric:
                pprint.pprint (song['name'] + ' (by ' + song['writer'] + ')')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

        elif menu == '5':
            db = client.songs
            collection = client.songlist
            all_acoustic = db.songlist.find({'medium':{'$regex':'.*'+'A'+'.*','$options':'i'}})
            for song in all_acoustic:
                pprint.pprint (song['name'] + ' (by ' + song['writer'] + ')')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

        elif menu == '6':
            db = client.songs
            full_list = db.songlist.find()
            for song in full_list:
                pprint.pprint (song['name'] + ' (by ' + song['writer'] + ')')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

        elif menu == '7':
            db = client.songs
            song_count = db.songlist.find().count()
            print ('There are ', song_count, ' songs in the database.')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

        elif menu == 'q':
            print (' ')

        else: 
            print ('Invalid selection.')
            print (' ')
            print ('Press enter to continue, q to quit')
            menu = input ()

main()
