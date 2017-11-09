class A:
    def get(self):
        print "GET of A"

    def post(self):
        print "POST OF A"

class B(A):

    def post(self):
        print "POST OF B"

    def put(self):
        print "PUT OF D"

class C(A):
    def get(self):
        print "GET of C"

    def post(self):
        print "POST OF C"

    def put(self):
        print "PUT OF D"

class D(B,C):

    def put(self):
        print "PUT OF D"

if __name__ == '__main__':
    d1 = D()
    # d1.get()
    # d1.post()
    # d1.put()
