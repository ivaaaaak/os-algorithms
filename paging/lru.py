order = [8, 20, 11, 21, 8, 6, 9, 15, 3, 14, 2, 20, 17, 9, 12, 18, 7, 13, 16, 21, 16, 15, 10, 14, 3,
         23, 5, 24, 16, 9, 3, 2, 12, 24, 18]

ram_frames = []
limit_frames = 5

swap_cnt = 0


def address(arr: [], el: int) -> bool:
    for i in range(len(arr)):
        if arr[i][0] == el:
            arr[i][1] = 0
            return True
    return False


def find_lru_el(arr: []) -> [int, int]:
    tbr = [-1, -1]
    for i in arr:
        if tbr[1] < i[1]:
            tbr = i
    return tbr


def print_state(i: int, arr: [], el_queued: [], el_in: [] = [], el_out: [] = []):
    i += 1
    print(f"{i})\t {el_queued} \t--->\t {list(map(lambda x: x[0], arr))}, \tin: {el_in}, out: {el_out}")


def add_to_ram(element):
    for i in range(len(ram_frames)):
        ram_frames[i][1] += 1
    ram_frames.append([element, 0])


for i in range(len(order)):
    if address(ram_frames, order[i]):
        print_state(i, ram_frames, [order[i]])
        continue
    if len(ram_frames) < limit_frames:
        add_to_ram(order[i])
        print_state(i, ram_frames, [order[i]], el_in=[order[i]])
    else:
        to_remove = find_lru_el(ram_frames)
        ram_frames.remove(to_remove)
        swap_cnt += 1
        add_to_ram(order[i])
        print_state(i, ram_frames, [order[i]], [order[i]], [to_remove[0]])

print(f"Количество замен: {swap_cnt}")
print(f"Page fault: {swap_cnt / len(order)}%")
