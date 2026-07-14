# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def test_area_of_circle_negative_radius():
   """Test with a negative radius to raise ValueError."""
   # Arrange
   radius = -1

   # Act & Assert
   with pytest.raises(ValueError):
      area_of_circle(radius)
def test_get_nth_fibonacci_negative():
   """Test with a negative number to raise ValueError."""
   # Arrange
   n = -1

   # Act & Assert
   with pytest.raises(ValueError):
      get_nth_fibonacci(n)