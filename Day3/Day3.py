import math

def quadratic_calcula(a,b,c):
    if a == 0:
        print(" Phương trình có nghiệm là: ", -b/c)
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            print("Phương trình có 2 nghiệm là :", (-b-math.sqrt(delta))/(2*a),(-b+math.sqrt(delta))/(2*a))
        elif delta==0:
            print("Phương trình có nghiệm kép là : ", -b/2*a)
        else: 
            print("Phương trình vô nghiệm")

quadratic_calcula(2,6,4)
quadratic_calcula(1,2,1)
quadratic_calcula(4,6,3)
#36 - 4*2*4