def reverse_words(sent):
    words = sent.split()
    words.reverse()
    rev_sent = ""

    for i in words:
        rev_sent += i + " "
    
    return rev_sent

sent = input()
print(reverse_words(sent))