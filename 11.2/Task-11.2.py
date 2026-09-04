import math


points = [[2.0, 0.0, -0.2], [3.5, 1.0, -0.3], [1.5, -0.8, -0.1]]
tx = 0.5
ty = 0.0
tz = 0.2
theta = math.radians(15)


for point in points:
    xc, yc, zc = point[0], point[1], point[2]
    
    xb = xc * math.cos(theta) - zc * math.sin(theta) + tx
    yb = yc + ty
    zb = xc * math.sin(theta) + zc * math.cos(theta) + tz
    

    print(f"Transformed: [{xb:.2f}, {yb:.2f}, {zb:.2f}]")
  