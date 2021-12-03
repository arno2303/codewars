"""
Instructions:

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the
same nesting structures and same corresponding length of nested arrays as the first array.

Example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

"""


def same_structure_as(original: list, other: list) -> bool:
    if type(original) != type(other) and len(original) != len(other):
        return False
    for i in range(len(original)):
        if isinstance(original[i], list):
            if isinstance(other[i], list):
                return same_structure_as(original[i], other[i])
            return False
        if isinstance(other[i], list):
            return False
    return True

