def chunk_data(data: list[int], chunk_size: int) -> tuple[int]:
    return tuple(data[i:i + chunk_size] for i in range(0, len(data), chunk_size))


print(chunk_data([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))