# --------------
##File path for the file 
file_path 

# define function
def read_file(path):
    file_read = open(path,'r')
    sentence = file_read.readline()
    file_read.close()
    return sentence

# call the defined function
sample_message = read_file(file_path)  
print(sample_message)

#Code starts here


# --------------
#Code starts here
file_path_1
file_path_2

# read first line from file 1
message_1 = read_file(file_path_1)  
print(message_1)

# read first line from file 2
message_2 = read_file(file_path_2)  
print(message_2)

# define a function
def fuse_msg(message_a , message_b) : 
    int_message_a = int(message_a)
    int_message_b = int(message_b)
    quotient = int(int_message_b / int_message_a)
    return str(quotient)

# call the function to perform division of 2 strings
secret_msg_1 = fuse_msg(message_1 , message_2)
print(secret_msg_1)


# --------------
#Code starts here
file_path_3

message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

message_4 = read_file(file_path_4)
print("first message = ", message_4)

message_5 = read_file(file_path_5)
print("second message = ", message_5)

def compare_msg(message_d , message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [x for x in a_list if x not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4 , message_5)  
print("Sentence =", secret_msg_3)


# --------------
#Code starts here
file_path_6

message_6 = read_file(file_path_6)
print("Message = ", message_6)

even_word = lambda x : len(x) % 2 == 0

def extract_msg(message_f) : 
    a_list = message_f.split()
    b_list = list(filter(even_word, a_list))
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)
print("Extracted Message = ", secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

#Code starts here

secret_msg = str(" ".join(message_parts))

def write_file(secret_msg , path): 
    file_write = open(path , 'a+')
    file_write.write(secret_msg)
    file_write.close()

write_file(secret_msg , final_path)
print("Secret message =" , secret_msg)



