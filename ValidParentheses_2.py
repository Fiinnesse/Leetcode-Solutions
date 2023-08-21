def isValid(s) -> bool:
      list = []

      dict = {"(":")",
              "[":"]",
              "{":"}"}
      
      for x in dict:
            if x in dict:
                  list.append(x)
            elif len(list) == 0 or dict[list.pop()] != x:
                  return False
            if len(list) > 0:
                  return False

      return True      
      
      print(list)
        


s = "()[]}{"

print(isValid(s))
