### Soru 1 ###
from typing import Iterable
result=[]
def flatten(items):
    if isinstance(items, Iterable) and not isinstance(items, (str, bytes, int, float)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes, int, float)):
                for sub_x in x:
                    flatten(sub_x)
            else:
                result.append(x)
    else:
        result.append(items)
    return result

input_1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_1= flatten(input_1)
print(output_1)

## Soru 2  ###

def tersini_al(liste):
    liste.reverse()
    for i in liste:
        i.reverse()
    return liste
input_2=[[1, 2], [3, 4], [5, 6, 7]]
output_2 = tersini_al(input_2)
print(output_2)