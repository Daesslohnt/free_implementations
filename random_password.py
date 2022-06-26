import random
import string

def define_random_password(passwd_length=8):
    rand_passwd = "".join(random.choices(string.ascii_letters + string.digits, k=passwd_length))
    return rand_passwd

for _ in range(10):
    print(define_random_password(30))