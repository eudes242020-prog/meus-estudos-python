import time
import os

def pausa_e_limpar():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')