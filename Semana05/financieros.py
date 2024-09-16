# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:17:55 2024

@author: Daniel Levano
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)


############################################
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {obtenerIGVconSubtotal(subtotal):.2f}" )
print(f"Total: {obtenerTotalconSubtotal(subtotal):.2f}" )

total = 1000.49
print(f"\nSubtotal: {obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")
