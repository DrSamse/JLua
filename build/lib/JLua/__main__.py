from os import get_terminal_size
from typing import Type
from lupa._lupa import LuaRuntime
import lupa._lupa

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

def SumString(table : list) -> str:
    sumstring = ""
    for string in table: sumstring += string
    return sumstring

def GetLuaString(obj) -> list:
    luastring = [ ]
    # print(type(obj))
    if type(obj) == type(dict()):
        luastring.append("\n{\n")
        for index, entry in enumerate(obj):
            luastring.append(str(entry) + " = " + SumString(GetLuaString(obj[entry])) + ",\n")
        luastring.append("}")

        luastring = SumString(luastring).split("\n")
        luastring.remove("")
        for i in range(1, len(luastring) - 1): 
            luastring[i] = "    " + luastring[i] + "\n"
        luastring[0] = luastring[0] + "\n"

    elif type(obj) == type(list()):
        sumstring = "{ "
        for entry in obj: sumstring += SumString(GetLuaString(entry)) + ", "
        sumstring += "}"
        sumStringList = sumstring.split("\n")
        for i in range(0, len(sumStringList) - 1):
            sumStringList[i] += "\n"
            luastring.append(sumStringList[i])
        luastring.append(sumStringList[len(sumStringList) - 1])

    elif type(obj) == type(str()):
        luastring.append("\"" + obj + "\"")

    elif type(obj) == type(int()):
        luastring = [ str(obj) ]

    else:
        luastring.append("\"" + repr(obj) + "\"")

    return luastring

# Decoding
def DecodeToDict(luaString : str = "", useDecoded : bool = False, decoded = None):
    lua = LuaRuntime()
    if not useDecoded:
        decoded = lua.eval(luaString)
    returnDict = { }
    for entry in decoded:
        try:
            attr = getattr(decoded, entry)
        except:
            attr = decoded[entry]

        if type(attr) == type(lua.eval("{ }")):
            attr = DecodeToDict(useDecoded=True, decoded=attr)
        # print(entry, attr)
        if type(entry) == type(int()): entry -= 1
        returnDict[entry] = attr
    return returnDict

class LuaCreatedClass(): pass  

def DecodeToClass(luaString : str = "", configClass = LuaCreatedClass(), useDecoded : bool = False, decoded = None):
    try:
        lua = LuaRuntime()
        if not useDecoded:
            decoded = lua.eval(luaString)
        for entry in decoded:
            # print(type(entry), entry)
            try:
                attr = getattr(decoded, entry)
            except TypeError:
                attr = entry
            if type(attr) == type(lua.eval("{ }")):
                if type(configClass) == type(LuaCreatedClass()):
                    attr = DecodeToClass(useDecoded=True, decoded=attr)
                else:
                    attr = DecodeToClass(configClass=getattr(configClass, entry), useDecoded=True, decoded=attr)
            setattr(configClass, entry, attr)
        return configClass
    except TypeError:
        raise TypeError("Not string type arg detected, class attributes can only be created of a string")

print(DecodeToClass(SumString(GetLuaString(testDictionary))))
