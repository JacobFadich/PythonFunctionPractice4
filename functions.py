#max_num function

def max_num(x,y,z):
    return max([x,y,z])

print(max_num(1,2,3))
print(max_num(10,73,3))

#mult_list function

def mult_list(list):
    if len(list) == 0:
        return 0
    product = list[0]
    if len(list) > 1:
        for i in list[1:]:
            product = product * i
    return product

print(mult_list([1,2,3]))
print(mult_list([6]))

#rev_string function

def rev_string(my_str):
    return my_str[::-1]

print(rev_string('apple'))
print(rev_string('Hello World'))

#num_within function

def num_within(x,y,z):
    return x in range(y,z+1)

print(num_within(1,2,3))
print(num_within(2,1,3))

#pascal function

triangle = [[1],[1,1]]

def pascal(x):
    if x <1:
        print("invalid input")
    elif x == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < x:
            row = []
            row_prev = triangle[row_number - 1]
            lenght = len(row_prev)+1
            for i in range(lenght):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < lenght-1:
                    row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

pascal(3)
pascal(5)
pascal(0)    



