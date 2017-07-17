
def  missingWords(s, t):
    s_list = s.split(" ")
    t_list = t.split(" ")
    sub_seq_list = []
    for s in s_list:
        sub_seq_list = sub_seq_list + find_sequence(s)
    for x in t_list:
        if x in sub_seq_list:
            s_list.remove(x)

    return s_list

def find_sequence(s):
    length = len(s)+1
    x = [s[x:y] for x in range(length) for y in range(length) if s[x:y]]
    return x

print(missingWords("I am using HackerRank to improve programing.", "am HackerRank to improve"))
