nested_json = {
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "geo": [
            {
            "lat": 40.7128,
            "lng": -74.0060},
            {
            "lat": 40.7128,
            "lng": -74.0060}]

    }}


def flatten_json(nested_json):
    flat_json = {}

    def flatten(element, parent_key=''):

        if isinstance(element, dict):
            for key in element:

                flatten(element[key], parent_key + key + '.')
        elif isinstance(element, list):
            for index, item in enumerate(element):
                flatten(item, parent_key + str(index) + '.')
        else:
            print("going in else")
            print(f"parent_key[:-1]:{parent_key[:-1]}")
            print(f"element:{element}")
            flat_json[parent_key[:-1]] = element

    flatten(nested_json)
    print( flat_json)
    unflatten_json(flat_json)



def unflatten_json(flat_json):
    # nested_json = {}
    #
    # for flat_key, value in flat_json.items():
    #     keys = flat_key.split('.')
    #     current_level = nested_json
    #
    #     for key in keys[:-1]:
    #         if key.isdigit():  # Check if the key should be an index in a list
    #             key = int(key)
    #             if key not in current_level:
    #                 current_level[key] = {}
    #             current_level = current_level[key]
    #         else:  # Treat the key as a dictionary key
    #             if key not in current_level:
    #                 current_level[key] = {}
    #             current_level = current_level[key]
    #
    #     final_key = keys[-1]
    #     if final_key.isdigit():  # Check if the final key should be an index in a list
    #         final_key = int(final_key)
    #     current_level[final_key] = value
    nested_json = {}

    def set_nested_item(nested_dict, key_path, value):
        keys = key_path.split('.')
        for key in keys[:-1]:
            if key.isdigit():
                key = int(key)
                nested_dict = nested_dict.setdefault(key, {})
            else:
                nested_dict = nested_dict.setdefault(key, {})
        last_key = keys[-1]
        if last_key.isdigit():
            last_key = int(last_key)
            nested_dict[last_key] = value
        else:
            nested_dict[last_key] = value

    for key_path, value in flat_json.items():
        set_nested_item(nested_json, key_path, value)

    print(nested_json)

flatten_json(nested_json)