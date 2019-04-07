
from math import sqrt

#getting sum of digits of numbers
def digit_sum(n):
    return sum(map(int,list(str(n))))

#finding out whether number is eular or not
def eular_count(range_value):
    count=0
    for num in range(range_value):
        base_list=[x for x in range(num) if sqrt(x)-round(sqrt(x))==0]
        condition_one=[(sqrt(x),sqrt(y)) for x in base_list for y in base_list if x+y==num]
        if(condition_one):
            condition_two=[(sqrt(x),sqrt(y)) for x in base_list for y in base_list if x+2*y==num]
            if(condition_two):
                condition_three=[(sqrt(x),sqrt(y)) for x in base_list for y in base_list if x+3*y==num]
                if(condition_three):
                    condition_four=[(sqrt(x),sqrt(y)) for x in base_list for y in base_list if x+7*y==num]
                    if(condition_four):
                        count+=1
    return count


def main():    
    input_num=int(input("Enter Number till you want to find out number of eular numbers:"))
    count1=eular_count(input_num)
    print(f"There are total {count1} eular numbers")

            
if __name__=='__main__':
    main()               
            
