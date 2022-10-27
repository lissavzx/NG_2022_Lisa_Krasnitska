import math
print ('ax^2+bx+c=0:')
a = int(input ('Enter your a'))
b = int(input ('Enter your b'))
c = int(input ('Enter your c'))
print ('discriminant d= ')
discr = (b**2-4*a*c)
if discr>0:
    x1 = (-b + math.sqrt(discr) )/(2*a)
    x2 = (-b-math.sqrt(discr))/(2*a)
    print('x1 =', x1,'x2 = ', x2 )

elif discr == 0:
    x = -b/(2*a)
    print('x=', x)
else:
    print('no roots')
