maior_at =0
cd_at =0
mp = 0
cod_at = 0

while True:
    codigo = int(input("digite o codigo, ou se quiser sair digite 0"))
    
    altura = float(input("digite a altura"))
    peso = float(input("digite o peso"))
    if codigo == 0:
        break
    
    else:
        if altura > maior_at:
            maior_at = altura
            cd_at = codigo
        print(maior_at , cd_at)
        if peso > mp:
            mp = peso
            cod_at = codigo
        print(mp , cod_at)