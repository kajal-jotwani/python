# # def encryption(char1: str, num: int) -> int:
# #     return ord(char1) ^ num
# # def decryption(value: int, num:int) -> str:
# #     return chr(value !^ num) 
# # def string_to_encryption(string: str) -> 
# # print(2**16)
# # print(263*257)
LN = '\n'
def reciprocal_mod_arithmatic(num: int, mod: int) -> str:
    table = []
    table.append(("    q", "    r", "    y"))
    table.append((0, mod, 0))
    table.append((mod//num, num, 1))
    while table[-1][1] != 1:
        prev_q = table[-1][0]
        prev_r = table[-1][1]
        prev_y = table[-1][2]
        prev_prev_q = table[-2][1]
        prev_prev_y = table[-2][2]
        present_r = prev_prev_q - prev_q * prev_r
        present_q = prev_r // present_r
        present_y = (prev_prev_y - prev_q * prev_y)
        table.append((present_q % mod, present_r % mod, present_y))
        table_for_reciprocal = ""
        for value in table:
            table_for_reciprocal += f'{value[0]:5}{value[1]:5}{value[2]:5}{LN}'
    return table_for_reciprocal
# print(reciprocal_mod_arithmatic(23, 100))
e = 7
p = 263
q = 257
n = p * q
print(n)
def char_2_num(character: str) -> int:
    return (ord(character) ** e) % n
# print(char_2_num("A"))
def encryption_string(string: str) -> int:
    encrypted = []
    for char in string:
        encrypted.append(char_2_num(char))
    return encrypted
print(e, n, encryption_string("kajal"), sep = '\n')
def decryption(encrypted: list[int]) -> str:
    d = reciprocal_mod_arithmatic(e, (p - 1) * (q - 1))
    print(d[-1])
    return ""

def decrypt(encrypt_list: list[int]) -> str:
    for y in encrypt_list:
        dy = y(y ** 5033) %n
        y1, y2 = divmod(dy, 256)
        print ((chr(y1) + chr(y2)) ,end = '')

decrypt([6372, 36518, 39155, 36518, 30354])