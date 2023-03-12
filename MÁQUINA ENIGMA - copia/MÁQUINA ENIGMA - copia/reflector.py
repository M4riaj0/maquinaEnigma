# -*- coding: utf-8 -*-
class reflect:
    def __init__(self , wiring):
        self.left = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
