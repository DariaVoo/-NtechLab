def findMaxSubArray(arr: list):
    curr_sum: int = 0
    best_sum: int = 0
    best_arr: list

    for end, x in enumerate(arr):
        if curr_sum <= 0:
            # Начинаем новый подмассив с текущего элемента
            start = end
            curr_sum = x
        else:
            # Добавляем элемент в текущий подмассив
            curr_sum += x
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_arr = arr[start:end + 1]
    return best_arr


def main():
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sub_arr = findMaxSubArray(A)
    print(sub_arr)


if __name__ == "__main__":
    main()
