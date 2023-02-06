odd=set()                           
for x in range(0,11):               
    if x%2!=0:                      
        odd.add(x)                 
primes=set()
for i in range(2,10):
    j=2
    f=0
    while j<=i/2:
        if i%j==0:
            f=1 
        j+=1
    if f==0:
        primes.add(i)
print("odd number:",odd)
print("prime number:", primes)
print("union:", odd.union(primes))
print("intersection",odd.intersection(primes))
print("difference", odd.difference(primes))
print("symmetric difference",odd.symmetric_difference(primes))
