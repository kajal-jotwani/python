def compress_ranges(list):
    if not list:
        return ""
    
    list = sorted(list)
    ranges = []
    
    start, end = list[0], list[0]

    for num in list[1:]:
        if is_consecutive(end, num):
            end = num
        else:
            ranges.append(format_range(start, end))
            start, end = num, num

    ranges.append(format_range(start, end))
    return ", ".join(ranges)

def is_consecutive(a, b):
    return b == a + 1

def format_range(start, end):
    if start == end:
        return f"{start}"
    else:
        return f"{start}-{end}"

# Example 
input_list = [7, 8, 9, 10, 14, 17, 18, 19, 25, 26, 27, 28, 29, 31]
print(compress_ranges(input_list))
