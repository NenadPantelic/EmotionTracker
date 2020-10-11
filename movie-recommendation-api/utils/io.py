from json import load


def load_json(json_file_path):
    """
    Loads json file.
    :param str json_file_path: path of json file that will be loaded
    :rtype: list
    :return: list of json (dictionary) objects
    """
    assert (isinstance(json_file_path, str))
    with open(json_file_path) as f:
        data = load(f)
    return data
