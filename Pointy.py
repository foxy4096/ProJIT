import math
from dataclasses import dataclass


@dataclass
class Grid:
    """
    Represents a grid of points.
    """

    points: list["Point"]
    width: int
    height: int
    cell_size: int

    def draw(self):
        """
        Draws the grid on the screen.
        """
        for y in range(0, self.height, self.cell_size):
            for x in range(0, self.width, self.cell_size):
                # Find the point in the grid that is closest to the current cell
                closest_point = min(
                    self.points, key=lambda p: p.distance(Point(x, y))
                )

                # Draw the closest point on the screen
                print(f"({closest_point.x}, {closest_point.y})", end="")
            print()
        print()
        print(f"Total points: {len(self.points)}")
        print(f"Cell size: {self.cell_size}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print()
        

@dataclass
class Point:
    """Represents a point in 2D space."""

    x: float
    y: float

    def distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): The other point to calculate the distance to.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# # Get input from the user for the coordinates of two points.
# x1, y1 = map(
#     float, input("Enter coordinates for the first point (separated by space): ").split()
# )
# x2, y2 = map(
#     float,
#     input("Enter coordinates for the second point (separated by space): ").split(),
# )

# # Create Point objects for the two coordinates.
# point1 = Point(x1, y1)
# point2 = Point(x2, y2)

# # Calculate and display the distance between the two points.
# distance = point1.distance(point2)
# print(f"The distance between the two points is: {distance}")

# Example usage:
    
import random

points = [Point(random.randint(0, 5), random.randint(0, 5)) for _ in range(25)]

grid = Grid(points, 100, 100, 1)

grid.draw()
