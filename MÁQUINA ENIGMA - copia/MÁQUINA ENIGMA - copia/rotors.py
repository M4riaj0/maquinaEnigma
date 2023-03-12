# -*- coding: utf-8 -*-
class rotor:
    def __init__(self , wiring, notch):
        self.left = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal): 
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

# I = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ" , "Q")
# II = rotor("AJDKSIRUXBLHWTÑMCQGZNPYFVOE", "E")
# III = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
# IV = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
# V = rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

# print(I.forward(0))

    def show(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[52] + self.left[:52]
                self.right = self.right[52] + self.right[:52]

    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".find(letter)
        self.rotate(n)

    def set_ring(self, n):

        #rotate the rotor backwards
        self.rotate(n-1, forward=False)


        #adjust the turnover notch in relationship to the writing
        n_notch = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[(n_notch - n) % 53]
