# matrix = input()
matrix = input() #'[[1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]]'
location = input() #'TB'
layer_no = int(input()) #1
filter_input = input()#'[[0, 0, 1], [0, 1, 0], [1, 0, 0]]'
stride = int(input())

filter = ''
for i in range(len(filter_input)):
    if filter_input[i] == '[' or filter_input[i] == ']' or filter_input[i]==',':
        continue
    else :
        ch = filter_input[i]
        filter += ch
filter = list(map(int, filter.split()))
filter2d = []
a = []
for i in range(1,1+len(filter)):
    if(i%3==0):
        a.append(filter[i-1])
        filter2d.append(a)
        a = []
    else:
        a.append(filter[i-1])
filter = filter2d
# print(filter)

matrix2 =''
for i in range(len(matrix)):
    if matrix[i] == '[' or matrix[i] == ']' or matrix [i]==',':
        continue
    else :
        ch = matrix[i]
        matrix2 += ch

matrix = list(map(int, matrix2.split()))

input_array = []

a = []
for i in range(1,1+len(matrix)):
    if(i%4==0):
        a.append(matrix[i-1])
        input_array.append(a)
        a = []
    else:
        a.append(matrix[i-1])

# print(input_array)
        
    

def add_padding_right(array):
    for i in range(len(array)):
        array[i].append(0)
    return array

def add_padding_left(array):
    for i in range(len(array)):
        temp = [0]
        temp = temp + array[i]
        array[i] = temp
    return array

def add_padding_top(array):
    size = len(array[0])
    temp = [0]*size
    temp = [temp]
    temp+=array
    array = temp
    return array

def add_padding_bottom(array):
    size = len(array[0])
    temp = [0]*size
    temp = [temp]
    array += temp
    return array


def add_padding(array, location, layer_no):
    if 'L' in location or 'A' in location:
        for i in range(layer_no):
            array = add_padding_left(array)

    if 'R' in location or 'A' in location:
        for i in range(layer_no):
            array = add_padding_right(array)

    if 'T' in location or 'A' in location:
        for i in range(layer_no):
            array = add_padding_top(array)

    if 'B' in location or 'A' in location:
        for i in range(layer_no):
            array = add_padding_bottom(array)

    return array


padded_array = add_padding(input_array, location= location, layer_no = layer_no)




output_array = []
# i = 0, j=0
# while((i <= len(padded_array)-3) and (j <= len(padded_array[0])-3)):
#     for a in range()

# print(i,len(padded_array[0])-2)
for i in range(0,len(padded_array)-2,stride):
    sum_array = []
    for j in range(0, len(padded_array[0])-2, stride):
        sum = 0
        # print(i,j)
        for a in range(3):
            for b in range(3):
                # print('a','b',a,b)
                sum += padded_array[i+a][j+b]*filter[a][b]
        # print(sum)
        sum_array.append(sum)

    output_array += [sum_array]

print(output_array)