from scheduling.algorithms.algorithm import Algorithm


class FCFS(Algorithm):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "FCFS"

    def start_task_on_cpu(self, tick_num):
        while len(self.CPU_queue) != 0:
            cpu_num = self.find_free_cpu(tick_num)

            if cpu_num is not None:
                process_num = self.CPU_queue.pop()
                self.CPUs[cpu_num] += ([process_num] * int(self.processes[process_num - 1].pop()[1]))
            else:
                break

        for i in range(0, len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                self.CPUs[i].append(0)
