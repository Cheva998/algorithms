p = True
q = True

#p = False
#q = False

def juajua(p):
    print (p)
    return

#juajua(p)

#print (not (p or not q))
#print (y)

#n=123
#print( ((n - n % 10) / 10) % 10)
#print((n - n % 10) / 10)
#print(((n - n % 10) % 100) / 10)


#def fun_(x):
#    y= -5 *x**5 + 69* x**2 - 47
#    return y
#print(fun_(0), fun_(1), fun_(2), fun_(3))


#def future_value(present_value, annual_rate, periods_per_year, years):
#    rate_per_period = annual_rate / periods_per_year
#    periods = periods_per_year * years
#    fv=present_value*(1+rate_per_period)**periods
#    return fv
#print ("$1000 at 2% compounded daily for 3 years yields $", future_value(500, .04, 10, 10))
#print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))

#num_sides=7
#length=3 #s in the quiz
#import math
#ar=(1.0/4*num_sides*length**2)/math.tan(math.pi/num_sides)
#print (ar)


#def max_of_2(a, b):
#    if a > b:
#        return a
#    else:
#        return b
#
#def max_of_3(a, b, c):
#    return max_of_2(a, max_of_2(b, c))
#
#print (max_of_3(1,2,3))



def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)

import math
project_to_distance(2, 7, 4)



