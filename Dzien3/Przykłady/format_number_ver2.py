"""
    W Pythonie można użyć adnotacji (ang. annotations)
    do wskazania oczekiwanego typu ale nie wpływa wykonywanie kodu
    Adnotacje są zatem informacjami dla programisty, a nie wymogiem
    """


def format_number(
    num: float,
    separator_thousands: str = ' ',
    separator_decimal: str = ',',
    decimal_places: int = 2
) -> str:
    """
    Formatuje liczbę:
    - separator_thousands: separator tysięcy (domyślnie spacja)
    - separator_decimal: separator części dziesiętnej (domyślnie przecinek)
    - decimal_places: liczba miejsc po przecinku (domyślnie 2)
    """
    # Formatowanie do postaci z przecinkiem jako tysiące i kropką dziesiętną
    formatted = f"{num:,.{decimal_places}f}"

    # Zamiana separatorow
    formatted = formatted.replace(",", "XyX")
    formatted = formatted.replace(".", separator_decimal)
    formatted = formatted.replace("XyX", separator_thousands)

    return formatted


print(format_number(43234.9))                          # 43 234,90
print(format_number(1234567.891, decimal_places=3))   # 1 234 567,891
print(format_number(1234567.8, separator_thousands=',',
      separator_decimal='.'))  # 1,234,567.80
print(format_number(1000, decimal_places=0))          # 1 000
