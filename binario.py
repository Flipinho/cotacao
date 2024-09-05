def decima_para_binario(num):
    if num == 0:
        return "0"
    binario = ""
    while num > 0:
        binario = str(num%2) + binario
        num = num // 2
    return binario

numd = int(input("Digite um numero ai: "))
binario = decima_para_binario(numd)
print(f"O numero decimal {numd} é assim em binario: {binario}")