# AlphaEncrypter 1.0.0 by Olivier van Asperen & Willem van Asperen

import random


def encrypt():

    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cypher = ""

    new_alpha = alpha
    for char in alpha:
        encrypt_val = random.randint(5, 100000)

        new_pos = (alpha.find(char) + encrypt_val) % (len(new_alpha)) if len(new_alpha) > 1 else 0
        cypher += new_alpha[new_pos]
        new_alpha = new_alpha[0:new_pos] + new_alpha[new_pos+1:]

    return alpha, cypher
