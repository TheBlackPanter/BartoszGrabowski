print("Kalkulator kosztów ubezpieczenia samochodu")

wiek_kierowcy = int(input("Podaj wiek kierowcy: "))
staz_kierowcy = int(input("Podaj staż kierowcy (w latach): "))
historia_prowadzenia_pojazdu = input("Czy kierowca miał wypadki lub kolizje w ciągu ostatnich 5 lat? (tak/nie): ")

winny_wypadek = None

if historia_prowadzenia_pojazdu == "tak":
    winny_wypadek = input("Czy kierowca był winny wypadku? (tak/nie): ")

typ_samochodu = input("Podaj typ samochodu (osobowy, dostawczy, ciężarowy): ")
wartosc_samochodu = float(input("Podaj wartość samochodu (w zł): "))
rodzaj_ubezpieczenia = input("Podaj rodzaj ubezpieczenia (OC, AC, AC+NW): ")
obszar_zamieszkania = input("Podaj obszar zamieszkania kierowcy (miasto, wieś): ")

czy_w_leasing = input("Czy samochód jest w leasing? (tak/nie): ")
marka_samochodu = input("Podaj markę samochodu: ")
rok_produkcji = int(input("Podaj rok produkcji samochodu: "))
rodzaj_paliwa = input("Podaj rodzaj paliwa (benzyna, diesel, elektryk, gaz): ")
pojemnosc_silnika = float(input("Podaj pojemność silnika (w litrach): "))
stan_licznika = int(input("Podaj stan licznika samochodu (w tysiącach kilometrów): "))
przejazd_rok = int(input("Podaj planowany przejazd samochodu w ciągu najbliższych 12 miesięcy (w kilometrach): "))
rok_wlasciciela = int(input("Podaj rok, od którego jesteś właścicielem auta: "))
miejsce_parkowania_noc = input("Podaj miejsce, gdzie samochód będzie najczęściej parkowany nocą(ulica, garaż, parking prywatny): ")
plec_wlasciciela = input("Podaj płeć właściciela samochodu (mężczyzna, kobieta, inny): ")
stan_cywilny_wlasciciela = input("Podaj stan cywilny właściciela samochodu (kawaler, żonaty, rozwiedziony, wdowiec): ")

cena_ubezpieczenia = 0

if typ_samochodu == "osobowy":
    cena_ubezpieczenia += 500
elif typ_samochodu == "dostawczy":
    cena_ubezpieczenia += 800
elif typ_samochodu == "ciężarowy":
    cena_ubezpieczenia += 1200

if wartosc_samochodu > 100000:
    cena_ubezpieczenia *= 1.2

if wiek_kierowcy < 25:
    cena_ubezpieczenia *= 1.2
elif wiek_kierowcy > 65:
    cena_ubezpieczenia *= 1.5

if staz_kierowcy < 2:
    cena_ubezpieczenia *= 1.3
elif staz_kierowcy > 10:
    cena_ubezpieczenia *= 0.8

if historia_prowadzenia_pojazdu == "tak":
    cena_ubezpieczenia *= 1.5
    if winny_wypadek == "tak":
        cena_ubezpieczenia *= 1.8

if rodzaj_ubezpieczenia == "OC":
    cena_ubezpieczenia *= 0.5
elif rodzaj_ubezpieczenia == "AC":
    cena_ubezpieczenia *= 0.8
elif rodzaj_ubezpieczenia == "AC+NW":
    cena_ubezpieczenia *= 1.2

if obszar_zamieszkania == "miasto":
    cena_ubezpieczenia *= 1.5

if czy_w_leasing == "tak":
    cena_ubezpieczenia *= 1.2

if marka_samochodu == "BMW":
    cena_ubezpieczenia *= 5

if rok_produkcji < 2010:
    cena_ubezpieczenia *= 1.3

if rodzaj_paliwa == "diesel":
    cena_ubezpieczenia *= 1.2

if pojemnosc_silnika > 2.0:
    cena_ubezpieczenia *= 1.5

if stan_licznika > 100:
    cena_ubezpieczenia *= 1.2

if przejazd_rok > 20000:
    cena_ubezpieczenia *= 1.3

if miejsce_parkowania_noc == "ulica":
    cena_ubezpieczenia *= 1.2

if plec_wlasciciela == "kobieta":
    cena_ubezpieczenia *= 0.9

print("\nPodsumowanie wprowadzonych danych:")
print("----------------------------------")
print(f"Wiek kierowcy: {wiek_kierowcy}")
print(f"Staż kierowcy: {staz_kierowcy} lat")
print(f"Czy kierowca miał wypadki lub kolizje w ciągu ostatnich 5 lat? {historia_prowadzenia_pojazdu}")
if historia_prowadzenia_pojazdu == "tak":
    print(f"Czy kierowca był winny wypadku? {winny_wypadek}")
print(f"Typ samochodu: {typ_samochodu}")
print(f"Wartość samochodu: {wartosc_samochodu} zł")
print(f"Rodzaj ubezpieczenia: {rodzaj_ubezpieczenia}")
print(f"Obszar zamieszkania: {obszar_zamieszkania}")
print(f"Czy samochód jest w leasing? {czy_w_leasing}")
print(f"Marka samochodu: {marka_samochodu}")
print(f"Rok produkcji samochodu: {rok_produkcji}")
print(f"Rodzaj paliwa: {rodzaj_paliwa}")
print(f"Pojemność silnika: {pojemnosc_silnika} l")
print(f"Stan licznika samochodu: {stan_licznika} tys. km")
print(f"Rok, od którego jesteś właścicielem auta: {rok_wlasciciela}")
print(f"Rok pierwszej rejestracji samochodu: {miejsce_rejestracji}")
print(f"Miejsce parkowania samochodu nocą: {miejsce_parkowania_noc}")
print(f"Numer rejestracyjny samochodu: {numer_rejestracyjny}")
print(f"Płeć właścicielasamochodu: {plec_wlasciciela}")
print(f"Stan cywilny właściciela samochodu: {stan_cywilny_wlasciciela}")

print("\nKoszt ubezpieczenia samochodu:")
print("-----------------------------")
print(f"Koszt ubezpieczenia samochodu wynosi {cena_ubezpieczenia} złotych.")
print("-------------------------------")
print("Dziękujemy za skorzystanie z naszego kalkulatora kosztów ubezpieczenia samochodu.")

numer_telefonu = input("Podaj numer telefonu: ")
print(f"Dziękujemy za podanie numeru telefonu: {numer_telefonu}. Skontaktujemy się z Tobą wkrótce.")