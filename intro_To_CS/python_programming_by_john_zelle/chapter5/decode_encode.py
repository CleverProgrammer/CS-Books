__author__ = 'Rafeh Qazi'


def decode(encoded_message):
    decoded_message = ''
    prev_i = 0
    for i, ordinal in enumerate(encoded_message):
        if ordinal == chr(32):
            decoded_message += chr(int(encoded_message[prev_i:i]))
            prev_i = i + 1
        elif i == len(encoded_message) - 1:
            decoded_message += chr(int(encoded_message[prev_i:]))
            break
    return decoded_message


if __name__ == "__main__":
    print(decode(input("Enter decoded messsage here:\n")))
