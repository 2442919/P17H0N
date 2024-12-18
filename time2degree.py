# Script care transforma timpul in grade de revolutie

def time_to_degrees(hour: int, minute: int) -> str:
    # Conversia orei si minutului in secunde totale
    total_seconds = hour * 3600 + minute * 60

    # Calcularea gradelor de rotatie
    degrees = total_seconds / 240

    return f"Revolution: {degrees:.2f} degrees"

# Citirea inputului de la utilizator
try:
    hour = int(input("Introduceți ora (0-23): "))
    minute = int(input("Introduceți minutul (0-59): "))

    if 0 <= hour <= 23 and 0 <= minute <= 59:
        result = time_to_degrees(hour, minute)
        print(result)
    else:
        print("Ora sau minutul sunt invalide. Introduceți valori între 0-23 pentru ore și 0-59 pentru minute.")
except ValueError:
    print("Input invalid. Asigurați-vă că introduceți numere întregi pentru ora și minut.")