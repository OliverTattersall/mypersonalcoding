class chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

class book:
    def __init__(self, author, length, title, language):
        self.author = author
        self.length = length
        self.title = title
        self.language = language




poop = book("Poopy", 200, "The chronicles of poopy", "english")
book2 = book("Bamn", 2, "bOom", 'english')


print(poop.language)
