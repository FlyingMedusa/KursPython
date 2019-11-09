import Zad2Figures as Fig
import experiment

square_side = 4
circle_radius = 3
trap_side_a = 3
trap_side_b = 5
trap_height = 4
triangle_side = 6
triangle_height = 5

square = Fig.square_field(square_side)
circle = Fig.circle_field(circle_radius)
trapezium = Fig.trapezium_field(trap_side_a, trap_side_b, trap_height)
triangle = Fig.triangle_field(triangle_side, triangle_height)

print(square, circle, trapezium, triangle)