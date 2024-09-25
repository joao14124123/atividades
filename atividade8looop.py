sin = 1000

st = sin + (sin * 0.015)

ano = 1997
p_a = 0.015*2

while ano <= 2024:
    st = st + (st * p_a)
    p_a = p_a * 2
    ano = ano + 1
    
print(f"o salario atual do funcionario em 2024 é R${st:.2f}")