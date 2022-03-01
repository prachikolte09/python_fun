#given an array write a function to put all the even number in the begining
#num=[2,3,8,4,9,5,7,6]
#ans=[2,4,6,8,3,9,5,7]
#questions to ask will the array will be sorted?
#or do we wanted sorted in the answer?
# can we allocate separate space?
#hint you can use two pointers when it's reordering you can use two pointers

def even_odd(num):
    even_num,odd_num= 0, len(num)-1
    while even_num<odd_num:
        #check if its number even yes then just increment and go ahead
        if num[even_num] % 2==0:
            even_num +=1
        else:
            # just swap the number for two pointers
            num[even_num],num[odd_num]=num[odd_num],num[even_num]
            odd_num-=1

num=[2,3,8,4,9,5,7,6]
even_odd(num)
print(num)
