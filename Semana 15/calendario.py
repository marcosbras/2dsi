profissionais = ["Ana", "Bruno", "Carla"]
dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]

# Cada linha da agenda é um profissional; cada coluna é um dia.
agenda = [
    [4, 3, 5, 2, 6],  # Ana
    [3, 4, 2, 5, 4],  # Bruno
    [5, 5, 4, 3, 7],  # Carla
]

print("=== AGENDA DE ATENDIMENTOS ===")
print("Prof\t" + "\t".join(dias))

for i in range(len(profissionais)):
    profissional = profissionais[i]
    atendimentos = agenda[i]
    linha = "\t".join(str(atendimentos[j]) for j in range(len(dias)))
    print(f"{profissional}\t{linha}")

print()
# Acesso pontual usando nomes em vez de números fixos sempre que possível.
dia_quarta = dias.index("Qua")
carla = profissionais.index("Carla")
print("Carla na Qua:", agenda[carla][dia_quarta])
