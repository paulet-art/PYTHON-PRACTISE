# this line of code Splits the string on a " " (space) delimiter and join using a - hyphen. 

def split_and_join(line):
    split_line = line.split(" ")
    join_line = "-".join(split_line)
    return join_line
