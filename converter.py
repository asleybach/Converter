#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converter.py
#  
#  Copyright 2016 roxy <asley@UnKnown>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import Tkinter
from Tkinter import *
import tkMessageBox
from tkMessageBox import *
def salir():
	resp = tkMessageBox.askquestion("Salir del Sistema","¿Seguro quiere Salir?", icon="warning")
	if resp=='no':
		print('XD')
		main					
	else:
		print ("close converter")
		sys.exit()
def pon_a_kilopon():
	salida=(entrada.get()) * 1000
def kilopon_a_pon():
	salida=(entrada.get()) / 1000
def kp_a_n():
	salida=(entrada.get()) * 9.8
def n_a_kp():
	salida=(entrada.get()) / 9.8
def n_a_dynas():
	salida=(entrada.get()) * 100000
def p_a_dynas():
	salida=(entrada.get()) * 980
def dynas_a_pon():
	salida=(entrada.get()) / 980
def kpadyn():
	dato=entrada.get()
	newton=kp_a_n(dato)
	kp=n_a_dynas(newton)
def Kilopondios():
	separador=Tk()
	
	separador.geometry("240x240")
	separador.grid()
	v = IntVar()
	Radiobutton(separador, bg="white",text="One", variable=v, value=1).grid(row=3,padx=50)
	Radiobutton(separador, bg="white",text="Two", variable=v, value=2).grid()
	Radiobutton(separador, bg="white",text="One", variable=v, value=3).grid()
	separador.config(bg="white")
	
class converter:
	def __init__(self):
		formulario=Tk()
		formulario.title("Converter")
		formulario.geometry("480x240")
		formulario.resizable(width=False,height=False)
		titu1o=Label(formulario,bg="white",text="Convertidor de Unidades Físicas",font=('Helvetica', 16))
		titu1o.grid(padx=50, pady=5)
		titulo2=Label(formulario,bg="white",text="Ingrese valor numérico",font=('Helvetica', 12))
		titulo2.grid(padx=50, pady=5)
		entrada=Entry(formulario).grid(padx=5,pady=5)
		v = IntVar()
		
		separador2=Frame (formulario,bg="white")
		separador2.grid()
		Radiobutton(separador2, bg="white",text="Two", variable=v, value=4).grid(row=3,padx=80)
		Radiobutton(separador2, bg="white",text="One", variable=v, value=5).grid()
		Radiobutton(separador2, bg="white",text="Two", variable=v, value=6).grid()
		menu_bar= Menu(formulario)
		
		unidad=Menu(menu_bar)
		ayuda=Menu(menu_bar)
		menu_bar.add_cascade(label="Unidades",menu=unidad, underline=0)
		menu_bar.add_cascade(label="Ayuda",menu=ayuda, underline=0)
		unidad.add_command(label="kilopondios",underline=0,command=Kilopondios)
		unidad.add_command(label="Dynas",underline=0,)
		unidad.add_command(label="Newton",underline=0,)
		unidad.add_command(label="Salir",underline=0,command=salir)
		ayuda.add_command(label="Acerca de Converter",underline=0,)
		ayuda.add_command(label="Créditos",underline=0)
		formulario.protocol("WM_DELETE_WINDOW",salir)
		formulario.config(bg="white",menu=menu_bar)
		formulario.mainloop()

def main():
    Conventer=converter()
    return 0

if __name__ == '__main__':
    main()
