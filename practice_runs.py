import math 
w = 185
a = 50
d = 14

# incorrect attempts:
# v = complex(math.pi * w * w * a * (w * a + 2540 * d) / 10,000,000,000)
# v = math.pi * (w * w) * a * (w * a + 2540 * d) / 10,000,000,000
# v = math.pi * w * w * a * (w * a + 2540 * d) / 10,000,000,000

# current attempt:
p1 = float(math.pi * (w * w) * a)
p2 = float(w * a + 2540 * d)
v = complex(p1 * p2 / 10,000,000,000)

print(v, 'is of type', type(v))
print (f"The approximate volume is {v:.2f} liters")