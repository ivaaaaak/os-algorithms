order = [8, 20, 11, 21, 8, 6, 9, 15, 3, 14, 2, 20, 17, 9, 12, 18, 7, 13, 16, 21, 16, 15, 10, 14, 3,
         23, 5, 24, 16, 9, 3, 2, 12, 24, 18]

ram_frames = []
limit_frames = 5

swap_cnt = 0


def exists(arr: [], el: int) -> bool:
    for i in arr:
        if i == el:
            return True
    return False


def find_farthest_el(arr: [], idx_from: int) -> int:
    farthest_pos = -1
    farthest_el = -1

    for frame in arr:
        for k in range(idx_from, len(order)):
            if order[k] == frame:
                if farthest_pos < k:
                    farthest_pos = k
                    farthest_el = frame
                break

        if k == len(order) - 1:
            farthest_el = frame
            break

    return farthest_el


def print_state(i: int, arr: [], el_queued: [], el_in=None, el_out=None):
    if el_out is None:
        el_out = []
    if el_in is None:
        el_in = []
    i += 1
    print(f"{i})\t {el_queued} \t--->\t {arr}, \tin: {el_in}, out: {el_out}")


for i in range(len(order)):
    if order[i] in ram_frames:
        print_state(i, ram_frames, [order[i]])
        continue
    if len(ram_frames) < limit_frames:
        ram_frames.append(order[i])
        print_state(i, ram_frames, [order[i]], el_in=[order[i]])
        continue
    else:
        to_remove = find_farthest_el(ram_frames, i)
        ram_frames.remove(to_remove)
        ram_frames.append(order[i])
        swap_cnt += 1
        print_state(i, ram_frames, [order[i]], [order[i]], [to_remove])

print(f"Количество замен: {swap_cnt}")
print(f"Page fault: {swap_cnt / len(order) * 100}%")
