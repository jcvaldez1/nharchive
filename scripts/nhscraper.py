import requests
import json
import datetime
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



''' ========== FUNCTIONS GO BELOW THIS LINE ========== '''

''' Retrieve the gallery's number of pages '''
def retrievePageCount():
    r = requests.get("https://nhentai.net/api/galleries/all")
    res = r.json()
    return res['num_pages']

''' Returns true if book_id is in page_no, otherwise false '''
def isBookIdInPage(book_id, page_no):
    r = requests.get("https://nhentai.net/api/galleries/all?page="+str(page_no))
    res = r.json()
    res_len = len(res['result'])
    for i in range(0, res_len):
        # print(res['result'][i]['id'], "==", book_id)
        if (res['result'][i]['id'] == book_id):
            return True
    return False

''' Retrieves all information in a page '''
def retrieveAllInfoInPage(page_no):
    r = requests.get("https://nhentai.net/api/galleries/all?page="+str(page_no))
    res = r.json()['result']
    return res

''' Given the page info JSON and the DB session,
    Save page information to the database '''
def saveInfo(res, db)
    for i in range(len(res)-1, -1, -1):
        # Get all necessary info
        id = res[i]['id']
        media_id = res[i]['media_id']
        title = res[i]['title']['english']
        title_pretty = res[i]['title']['pretty']
        scanlator = res[i]['scanlator']
        upload_date = res[i]['upload_date']
        pages = res[i]['num_pages']
        favorites = res[i]['num_favorites']
        tags = []
        character = []
        parody = []
        artist = []
        group = []
        for j in range(0, len(res[i]['tags'])):
            if (res[i]['tags'][j]['type'] == 'tag'): tags.append(res[i]['tags'][j]['name']])
            elif (res[i]['tags'][j]['type'] == 'character'): character.append(res[i]['tags'][j]['name'])
            elif (res[i]['tags'][j]['type'] == 'parody'): parody.append(res[i]['tags'][j]['name'])
            elif (res[i]['tags'][j]['type'] == 'artist'): artist.append(res[i]['tags'][j]['name'])
            elif (res[i]['tags'][j]['type'] == 'group'): group.append(res[i]['tags'][j]['name'])

        # print("Book ID:", id)
        # print("Media ID:", media_id)
        # print("Title:", title)
        # print("Short Title:", title_pretty)
        # print("Scanlator:", scanlator)
        # print("Upload Date:", datetime.datetime.fromtimestamp(int(upload_date)).strftime('%Y-%m-%d %H:%M:%S'))
        # print("Pages:", pages)
        # print("Favorites Count:", favorites)
        # print("Tags:", tags)
        # print("Character:", character)
        # print("Parody:", parody)
        # print("Artist(s):", artist)
        # print("Group:", group)
        # print()



''' ========== MAIN CODE GOES HERE ========== '''
print(retrieveAllInfoInPage(1))
