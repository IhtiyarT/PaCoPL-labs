class Unique(object):
    def __init__(self, items, **kwargs):
        if "ignore_case" in kwargs.keys():
            self.__ignore_case = kwargs.get("ignore_case")
        else: self.__ignore_case = False
        self.__data = items
        self.__elems_set = set()
        self.__number = -1

    def __next__(self):
        self.__number += 1
        try:
            if isinstance(self.__data[self.__number], str):
                obj = self.__data[self.__number].lower() if self.__ignore_case else self.__data[self.__number]
                if obj not in self.__elems_set:
                    self.__elems_set.add(obj)
                    return obj
                else:
                    return self.__next__()
            elif self.__data[self.__number] not in self.__elems_set:
                self.__elems_set.add(self.__data[self.__number])
                return self.__data[self.__number]
            else:
                return self.__next__()
        except IndexError:
            self.__number -= 1
            raise StopIteration

    def __iter__(self):
        return self


data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# for i in Unique(data1):
#     print(i)

# for i in Unique(data2, ignore_case=True):
#     print(i)
