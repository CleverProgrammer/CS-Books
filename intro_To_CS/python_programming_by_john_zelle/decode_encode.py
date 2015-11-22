# import message_encoder

def decode(encoded_message):
    decode = ''
    prev_i = 0
    for i, ordinal in enumerate(encoded_message):
        if ordinal == chr(32):
            decode += chr(int(encoded_message[prev_i:i]))
            prev_i = i+1
        elif i == len(encoded_message) - 1:
            decode += chr(int(encoded_message[prev_i:]))
            break
    return decode

if __name__ == "__main__":
    print(decode(input("Enter decoded messsage here:\n")))
