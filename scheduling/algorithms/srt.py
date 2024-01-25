from scheduling.algorithms.algorithm import Algorithm


class SRT(Algorithm):

    def __init__(self):
        super().__init__()

    def start_task_on_cpu(self, tick_num):

        while len(self.CPU_queue) != 0:
            cpu_num = self.find_free_cpu(tick_num)

            if cpu_num is not None:
                min_process_size = self.serve_time[self.CPU_queue[0] - 1]
                shortest_process_ind = 0

                for j in range(1, len(self.CPU_queue)):
                    cur_process_size = self.serve_time[self.CPU_queue[j] - 1]
                    if cur_process_size < min_process_size:
                        min_process_size = cur_process_size
                        shortest_process_ind = j

                process_num = self.CPU_queue[shortest_process_ind]
                self.CPU_queue.remove(process_num)
                self.CPUs[cpu_num] += [process_num] * int(self.processes[process_num - 1][-1][1])
            else:
                break

        for j in range(len(self.CPUs)):
            if len(self.CPU_queue) != 0:
                cur_process_num = self.CPUs[j][tick_num]
                cur_process_size = self.serve_time[cur_process_num - 1]

                min_process_size = self.serve_time[self.CPU_queue[0] - 1]
                shortest_process_ind = 0

                for j in range(1, len(self.CPU_queue)):
                    cur_process_size = self.serve_time[self.CPU_queue[j] - 1]
                    if cur_process_size < min_process_size:
                        min_process_size = cur_process_size
                        shortest_process_ind = j

                new_process_num = self.CPU_queue[shortest_process_ind]
                new_process_size = self.serve_time[new_process_num - 1]

                if new_process_size < cur_process_size:
                    self.CPUs[j][tick_num:] = [new_process_num] * int(self.processes[new_process_num - 1][-1][1])
                    self.CPU_queue.remove(new_process_num)
            else:
                break

        for i in range(len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                self.CPUs[i].append(0)
            else:
                cur_process_num = self.CPUs[i][tick_num]
                self.processes[cur_process_num - 1][-1][1] = int(self.processes[cur_process_num - 1][-1][1]) - 1
                if self.processes[cur_process_num - 1][-1][1] == 0:
                    self.processes[cur_process_num - 1].pop()

    def check_if_displaced(self, cpu_num, tick_num):
        if tick_num == 0:
            return False
        if not self.check_if_cpu_free(cpu_num, tick_num) \
                and not self.check_if_cpu_free(cpu_num, tick_num - 1) \
                and self.CPUs[cpu_num][tick_num] != self.CPUs[cpu_num][tick_num - 1]:
            return True

    def update_cpu_queue(self, tick_num):
        if tick_num % 2 == 0 and tick_num <= 10:
            process_num = tick_num // 2 + 1
            self.CPU_queue.insert(0, process_num)

        for i in range(0, len(self.CPUs)):
            if self.check_if_displaced(i, tick_num):

                process_num = self.CPUs[i][tick_num - 1]

                if len(self.processes[process_num - 1]) == 0:
                    continue

                if self.processes[process_num - 1][-1][0] == "CPU" \
                        and type(self.processes[process_num - 1][-1][1]) is int:
                    self.CPU_queue.insert(0, process_num)

        for i in range(0, len(self.IOs)):
            process_num = self.get_ended_io_task_number(i, tick_num)

            if process_num is not None:
                if len(self.processes[process_num - 1]) == 0:
                    continue

                self.CPU_queue.insert(0, process_num)
