from collections import deque


class Robot:
    """A class that defines our robot and calculates the size of the area he can access"""

    SAFE_LIMIT = 23
    STARTING_POINT = (0, 0)

    def check_point_safe(self, point):
        """Returns True if the sum of digits of the valid point's x and y values is less than or equal to SAFE_LIMIT, false otherwise."""
        if (not point or type(point) is not tuple or len(point) != 2):
            raise ValueError("point argument is not a valid (x, y) point")

        point_sum_digits = 0
        x = abs(point[0])
        y = abs(point[1])
        points = [x, y]

        for p in points:
            point_sum_digits += self.get_sum_of_digits(p)
            if point_sum_digits > self.SAFE_LIMIT:
                return False

        return True

    def get_sum_of_digits(self, num):
        """Returns the sum of the digits of the absolute value of integer num."""
        if (num < 0):
            num *= -1
        sum_digits = 0
        num_str = str(num)

        for d in num_str:
            sum_digits += int(d)

        return sum_digits

    def calculate_accessible_area(self):
        """Returns the area accesible by the robot."""
        visited = {self.STARTING_POINT}
        queue = deque([self.STARTING_POINT])

        while(queue):
            current = queue.popleft()
            neighbors = self.get_neighbors(current)
            for n in neighbors:
                if n not in visited and self.check_point_safe(n):
                    visited.add(n)
                    queue.append(n)

        return len(visited)

    def get_neighbors(self, point):
        """Returns the neighbor points of the current point accessible by our robot."""
        if (not point or type(point) is not tuple or len(point) != 2):
            raise ValueError("point argument is not a valid (x, y) point")

        top = (point[0], point[1] + 1)
        right = (point[0] + 1, point[1])
        bottom = (point[0], point[1] - 1)
        left = (point[0] - 1, point[1])

        return [top, right, bottom, left]


if __name__ == '__main__':
    robot = Robot()
    area = robot.calculate_accessible_area()
    print(area)
