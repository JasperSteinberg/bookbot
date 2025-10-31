def word_count(text: str) -> int:
    return len(text.split())

def char_count(text: str) -> dict:
    text = text.lower()

    dict = {}

    for char in text:
        if char not in dict.keys():
            dict[char] = 1
        else:
            dict[char] += 1

    return dict

def sorted_dict(dict: dict) -> dict:
    dict_list = []
    for key, val in dict.items():
        dict_list.append(
            {
                "char": key,
                "num": val
            }
        )
    def sort_on(items):
        return items["num"]
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list