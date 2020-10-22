class Test():
    var1 = 10
    var2 = "Test"
    def __init__(self):
        pass

    def Test(self):
        pass

    def __repr__(self):
        return "var1 = " + str(self.var1) + "  var2 = " + self.var2

testDictionary = {
    "var1" : 30,
    "var2" : 50,
    "testClass" : Test(),
    "test" : {
        "moreTest" : "Success",
        "extraTest" : {

        },
        "listTest" : [ 10, 20, "Nice" ]
    }
}

otherDict = {
    1, 2, 3, 4
}