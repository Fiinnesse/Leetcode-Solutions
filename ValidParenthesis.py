def isValid(s) -> bool:
        list = []

        dict = {")":"(", "]":"[", "}":"{"}

        for x in s:
            #print(x)
            if x in dict.values():
                  list.append(x)
                  #print("this is the list at beginning: ",list)
            elif list and dict[x] == list[-1]:
                  #print(list, " && ", dict[x]," == ",list[-1])
                  list.pop()
                  #print("this is the new list: ", list)
            else:
                  return False


        return list == []

s = "()[]}{"

print(isValid(s))

dict = {")":"(", "]":"[", "}":"{"}


list = ["("]
str = "("

print(list[-1])