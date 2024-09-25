notas = {}


for i in range(1, 5):
    nota = float(input(f"Insira a nota {i}: "))
    notas[f'Nota {i}'] = nota


media = sum(notas.values()) / len(notas)


print("\nNotas inseridas:")
for chave, valor in notas.items():
    print(f"{chave}: {valor}")

print(f"\nMédia das notas: {media:.2f}")