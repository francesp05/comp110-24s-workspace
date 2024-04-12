"""Testing Point class."""

from lessons.CQ08.point import Point

mypoint = Point(2.7, 5.9)

mypoint.scale_by = 2
mypoint.scale = 5

print(mypoint.scale_by)
print(mypoint.scale)