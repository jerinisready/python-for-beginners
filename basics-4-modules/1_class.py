class Book:
    def __init__(self):
        auther = ""
        book = ""
        price = ""

    def set_book(self, book):
        self.book = book

    def set_auther(self, auther):
        self.auther = auther

    def set_price_in_INR(self,rupees):
        self.price = rupees

    def get_price_in_USD(self):
        return self.price/67.0    # Convertion to USD

    def desc(self):
        return """{0.book} is one of the Famous Book, Written By {0.auther},
        and is available on rate Rs.{0.price}/- in India """.format(self)


if __name__ == '__main__':
        myBook = Book()
        myBook.set_book("HALF GIRL FRIEND")
        myBook.set_auther("Chethan Bhagat")
        myBook.set_price_in_INR(130.66)
        print myBook.desc()
        print "BOOK IS ALSO AVAILABLE IN USA @ $%.2f " % myBook.get_price_in_USD()
