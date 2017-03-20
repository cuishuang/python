import numpy

#numpy.array([1,2,3])
print(777)
cs = numpy.array([1,2,3])
print(cs)

print('\n')

height = [1.73,1.68,1.71,1.89,1.79]

weight = [65.4,59.2,63.6,88.4,68.7]


bmi = numpy.array(weight)/numpy.array(height) ** 2

print(bmi)
#输出的是[ 21.85171573  20.97505669  21.75028214  24.7473475   21.44127836]

#原来list和list是没法直接运算的,而numpy包将其变为了可以运算的;

print('\n')

print(bmi[1])
#输出的是20.9750566893

print(bmi>23)
#输出的是[False False False  True False]







