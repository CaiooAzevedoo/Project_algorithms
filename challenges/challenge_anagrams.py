def is_anagram(first_string, second_string):
    f_sorted = list(first_string.lower())
    s_sorted = list(second_string.lower())

    merge_sort(f_sorted)
    merge_sort(s_sorted)

    first = "".join(f_sorted)
    second = "".join(s_sorted)

    if len(first) == 0 or len(second) == 0:
        return (first, second, False)
    if first == second:
        return (first, second, True)
    if first != second:
        return (first, second, False)


# Função merge_sort
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/73f2a1d5-7d77-440b-a9f2-3ea9750db228/day/346e18ae-25d8-47a5-bd59-0e4d9cd2a2d2/lesson/9b22b10c-1e8a-4f00-bab8-edac69573b6b

def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
