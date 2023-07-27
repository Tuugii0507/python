# a = my_function(["Giorgio", "Irene", "Antonio", "Carla"], ["o", "e"])
# print(a)

# result ["Giorgio", "Irene", "Antonio"]


def my_function(arr1, arr2):

    result = []
    for x in arr1:
        for y in arr2: 
            for xa in x:
                if (arr1.index(x) == len(arr1) - 1 ):
                    return [*set(result)]
                elif (xa == y):
                    result.append(x) 
                    
a = my_function(["Giorgio", "Irene", "Antonio", "Carla",], ["o", "e"])
print(a) #["Giorgio", "Irene", "Antonio"]