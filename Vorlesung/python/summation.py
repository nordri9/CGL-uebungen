def get_summation_sq(number):
    summ = 0
    for i in range(1,number+1):
        summ += i**2
#        print(i,":",summ)
    return summ

    assert isinstance(number,int) and number >=1, "Die zahl ist keine natürlche positive Zahl"
print(get_summation_sq(10))

assert get_summation_sq(10) == (10*(10+1)*(2*10+1))/6
