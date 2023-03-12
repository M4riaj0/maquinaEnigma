# -*- coding: utf-8 -*-
import re
from keyboard import keyboard
from plugboard import plugboard
from rotors import rotor
from reflector import reflect
from enigma import Enigma

# historical enigma rotors and reflectors
I   = rotor("ÑEKMFLGDQVZNTOWYHXUSPAIBRCJekmflgdqvzntowyhxuspaibrcj" , "Q")
II  = rotor("ÑAJDKSIRUXBLHWTMCQGZNPYFVOEajdksiruxblhwtmcqgznpyfvoe", "E")
III = rotor("ÑBDFHJLCPRTXVZNYEIWGAKMUSQObdfhjlcprtxvznyeiwgakmusqo", "V")
IV  = rotor("ÑESOVPZJAYQUIRHXLNFTGKDCMWBesovpzjayquirhxlnftgkdcmwb", "J")
V   = rotor("ÑVZBRGITYUPSDNHLXAWMJQOFECKvzbrgityupsdnhlxawmjqofeck", "Z")
A   = reflect("ÑEJMZALYXVBWFCRQUONTSPIKHGDejmzalyxvbwfcrquontspikhgd")
B   = reflect("ÑYRUHQSLDPXNGOKMIEBFZCWVJATyruhqsldpxngokmiebfzcwvjat")
C   = reflect("ÑFVPJIAOYEDRZXWGCTKUQSBNMHLfvpjiaoyedrzxwgctkuqsbnmhl")

#keyboard and plugboard
KB = keyboard()
PB = plugboard([])
# PB = plugboard(["AB", "CD", "EF"])

#define enigma machine
ENIGMA = Enigma(A,IV,II,I,PB,KB)

# set the rings
ENIGMA.set_rings((1,1,1))

#set message key
ENIGMA.set_key("CAT")

#encipher message 
#message = "EFFIFNPRKZHAETUUEEYN"
#cipher_text = ""
#for letter in message:
#    cipher_text = cipher_text + ENIGMA.encipher(letter)
#print("Prueba 2")
#print(message)
#print(cipher_text)

with open('archivo_entrada.txt', 'r', encoding='utf-8') as archivo_entrada:
    with open('archivo_encriptado.txt', 'w', encoding='utf-8') as archivo_encriptado:
        letter = ''
        content = archivo_entrada.read()
        for letter in content:
            archivo_encriptado.write(ENIGMA.encipher(letter))

# ENIGMA = Enigma(A,IV,II,I,PB,KB)
# ENIGMA.set_rings((1,1,1))
# ENIGMA.set_key("CAT")

# with open('archivo_entrada.txt', 'r', encoding='utf-8') as archivo_entrada:
#     with open('archivo_desencriptado.txt', 'w', encoding='utf-8') as archivo_desencriptado:
#         letter2 = ''
#         content2 = archivo_entrada.read()
#         for letter2 in content2:
#             archivo_desencriptado.write(ENIGMA.encipher(letter2))
        