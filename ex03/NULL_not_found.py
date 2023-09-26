def NULL_not_found(object: any) -> int:
    ob_type = type(object)
    if object is None:
        print('Nothing:', object, ob_type)
    elif ob_type == float and object != object:
        print('Cheese:', object, ob_type)
    elif ob_type == int and object == 0:
        print('Zero:', object, ob_type)
    elif ob_type == str and object == '':
        print('Empty:', object, ob_type)
    elif ob_type == bool and object is False:
        print('Fake:', object, ob_type)
    else:
        print("Type not found")
        return 1
    return 0
