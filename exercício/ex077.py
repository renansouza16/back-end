valores = []
for c in range(0,5):
    num = int(input('digite um valor'))
    if c == 0:
        valores.append(num)
    elif num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores): 
            if num <= valores[pos]:
                valores.insert(pos, num) 
                break
            pos+=1
print(f"Os valores digitados em ordem foram {valores}")
