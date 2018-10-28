#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Caesar Cipher encoder/decoder"""

import enchant
D = enchant.Dict("en_US")

def encode(msg, shift):
    cipher = ''
    msg = msg.upper()
    for c in msg:
        cipher += rot(c, shift) if c.isalpha() else c
    return cipher

def decode(msg, encode_shift):
    cipher = ''
    msg = msg.upper()
    shift = 26 - encode_shift
    for c in msg:
        cipher += rot(c, shift) if c.isalpha() else c
    return cipher

def rot13(msg):
    return encode(msg, 13)

def brute_force(cipher, show_all=False):
    cipher = cipher.upper()
    lines = {}
    for i in range(26):
        likely = 0
        line = 'ROT{:02} - '.format(i)
        for c in cipher:
            likely += count_likely(line)
            line += rot(c, i) if c.isalpha() else c
        lines[line] = likely

    lines = sorted(lines.items(), key=lambda kv: kv[1], reverse=True)
    if show_all:
        for line in lines:
            print(line[0])
    return lines[0][0][8:]

def rot(char, shift):
    return chr((ord(char) - ord('A')+shift)%26 + ord('A'))

def count_likely(text):
    likely = 0
    for i in range(len(text)):
        if D.check(text[i:]):
            likely += 1
    return likely

if __name__ == '__main__':
    print(decode(encode('abcdefghijklmnopqrstuvwxyz', 10), 10))
    ciphertext = 'kdfn wkh sodqhw'
    print(brute_force(ciphertext))
