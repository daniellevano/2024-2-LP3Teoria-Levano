# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:23:07 2024

@author: Daniel Levano
"""

archivo = open("noticia.txt","at")

contenido = "\nFuente: RPP"
archivo.write(contenido)
archivo.close()