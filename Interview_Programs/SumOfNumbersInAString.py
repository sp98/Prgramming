import re
def num_sum(my_str):
    return sum(int(x) for x in my_str if '0'<= x <= '9')

def num_sum2(data):
    num = ''
    total_sum = 0
    curr_num_index = 0
    for x in range(0, len(my_str)):
        #print(x)
        if '0'<= data[x] <= '9':
            num = data[x]
            print('x : ' + str(x))
            print('curr_num_index : ' + str(curr_num_index))
            if x == curr_num_index + 1:
                num = num + data[x]
                print('num : ' + str(num) )
            elif len(num) > 0:
                total_sum = total_sum + int(num)
                num = ''
                print('total_sum : ' + str(total_sum))
            curr_num_index = x
    return total_sum


if __name__ == '__main__':
    my_str = 'a45b1'
    # print(num_sum(my_str)) # Python Way, prints individual.
    # print(sum(int(x) for x in re.findall(r'[0-9]', my_str)))
    print(num_sum2(my_str)) # Python Way, prints individual.
