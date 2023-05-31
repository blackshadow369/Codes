import binascii
import time
import data
#from functools import wraps
import functools as ft


# conversion of plain to binary
def plain_to_binary(plain_str):
    #print("plain text :"+plain_str)
    #binary_str = ''.join(format(ord(i), '08b') for i in plain_str)
    #print("plain to binary result : "+binary_str)
    #binary_str = ' '.join(format(ord(i), 'b') for i in plain_str)
    #print(binary_str)
    return str(''.join(format(ord(i), '08b') for i in plain_str))


DNA_encoding = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
}
#conversion of binary to DNA sequence
@ft.lru_cache(maxsize=None)
def b_t_n(v):
    for key in list(DNA_encoding.keys()):
        if v == key:
            return DNA_encoding.get(key)



def binary_to_DNA(binary_str):
    #print("binary text : "+binary_str)
    binary_list = [binary_str[i: i + 2] for i in range(0, len(binary_str), 2)]
    DNA_list = []
    for num in binary_list:
        DNA_list.append(b_t_n(num))

    DNA_str = "".join(DNA_list)
    #print("binary to dna result : "+DNA_str)
    #print(DNA_str)
    return DNA_str


# conversion of DNA to morse code

MORSE_CODE_DICT = { 'A': '.-', 'C': '-.-.','G': '--.', 'T': '-'}
# dna to morse
@ft.lru_cache(maxsize= None)
def d_t_n(v):
    return MORSE_CODE_DICT[v]

def dna_to_morse(dna_str):
    #print("dna text : ",dna_str)
    morse_str = ""
    for letter in dna_str:
        if letter != ' ':
            morse_str += d_t_n(letter) + ' '
        else:
            morse_str += ' '
    #print("morse text : ",morse_str)
    return morse_str

#value = 'Geeks'
def Encryption(value):
    binary_str = plain_to_binary(value)
    dna_str = binary_to_DNA(binary_str)
    morse_str = dna_to_morse(dna_str)
    return morse_str


# Decryption
@ft.lru_cache(maxsize= None )
def m_t_d(citext):
    return list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]


def morse_to_dna(morese_str):
    morese_str += ' '
    decipher = ''
    citext = ''

    for letter in morese_str:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += m_t_d(citext)
                citext = ''
    return decipher

# dna to binary
@ft.lru_cache(maxsize= None)
def d_t_b(i):
    for key, value in DNA_encoding.items():
        if i == value:
            return key
    return ""


def dna_to_binary(dna_str):
    binary = ""
    for i in dna_str:
        binary += d_t_b(i);
    return binary

@ft.lru_cache(maxsize = None)
def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)
@ft.lru_cache(maxsize= None)
def binary_to_plain(binary_str):
    plain_str = ""
    for i in range(0, len(binary_str), 8):
        temp_data = int(binary_str[i:i + 8])

        decimal_data = BinaryToDecimal(temp_data)
        plain_str = plain_str+ chr(decimal_data)
    #print(plain_str)

#entering data
with open('1_mb_file.txt', 'r') as f:
    # Read the contents of the file into a variable
    file_contents = f.read()
#one = input("Here is the input : ")
#Encrpytion time
pst = time.process_time()
st = time.time()
value = Encryption(file_contents)
et = time.time()
pet = time.process_time()
tt = et-st
ptt = pet - pst
mili_ptt = ptt*1000
mili_tt = tt*1000
print("BDM ENCRYPTION TIMING DETAILS :")
print("Wall time of encryption in seconds  : ",tt," seconds")
print("Wall time of encryption in milliseconds :",mili_tt," miliseconds ")
print("Cpu time of encryption in seconds : ",ptt," seconds")
print("Cpu time of encryption in milliseconds :",mili_ptt," miliseconds ")
print("\n")

def Decrption(value):
    dna_str1 = morse_to_dna(value)
    binary = dna_to_binary(dna_str1)
    binary_to_plain(binary)

#Decryption time
pst = time.process_time()
st = time.time()
Decrption(value)
et = time.time()
pet = time.process_time()
tt = et-st
ptt = pet - pst
mili_ptt = ptt*1000
mili_tt = tt*1000
print("BDM DECRYPTION TIMING DETAILS :")
print("Wall time of encryption in seconds  : ",tt," seconds")
print("Wall time of encryption in milliseconds :",mili_tt," miliseconds ")
print("Cpu time of encryption in seconds : ",ptt," seconds")
print("Cpu time of encryption in milliseconds :",mili_ptt," miliseconds ")



