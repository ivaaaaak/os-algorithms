from abc import abstractmethod, ABC


class Algorithm(ABC):

    def __init__(self):
        self.CPUs = [[], [], [], []]
        self.IOs = [[], []]
        self.CPU_queue = []
        self.IO_queues = [[], []]
        self.processes = []
        self.serve_time = []

    def get_serve_times(self):
        self.serve_time.clear()
        for i in range(0, len(self.processes)):
            self.serve_time.append(0)
            for j in range(0, len(self.processes[i])):
                self.serve_time[i] += int(self.processes[i][j][1])

    def find_free_cpu(self, tick_num):
        for i in range(0, len(self.CPUs)):
            if self.check_if_cpu_free(i, tick_num):
                return i
        return None

    def check_if_cpu_free(self, cpu_num, tick_num):
        if tick_num == 0:
            return True
        return len(self.CPUs[cpu_num]) == tick_num or self.CPUs[cpu_num][tick_num] == 0

    def check_if_io_free(self, io_num, tick_num):
        if tick_num == 0:
            return True
        return len(self.IOs[io_num]) == tick_num

    def check_if_cpu_task_is_over(self, cpu_num, tick_num):
        if tick_num == 0:
            return False
        if len(self.CPUs[cpu_num]) == tick_num + 1 and self.CPUs[cpu_num][tick_num] != 0:
            return True
        return False

    def check_if_io_task_is_over(self, io_num, tick_num):
        if tick_num == 0:
            return False
        if len(self.IOs[io_num]) == tick_num + 1 and self.IOs[io_num][tick_num] != 0:
            return True
        return False

    def get_ended_cpu_task_number(self, cpu_num, tick_num):
        if self.check_if_cpu_task_is_over(cpu_num, tick_num):
            return self.CPUs[cpu_num][tick_num]
        return None

    def get_ended_io_task_number(self, io_num, tick_num):
        if self.check_if_io_task_is_over(io_num, tick_num):
            return self.IOs[io_num][tick_num]
        return None

    @abstractmethod
    def start_task_on_cpu(self, tick_num):
        pass

    def start_task_on_io(self, tick_num):
        for i in range(0, len(self.IOs)):

            if len(self.IO_queues[i]) != 0 and self.check_if_io_free(i, tick_num):
                process_num = self.IO_queues[i].pop()
                self.IOs[i] += [process_num] * int(self.processes[process_num - 1].pop()[1])

            elif self.check_if_io_free(i, tick_num):
                self.IOs[i].append(0)

    def update_io_queue(self, tick_num):
        for i in range(len(self.CPUs)):
            process_num = self.get_ended_cpu_task_number(i, tick_num)

            if process_num is not None:
                if len(self.processes[process_num - 1]) == 0:
                    continue
                next_task = self.processes[process_num - 1][-1]

                if next_task[0] == "IO1":
                    self.IO_queues[0].insert(0, process_num)

                elif next_task[0] == "IO2":
                    self.IO_queues[1].insert(0, process_num)

    def update_cpu_queue(self, tick_num):
        if tick_num % 2 == 0 and tick_num <= 10:
            process_num = tick_num // 2 + 1
            self.CPU_queue.insert(0, process_num)

        for i in range(0, len(self.IOs)):
            process_num = self.get_ended_io_task_number(i, tick_num)

            if process_num is not None:
                if len(self.processes[process_num - 1]) == 0:
                    continue

                self.CPU_queue.insert(0, process_num)

    def check_all_processes_end(self, tick_num):
        for i in range(len(self.processes)):
            if len(self.processes[i]) != 0:
                return False
            for j in range(len(self.CPUs)):
                if not self.check_if_cpu_free(j, tick_num):
                    return False
            for j in range(len(self.IOs)):
                if not self.check_if_io_free(j, tick_num):
                    return False
        return True

    def handle_tick(self, tick_num):
        self.start_task_on_cpu(tick_num)
        self.start_task_on_io(tick_num)

        self.update_io_queue(tick_num)
        self.update_cpu_queue(tick_num)

    def get_processes_from_task(self, task_file):
        self.processes.clear()
        with open(task_file, "r") as f:
            for line in f:
                new_process = line.rstrip().split(";")
                new_process.reverse()
                self.processes.append([[task[0:3], task[4:-1]] for task in new_process])

    def process_scheduling(self, task_file):
        self.get_processes_from_task(task_file)
        self.get_serve_times()

        tick = 0
        while not self.check_all_processes_end(tick):
            self.handle_tick(tick)
            tick += 1
