import time

# Obținem componentele curente ale orei
hrs = int(time.strftime("%H"))  # Ore (format de 24 de ore)
# Folosim funcția strftime pentru a obține ora curentă în format de 24 de ore. O conversie la întreg (int) este necesară pentru a putea face operații matematice.

hrs_cd = 24 - hrs  # Numărătoarea inversă a orelor
# Calculăm câte ore mai sunt până la sfârșitul zilei. Dacă ora este 8, hrs_cd va fi 16, adică mai sunt 16 ore până la miezul nopții.

min = int(time.strftime("%M"))  # Minute
# Obținem minutul curent, care este un număr între 0 și 59.

min_cd = 60 - min  # Numărătoarea inversă a minutelor
# Calculăm câte minute mai sunt până la sfârșitul orei curente. Dacă sunt 15 minute, min_cd va fi 45, adică mai sunt 45 de minute până la următoarea oră.

sec = int(time.strftime("%S"))  # Secunde
# Obținem secunda curentă, un număr între 0 și 59.

sec_cd = 60 - sec  # Numărătoarea inversă a secundelor
# Calculăm câte secunde mai sunt până la minutul următor. Dacă sunt 30 de secunde, sec_cd va fi 30, adică mai sunt 30 de secunde până la minutul următor.

dom = int(time.strftime("%d"))  # Ziua lunii
# Obținem ziua curentă a lunii, un număr între 1 și 31.

dow = int(time.strftime("%w"))  # Ziua săptămânii (0=duminică, 6=sâmbătă)
# Obținem ziua curentă a săptămânii (de la 0 la 6, unde 0 este duminică și 6 este sâmbătă).

dow_cd = 7 - dow  # Numărătoarea inversă a zilelor din săptămână
# Calculăm câte zile mai sunt până la sfârșitul săptămânii. Dacă astăzi este miercuri (dow=3), dow_cd va fi 4, adică mai sunt 4 zile până la duminică.

now = int(time.strftime("%U"))  # Numărul săptămânii din an
# Obținem săptămâna curentă a anului, un număr între 0 și 52.

now_cd = 52 - now  # Numărătoarea inversă a săptămânilor din an
# Calculăm câte săptămâni mai sunt până la sfârșitul anului. Dacă suntem în săptămâna 50, now_cd va fi 2, adică mai sunt 2 săptămâni până la sfârșitul anului.

mon = int(time.strftime("%m"))  # Numărul lunii (1-12)
# Obținem luna curentă a anului (de la 1 la 12).

mon_cd = 12 - mon  # Numărătoarea inversă a lunilor din an
# Calculăm câte luni mai sunt până la sfârșitul anului. Dacă suntem în decembrie (mon=12), mon_cd va fi 0, adică mai este 1 lună.

doy = int(time.strftime("%j"))  # Ziua anului
# Obținem ziua curentă a anului (de la 1 la 365 pentru anii normali sau 366 pentru anii bisecți).

doy_cd = 365 - doy  # Numărătoarea inversă a zilelor din an
# Calculăm câte zile mai sunt până la sfârșitul anului. Dacă suntem în ziua 353, doy_cd va fi 12, adică mai sunt 12 zile până la sfârșitul anului.

noy = int(time.strftime("%Y"))  # Anul curent
# Obținem anul curent.

# Calculăm diverse valori legate de timpul din zi
dim = hrs * 60 + min  # Ziua în minute
# Calculăm câte minute au trecut din zi de la 00:00. Dacă este ora 08:15, dim va fi 8*60 + 15 = 495 minute.

dim_cd = 1440 - dim  # Numărătoarea inversă a minutelor din zi
# Calculăm câte minute mai sunt până la sfârșitul zilei. O zi are 1440 de minute (24 ore * 60 minute), astfel dim_cd va fi 1440 - dim.

dis = dim * 60 + sec  # Ziua în secunde
# Calculăm câte secunde au trecut din zi de la 00:00. Dacă este 08:15:30, dis va fi 495 minute * 60 + 30 secunde = 29730 secunde.

dis_cd = 86400 - dis  # Numărătoarea inversă a secundelor din zi
# Calculăm câte secunde mai sunt până la sfârșitul zilei. O zi are 86400 de secunde (24 ore * 60 minute * 60 secunde), astfel dis_cd va fi 86400 - dis.

yih = doy * 24 + hrs  # Anul în ore
# Calculăm câte ore au trecut din anul curent. Dacă este ziua 353 și ora 8, yih va fi 353 * 24 + 8 = 8480 ore.

yih_cd = 8766 - yih  # Numărătoarea inversă a orelor din an
# Calculăm câte ore mai sunt până la sfârșitul anului. Un an are 8766 de ore (365 zile * 24 ore), astfel yih_cd va fi 8766 - yih.

yim = doy * 1440 + dim  # Anul în minute
# Calculăm câte minute au trecut din anul curent. Dacă este ziua 353 și 08:15, yim va fi 353 * 1440 + 495 = 508065 minute.

yim_cd = 525960 - yim  # Numărătoarea inversă a minutelor din an
# Calculăm câte minute mai sunt până la sfârșitul anului. Un an are 525960 de minute (365 zile * 1440 minute), astfel yim_cd va fi 525960 - yim.

yis = doy * 86400 + dis  # Anul în secunde
# Calculăm câte secunde au trecut din anul curent. Dacă este ziua 353 și 08:15:30, yis va fi 353 * 86400 + 29730 = 30495780 secunde.

yis_cd = 31557600 - yis  # Numărătoarea inversă a secundelor din an
# Calculăm câte secunde mai sunt până la sfârșitul anului. Un an are 31557600 de secunde (365 zile * 86400 secunde), astfel yis_cd va fi 31557600 - yis.

# Stage II - TIME IN DEGREE
did = dis // 240  # Ziua în grade
# Calculăm câte grade au trecut din zi, considerând că 1 grad este egal cu 240 de secunde.

did_cd = 360 - did  # Numărătoarea inversă a gradelor din zi
# Calculăm câte grade mai sunt până la sfârșitul zilei. O zi are 360 de grade.

hid = min // 4  # Ora în grade
# Calculăm câte grade au trecut din oră, considerând că 1 grad este egal cu 4 minute.

hid_cd = 15 - hid  # Numărătoarea inversă a gradelor din oră
# Calculăm câte grade mai sunt până la sfârșitul orei. O oră are 15 grade.

# Stage III - SUMERIAN TIME SYSTEM
diss = dis // 2  # Ziua în secunde sumeriene
# În sistemul de timp sumerian, 1 secundă sumeriană reprezintă 2 secunde normale.

diss_cd = 43200 - diss  # Numărătoarea inversă a sec. sumeriene din zi
# Calculăm câte secunde sumeriene mai sunt până la sfârșitul zilei. O zi în secunde sumeriene are 43200 de secunde.

dism = dim // 2  # Ziua în minute sumeriene
# În sistemul de timp sumerian, 1 minut sumerian reprezintă 2 minute normale.

dism_cd = 720 - dism  # Numărătoarea inversă a minutelor sumeriene din zi
# Calculăm câte minute sumeriene mai sunt până la sfârșitul zilei. O zi în minute sumeriene are 720 de minute.

sh = hrs // 2  # Ziua în ore sumeriene (format de 12 ore)
# În sistemul de timp sumerian, 1 oră sumeriană reprezintă 2 ore normale.

sh_cd = 12 - sh  # Numărătoarea inversă a orelor sumeriene din zi
# Calculăm câte ore sumeriene mai sunt până la sfârșitul zilei. O zi sumeriană are 12 ore.

sm = dism - sh * 60  # Minutul sumerian
# Calculăm câte minute sumeriene au trecut din zi.

sm_cd = 60 - sm  # Numărătoarea inversă a minutelor sumeriene
# Calculăm câte minute sumeriene mai sunt până la sfârșitul zilei.

ss = diss - dism * 60  # Secunda sumeriană
# Calculăm câte secunde sumeriene au trecut din zi.

ss_cd = 60 - ss  # Numărătoarea inversă a secundelor sumeriene
# Calculăm câte secunde sumeriene mai sunt până la sfârșitul zilei.

syih = doy * 12 + sh  # Anul sumerian în ore
# Calculăm câte ore au trecut din anul sumerian, având în vedere că 1 an sumerian are 12 ore.

syih_cd = 4383 - syih  # Numărătoarea inversă a orelor sumeriene din an
# Calculăm câte ore sumeriene mai sunt până la sfârșitul anului sumerian. Un an sumerian are 4383 de ore.

syim = doy * 720 + dism  # Anul sumerian în minute
# Calculăm câte minute au trecut din anul sumerian.

syim_cd = 262980 - syim  # Numărătoarea inversă a minutelor sumeriene din an
# Calculăm câte minute sumeriene mai sunt până la sfârșitul anului sumerian. Un an sumerian are 262980 de minute.

syis = doy * 43200 + diss  # Anul sumerian în secunde
# Calculăm câte secunde sumeriene au trecut din anul sumerian.

syis_cd = 15778800 - syis  # Numărătoarea inversă a sec. sumeriene din an
# Calculăm câte secunde sumeriene mai sunt până la sfârșitul anului sumerian. Un an sumerian are 15778800 secunde.

# Stage IV - SUMERIAN TIME IN DEGREE
revolution = diss // 120  # Ziua în grade (pornind de la miezul nopții)
# Calculăm câte revoluții sumeriene au trecut din zi, considerând că o revoluție reprezintă 120 de secunde sumeriene.

revolution_cd = 360 - revolution  # Numărătoarea inversă a revoluțiilor din zi
# Calculăm câte revoluții mai sunt până la sfârșitul zilei.

syid = syis // 120  # Anul sumerian în grade
# Calculăm câte grade sumeriene au trecut din anul sumerian.

syid_cd = 131490 - syid  # Numărătoarea inversă a gradelor sumeriene din an
# Calculăm câte grade sumeriene mai sunt până la sfârșitul anului sumerian.

smon = syid // 10800  # Anul sumerian în luni (bazat pe cicluri de 360 de ore)
# Calculăm câte luni sumeriene au trecut din anul sumerian.

smon_cd = 12 - smon  # Numărătoarea inversă a lunilor sumeriene din an
# Calculăm câte luni sumeriene mai sunt până la sfârșitul anului sumerian.

shid = sm // 2  # Ora sumeriană în grade
# Calculăm câte grade sumeriene au trecut din oră.

shid_cd = 30 - shid  # Numărătoarea inversă a gradelor sumeriene din oră
# Calculăm câte grade sumeriene mai sunt până la sfârșitul orei.

# Stage V - OUTPUT
# Formatăm și afișăm timpul în diverse moduri

Time = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s\n"
print(Time % ("24hFORMAT", ":", f"+{hrs}:{min}:{sec}", ":", f"-{hrs_cd}:{min_cd}:{sec_cd}",
              "12hFORMAT", ":", f"+{sh}:{sm}:{ss}", ":", f"-{sh_cd}:{sm_cd}:{ss_cd}"))

# Afișăm diversele etape de calcul în formate similare

DayInHours = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s"
print(DayInHours % ("DayInHours", ":", f"+{hrs}", ":", f"-{hrs_cd}", "DayInSumerianHours", ":", f"+{sh}", ":", f"-{sh_cd}"))

DayInMinutes = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s"
print(DayInMinutes % ("DayInMinutes", ":", f"+{dim}", ":", f"-{dim_cd}", "DayInSumerianMinutes", ":", f"+{dism}", ":", f"-{dism_cd}"))

DayInSeconds = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s\n"
print(DayInSeconds % ("DayInSeconds", ":", f"+{dis}", ":", f"-{dis_cd}", "DayInSumerianSeconds", ":", f"+{diss}", ":", f"-{diss_cd}"))

YearInDays = "\n%20s%2s%10s%2s%10s"
print(YearInDays % ("YearInDays", ":", f"+{doy}", ":", f"-{doy_cd}"))

YearInHours = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s"
print(YearInHours % ("YearInHours", ":", f"+{yih}", ":", f"-{yih_cd}", "SumerianYearInHours", ":", f"+{syih}", ":", f"-{syih_cd}"))

YearInMinutes = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s"
print(YearInMinutes % ("YearInMinutes", ":", f"+{yim}", ":", f"-{yim_cd}", "SumerianYearInMinutes", ":", f"+{syim}", ":", f"-{syim_cd}"))

YearInSeconds = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s\n"
print(YearInSeconds % ("YearInSeconds", ":", f"+{yis}", ":", f"-{yis_cd}", "SumerianYearInSeconds", ":", f"+{syis}", ":", f"-{syis_cd}"))

DayInDegree = "\n%20s%2s%10s%2s%10s"
print(DayInDegree % ("DayInDegree", ":", f"+{did}", ":", f"-{did_cd}"))

HourInDegree = "\n%20s%2s%10s%2s%10s\t\t%22s%3s%10s%2s%10s\n"
print(HourInDegree % ("HourInDegree", ":", f"+{hid}", ":", f"-{hid_cd}", "SumerianHourInDegree", ":", f"+{shid}", ":", f"-{shid_cd}"))
