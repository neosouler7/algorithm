"""
1 2 3 4 5 6 7 8

ascending, descending, mixed

comment)
nothing
"""


array = list(map(int, input().split()))
array_asc = sorted(array, reverse=False)
array_dsc = sorted(array, reverse=True)
if array == array_asc:
    print("ascending")
elif array == array_dsc:
    print("descending")
else:
    print("mixed")
