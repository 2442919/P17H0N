# Script simplificat pentru transformarea timpului in grade de revolutie

def time_to_degrees(hour: int, minute: int) -> str:
    # Calculam totalul de secunde din ora si minut
    total_seconds = hour * 3600 + minute * 60  # 1 ora are 3600 secunde, 1 minut are 60 secunde

    # Determinam gradele de rotatie, stiind ca 1 grad corespunde la 240 de secunde
    degrees = total_seconds / 240

    # Returnam rezultatul formatat cu doua zecimale
    return f"Revolution: {degrees:.2f} degrees"

# Solicitam utilizatorului sa introduca ora si minutul
hour = int(input("Introduceți ora (0-23): "))  # Citim ora (intre 0 si 23)
minute = int(input("Introduceți minutul (0-59): "))  # Citim minutul (intre 0 si 59)

# Calculam si afisam rezultatul
print(time_to_degrees(hour, minute))
