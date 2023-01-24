#ADN homework
num = 1
print("Ingrese cuantas moleculas de ADN convertira en Alternancias de ARN")
tope = int(input(""))

while num <= tope:
    print("Ingrese el valor de la molecula de ADN")
    print("A = Adenina, C = Citosina, G = Guanina o T = Timina")
    mol = str(input(""))
    if mol == str("A"):
            mol = str("U")
    elif mol == str("C"):
            mol = str("G")
    elif mol == str("G"):
        mol = str("C")
    elif mol == str("T"):
        mol = str("A")
    num += 1
else:
    print(mol)
    print("Finalizó")
