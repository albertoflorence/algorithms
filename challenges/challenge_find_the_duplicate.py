def find_duplicate(nums):
    table = set()
    for n in nums:
        if not isinstance(n, int) or n < 0:
            return False
        if n in table:
            return n
        else:
            table.add(n)

    return False
