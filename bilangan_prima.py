# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:15:35 2023

@author: Huawei
"""

def is_prima (x):
  if x <= 1:
        return False
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def main():
    prima = int(input("Masukkan bilangan prima : "))
    
    if is_prima(prima):
        print(prima,'adalah bilangan prima')
    else:
        print(prima,'bukan bilangan prima')
            
main()