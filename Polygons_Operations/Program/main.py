from poligon import *

polygon1 = []
polygon2 = []
create_polygon(polygon1,'date.txt')
create_polygon(polygon2,'date2.txt')
print("The polygon has the following coordinates")
print_poligon(polygon1)
get_rectangle(polygon1)
print("The polygon area is ", get_polygon_area(polygon1))
print("The perimeter of polygon is ", get_perimeter(polygon1))
if IsConvex(polygon1):
    print("It is convex")
else:
    print("It is not convex")
compare_polygons(polygon1, polygon2)
puncte_convex = concatenate(polygon1,polygon2)
print("The resulted polygon from concatenation has the following coordinates")
print_poligon(puncte_convex)
