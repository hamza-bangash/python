def even_weight(kilo):
    if kilo%2==0 and kilo > 2:
        return 'YES'
    else:
        return 'NO'
    
kilo = int(input())
print(even_weight(kilo))