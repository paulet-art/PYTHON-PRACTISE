#Outputs the integer number indicating the total number of occurrences of the substring in the original string.

def count_substring(string, sub_string):
    count = 0
    sub_string_length = len(sub_string)
    
    for i in range(len(string) - sub_string_length+1): # range to check entire string
        if string[i:i+sub_string_length] == sub_string: # range equal to the sublength chunck size
            count +=1
    
    return count
   
