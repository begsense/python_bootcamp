def generate_list(n: int) -> list[int]:
    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        list.append(n)
    return list

def generate_list_by_cache(n: int, cache: dict[int, list[int]]) -> list[int]:
    if n in cache:
        return cache[n]
    
    if n == 1:
        cache[1] = [1]
        return [1]
    
    list = [n]
    if n % 2 == 0:
        next_num = n // 2
    else:
        next_num = n * 3 + 1
    
    rest_of_list = generate_list_by_cache(next_num, cache)
    
    full_list = list + rest_of_list
    
    cache[n] = full_list

    return full_list

def main():
    print(generate_list(10))
    print(generate_list_by_cache(10, {}))

if __name__ == '__main__': 
    main()