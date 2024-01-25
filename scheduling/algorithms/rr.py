from scheduling.algorithms.algorithm import Algorithm


class RR(Algorithm):

    def __init__(self, time):
        super().__init__()
        self.time = time

    def start_task_on_cpu(self, tick_num):
        while len(self.CPU_queue) != 0:
            cpu_num = self.find_free_cpu(tick_num)

            if cpu_num is not None:
                process_num = self.CPU_queue.pop()

                size = self.time if int(self.processes[process_num - 1][-1][1]) > self.time else int(
                    self.processes[process_num - 1][-1][1])

                self.CPUs[cpu_num] += [process_num] * size

                self.processes[process_num - 1][-1][1] = int(self.processes[process_num - 1][-1][1]) - size

                if int(self.processes[process_num - 1][-1][1]) <= 0:
                    self.processes[process_num - 1].pop()
            else:
                break

        for i in range(0, len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                self.CPUs[i].append(0)

    def update_cpu_queue(self, tick_num):
        if tick_num % 2 == 0 and tick_num <= 10:
            process_num = tick_num // 2 + 1
            self.CPU_queue.insert(0, process_num)

        for i in range(0, len(self.CPUs)):
            process_num = self.get_ended_cpu_task_number(i, tick_num)

            if process_num is not None:
                if len(self.processes[process_num - 1]) == 0:
                    continue

                if self.processes[process_num - 1][-1][0] == "CPU":
                    self.CPU_queue.insert(0, process_num)

        for i in range(0, len(self.IOs)):
            process_num = self.get_ended_io_task_number(i, tick_num)

            if process_num is not None:
                if len(self.processes[process_num - 1]) == 0:
                    continue

                self.CPU_queue.insert(0, process_num)
