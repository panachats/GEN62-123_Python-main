def get_email ():
    email = input("Enter your email : ")
    at = 0
    dot = False
    if email[0] == "@":
        return get_email()
    for x in email:
        if x == '@':
            at += 1
        if at > 1 :
            return get_email()
        if at == 1 and x == '.':
            dot = True
    if dot:
        return email
    return get_email()
get_email()