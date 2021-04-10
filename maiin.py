import math

Pnmax = 79000
nPmax = 90
Mmax = 157
nMmax = 63.3333
m = 1000
mmax = 1495
ik = []
ik.append(3.46)
ik.append(2.12)
ik.append(1.44)
ik.append(0.89)
i0 = 3.67
l = 4385
d = 1675
h = 1405
dtengely = 2475
dnyom = 1427
dnyom2 = 1422
clev = 0.35
gör = 0.01
nű = 0.91
redáll = 1.05
alfa = math.radians(math.atan(15 / 100))
tap = 0.8
g = 9.81

print('1.')
rk = 270
print('rk: ', rk)

file = open("dat.txt", "a")

print('2.')
MPmax = Pnmax / (2 * math.pi * nPmax)
print('Mpmax: ', MPmax)
#print('MMmax: ', Pnmax / (2 * math.pi * nMmax))
print()

print('3.')
print('Pmmax: ', Mmax * 2 * math.pi * nMmax)
print()

print('4.')

FgsM = m * g * nMmax
FgsP = m * g * nPmax
print('Fgs (M): ', FgsM)
print('Fgs (P): ', FgsP)
print()

FgeM = m * g * nMmax * math.cos(alfa)
FgeP = m * g * nPmax * math.cos(alfa)
print('Fge (M): ', FgeM)
print('Fge (P): ', FgeP)
print()

Fe = m * g * math.sin(alfa)
print('Fe: ', Fe)
print()

for i in ik:
    print('fokozat: ', ik.index(i) + 1)

    Vkm = (rk * 2 * math. pi * nMmax) / (i0 * i)
    Vkp = (rk * 2 * math. pi * nPmax) / (i0 * i)

    print('Vk (M): ', Vkm)
    print('Vk (P): ', Vkp)

    #km/h to m/s
    Vkm *= 0.27777
    Vkp *= 0.27777

    FkM = (Mmax * i0 * i * nű) / rk
    FkP = (MPmax * i0 * i * nű) / rk
    print('Fk (M)', FkM)
    print('Fk (M)', FkP)

    FlegM = 0.5 * 0.78 * h * d * clev * 1.23 * Vkm ** 2
    FlegP = 0.5 * 0.78 * h * d * clev * 1.23 * Vkp ** 2
    print('Flég (M): ', FlegM)
    print('Flég (P): ', FlegP)

    FgyM = FkM - (FgeM + Fe + FlegM)
    FgyP = FkP - (FgeP + Fe + FlegP)
    print('Fgy (M): ', FgyM)
    print('Fgy (P): ', FgyP)

    #valami fontos passz
    ro = 1
    print('emelkedőn:')
    print('a (M): ', FgyM / (m * ro))
    print('a (p): ', FgyP / (m * ro))
    print()

    print('Dinamika: ', (FkP - FlegP) / m * g)
    print()
    print()


print()
file.close()


