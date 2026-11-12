def square(side):
    area = side * side
    if area != int(area):
        area = int(area) + 1
    return area

print(square(2.1))
print(square(2))