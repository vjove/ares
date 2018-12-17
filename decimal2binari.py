def decimal2binari(n):
    r = n   # resto
    m = 0   # mòdul

    binari = ""
    while r > 0:
        m = r%2
        r = r//2
        binari = "%s%s" % (m, binari)

    if binari == "":
        binari = "0"

    return binari


def convert_input():
    n = int(input("Introdueix un número: "))
    print("El teu número en decimal és: %s" % n)

    binari = decimal2binari(n)
    print("El teu número en binari és: %s" % binari)


def show(n):
    for i in range(n):
        print("Decimal %s, Binari: %s" % (i, decimal2binari(i)))


show(100)
