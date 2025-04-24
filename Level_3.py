List = [12, 15, 8, 3, 5]




def findMaxInList(List):
    Max = List[0]
    for i in List:
        if i > Max:
            Max = i
    return Max


print(findMaxInList(List))
