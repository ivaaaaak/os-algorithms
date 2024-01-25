from scheduling.algorithms.fcfs import Algorithm


class SPN(Algorithm):

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
                self.CPUs[cpu_num] += [process_num] * int(self.processes[process_num - 1].pop()[1])

            else:
                break

        for i in range(0, len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                self.CPUs[i].append(0)
