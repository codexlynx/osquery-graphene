import string

def sanitize(input):
    output = ''
    whilelist = string.ascii_letters + string.digits + '/\\/.'
    for char in input:
        if char in list(whilelist):
            output = output + char
    return output
