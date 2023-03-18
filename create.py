from model import Quotes, Authors
import json

def upload_data():

    with open("authors.json") as f:
        authors = json.load(f)
        for a in authors:
            author = Authors()
            author.fullname = a['fullname']
            author.born_date = a['born']
            author.born_location = a['born_location']
            author.description = a['description']
            author.save()

    with open("quotes.json") as f:
        quotes = json.load(f)
        for q in quotes:
            author = Authors.objects(fullname = q['author']).first()
            if author.id:
                quote = Quotes()
                quote.tags = q['tags']
                quote.author = author.id
                quote.quote = q['quote']
                quote.save()
            else:
                print("Unknown author")

if __name__ == '__main__':
    upload_data()