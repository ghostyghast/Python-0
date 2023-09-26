def all_thing_is_obj(object: any) -> int:
    ob_type = type(object)
    types = [list, tuple, set, dict]
    if ob_type == str:
        print("Brian is in the kitchen :", ob_type)
        return 42
    for x in types:
        if ob_type == x:
            print(ob_type.__name__.capitalize() + ':', ob_type)
            return 42
    print('Type not found')
    return 42
