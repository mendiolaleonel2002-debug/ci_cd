import sys
from generate.password_generator import generate_password

def main():

    if len(sys.argv) < 2:
        print("Uso: python main.py <longitud>")
        return
    
    try:
        length = int(sys.agrv[1])
    except ValueError:
        print("Error: la longitud deber ser un número")
        return

    
