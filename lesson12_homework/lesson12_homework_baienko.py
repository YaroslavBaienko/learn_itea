def split_message_by_key_len(message, key_length):
    return [message[i:i + key_length] for i in range(0, len(message), key_length)]



len1 = split_message_by_key_len('Hello world by the world of length be', 4)
print(len1)


def encrypt(prepared_message, subsequence: str):
    encrypted = []
    for object in prepared_message:
        if len(object) == len(subsequence):
            for index in subsequence:
                encrypted.append(object[int(index)])
        else:
            pass
    return encrypted, len(encrypted)




