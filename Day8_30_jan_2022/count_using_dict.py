"""
@author : Nishant Sanjay kumbhar
@goal : get the count of each of letter in string
"""
def get_string(sample_string : str) -> dict:
    sample_dict = {}
    for i in sample_string:
        if i not in sample_dict:
            sample_dict[i] = 0
        sample_dict[i] += 1
    return sample_dict


f_dict = get_string("hi this is Nishant")
print(f_dict)