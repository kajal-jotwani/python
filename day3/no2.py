COMMA = ","
PASS = 34

def parse_line(line: str) -> list:
    name, *marks = line.strip().split(COMMA)
    marks = [int(_) for _ in marks]
    return [name] + marks + [sum(marks)]

def load_data(mark_file: str) -> list:
    return [parse_line(line) for line in open(mark_file)]

def arrange(mark_list: list) -> list:
    def make_key(one: list) -> str:
        fails = sum(int (mark < PASS) for mark in one[1:-1])
        return f'{fails}{(10000 - one[-1]): 4}{one[0]}'
    return sorted(mark_list, key = make_key)

def assign_rank(score_wise: list) -> list:
    score = -1
    rank = 0
    assigned = []
    for position, one_score in enumerate(score_wise, start=1):
        if one_score[-1] != score:
            rank = position
            score = one_score[-1]
        assigned.append(f'{rank:4}{one_score[0]:40}{one_score[-1]:5}')
    return assigned

print(load_data("marks.txt")[:10])
print(arrange(load_data))



        

    

    