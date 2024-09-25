n = 1
tri = False
per = int(input("digite um numero maior que 0 "))

while n*(n+1)*(n+2)<=per:
    n=n+1
    
    if n*(n+1)*(n+2)==per:
        tri = True
        break
    
if tri == True:
    print(f"triangular {n,n+1,n+2}")
else:
     print("Não triangular")