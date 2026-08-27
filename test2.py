"""Conan"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
word = str(input())
step = int(input())
new = alphabet.index(word) + step
new = alphabet[new]
print(new)