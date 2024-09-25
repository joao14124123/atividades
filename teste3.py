import time

# Obter a hora atual em segundos desde a meia-noite de 1º de janeiro de 1970
tempo_em_segundos = time.time()

# Converter segundos para formato de hora legível
hora_estruturada = time(tempo_em_segundos)

# Extrair hora, minuto e segundo do tempo estruturado
hora = hora_estruturada[3]
minuto = hora_estruturada[4]
segundo = hora_estruturada[5]
# Formatar e exibir a hora atual
print(f"{hora}:{minuto}:{segundo}")

