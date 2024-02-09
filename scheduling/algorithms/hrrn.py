from scheduling.algorithms.algorithm import Algorithm


class HRRN(Algorithm):

    def __init__(self):
        super().__init__()
        self.wait_time = [0] * 6

    def __str__(self):
        return "HRRN"

    def start_task_on_cpu(self, tick_num):
        while len(self.CPU_queue) != 0:
            cpu_num = self.find_free_cpu(tick_num)

            if cpu_num is not None:
                process_num = self.CPU_queue[0] - 1
                min_r = (self.wait_time[process_num] + self.serve_time[process_num]) / self.serve_time[process_num]
                min_ind = 0

                for i in range(1, len(self.CPU_queue)):
                    process_num = self.CPU_queue[i] - 1
                    r = (self.wait_time[process_num] + self.serve_time[process_num]) / self.serve_time[process_num]
                    if r < min_r:
                        min_r = r
                        min_ind = i

                process_num = self.CPU_queue[min_ind]
                self.CPU_queue.remove(process_num)
                self.CPUs[cpu_num] += ([process_num] * int(self.processes[process_num - 1].pop()[1]))
            else:
                break

        for i in range(1, len(self.CPU_queue)):
            process_num = self.CPU_queue[i] - 1
            self.wait_time[process_num] += 1

        for i in range(len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                self.CPUs[i].append(0)
