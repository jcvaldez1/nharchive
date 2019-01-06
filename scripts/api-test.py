import json
import requests
import sys
# test book retrieval

MAX_ID = 256400
BACKEND_URL = "http://localhost:8000/manga/"

def clean(book):
    
    #
    book["book_id"] = book.pop("id")

    # remove the images portion since it only just give the dimensions
    book.pop["images"]

def register_title(title_dict):
    
    pass

def register_book():
    pass

def tag_check():
    pass

def scrape():

    for x in range(0,MAX_ID):
        book_sample = requests.get("https://nhentai.net/api/gallery/" + str(x))
        exists_on_db = requests.get(BACKEND_URL + str(x))
        if(book_sample.ok)and(exists_on_db.ok):

            # book_sample should now be a dictionary containing the book info
            book_sample = book_sample.json()

            # rename some of the keys to be inline with the backend attr names
            # for serialization
            clean(book_sample)

            # create new title
            title = register_title(book_sample["title"])

            # check the tag and tag_type if it exists
            # create new instance if it doesnt, do nothing otherwise
            # tag_ids -> list of all tag_ids of the tags that this book has
            tag_ids = tag_check(book_sample["tags"])

            # create the Book instance
            book_sample["title"] = title
            register_book(book_sample, title, tag_ids)
        else:
            print(book_sample.status_code)



if __name__ == "__main__":
    # execute only if run as a script
    scrape()
