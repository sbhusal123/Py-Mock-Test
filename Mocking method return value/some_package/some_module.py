class someHelperClass:

    def some_method(self):
        return True



class someClass:

    def call(self):
        sm = someHelperClass()
        if sm.some_method():
            return "Returned True"
        else:
            return "Returned False"
