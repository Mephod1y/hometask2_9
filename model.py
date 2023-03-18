from mongoengine import *

connect(host="mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9", ssl=True)


class Authors(Document):
    fullname = StringField(max_length=500)
    born_date = StringField(max_length=500)
    born_location = StringField(max_length=500)
    description = StringField(max_length=5000)


class Quotes(Document):
    tags = ListField(StringField(max_length=500))
    author = ReferenceField(Authors)
    quote = StringField(max_length=500)

