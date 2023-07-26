# a = my_function(["Giorgio", "Irene", "Antonio", "Carla"], ["o", "e"])
# print(a)

# result ["Giorgio", "Irene", "Antonio"]


def my_function(arr1, arr2):
    result = []
    for x in arr1:
        for y in arr2: 
            for xa in x: 
                last_words_index = arr1[len(arr1) - 1]
                # print(arr1.index(last_words_index), len(arr1), xa)
                if last_words_index == arr1[len(arr1) - 1]:
                    print(last_words_index, arr1[len(arr1) - 1])
                    
                # if(xa == y):
                #     result.append(x)
                #     # print([*set(result)])


a = my_function(["Giorgio", "Irene", "Antonio", "Carla", "Arthur", "Steve"], ["o", "e"])
# print(a) #["Giorgio", "Irene", "Antonio"]