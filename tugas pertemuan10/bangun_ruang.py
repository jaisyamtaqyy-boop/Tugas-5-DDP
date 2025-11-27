import math

def luas_kubus(sisi):
    return 6 * sisi * sisi

def luas_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_bola(jari_jari):
    return 4 * math.pi * jari_jari * (jari_jari)

def luas_tabung(jari_jari, tinggi):
    return math.pi * jari_jari * (jari_jari + tinggi)

def luas_kerucut(jari_jari, selimut):
    return math.pi * jari_jari * (jari_jari + selimut)