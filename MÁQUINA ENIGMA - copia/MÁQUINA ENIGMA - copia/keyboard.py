# -*- coding: utf-8 -*-
class keyboard:
    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".find(letter)
        return signal
    
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[signal]
        return letter