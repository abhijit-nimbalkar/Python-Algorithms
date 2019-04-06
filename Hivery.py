def first_occurrence(string):
    #getting the start_index, end_index of the string
    #settting next_index to zero which will store the index of next occurance of charachter in the string
    #setting the accessed_char_count to 0 to measure number of character accessed from the string to get the first occurrence 
    start_index,next_index,end_index,accessed_char_count=1,0,len(string),0

    first_char=string[next_index]           #Getting first character of string 
    first_occurrence=None                   #getting first occurrence of character in the string

    while start_index<end_index:            #running the while loop until start index(init 0) becomes greater or equal to end index(init length of string)
        accessed_char_count+=1
        if first_char in string[start_index:end_index]:         #If occurance of first_char is found
            next_index=string.index(first_char,start_index,end_index)   #getting the index of that occurrence
            first_occurrence=string[next_index]                     
            end_index=next_index-1                      #making end index euqal to the index of first character on the left side of the occurrence char
            first_char=string[end_index]                #setting the first character to new end index of the substring
        else:
            first_char=string[start_index]              #if character not found in the substring then travesring to the right with increase in start index
            start_index+=1

    if(first_occurrence):   #if first repeated occurrence found
        print(f"Total number of character accessed {accessed_char_count} out of {len(string)} to get the first repeated occurance of the character.")
        return first_occurrence
    else:
        return "I am sorry but there is not a single repeated occurrence of character in the string!"

def main():
    print(f"First occurrence of character : {first_occurrence('abcdefgsdrft')}\n")
    print(f"First occurrence of character : {first_occurrence('abcdefcgah')}\n")
    print(f"First occurrence of character : {first_occurrence('abcdefefec')}\n")
    print(f"First occurrence of character : {first_occurrence('abcdefghjiad')}\n")

if __name__=='__main__':
    main()
