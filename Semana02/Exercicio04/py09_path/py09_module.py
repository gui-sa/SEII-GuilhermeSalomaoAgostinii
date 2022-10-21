from unicodedata import numeric


print("Imported my module!")

teste = 'Test_string'


def find_index(to_search:list,target:any)->any:
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

    