def field(items, *args):
    assert len(args) > 0
    result = []
    dict_count = 0
    for item in items:
        result.append(dict())
        for key in item.keys():
            if key in args and item[key] is not None:
                result[dict_count].update({key: item[key]})
        dict_count += 1

    if len(args) == 1:
        is_first = True
        for dictionary in result:
            if len(dictionary) == 0: continue
            # print(f"'{dictionary[args[0]]}'", end='') if is_first else print(f", '{dictionary[args[0]]}'", end='')
            is_first = False

    elif len(args) > 1:
        is_first = True
        for dictionary in result:
            if len(dictionary) == 0: continue
            # print(dictionary, end='') if is_first else print(f", {dictionary}", end='')
            is_first = False
    return [x[args[0]] for x in result]


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': None},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

# field(goods, 'title', 'color')
