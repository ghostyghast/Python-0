def all_thing_is_obj(object: any) -> int:
    ob_type = type(object)
    if ob_type == int or ob_type == float:
        print('Type not found')
    elif ob_type == str:
        print("Brian is in the kitchen :", ob_type)
    else:
        name = str(ob_type.__name__)
        print(name.capitalize(), ':', ob_type)
        return 42
