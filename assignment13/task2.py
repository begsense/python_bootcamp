def midpoint(x1: int, y1: int, x2: int, y2: int) -> tuple[float, float]:
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def main():
    print(midpoint(1, 2, 3, 4))
    print(midpoint(5, 3, 7, 8))
    print(midpoint(10, 5, 4, 9))
    result = midpoint(1, 2, 3, 4)
    print(type(result[0]))

if __name__ == '__main__': 
    main()