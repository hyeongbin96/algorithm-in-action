import math

fir_bunja, fir_bunmo = map(int, input().split())
sec_bunja, sec_bunmo = map(int, input().split())

bunja = (fir_bunja * sec_bunmo) + (sec_bunja * fir_bunmo)
bunmo = fir_bunmo * sec_bunmo

if math.gcd(bunja, bunmo) > 1 :
    gcd = math.gcd(bunja, bunmo)
    bunja = bunja // gcd
    bunmo = bunmo // gcd
    print(bunja, bunmo)
else :
    print(bunja, bunmo)