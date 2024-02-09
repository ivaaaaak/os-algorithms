import sys

from texttable import Texttable

from scheduling.algorithms.fcfs import FCFS
from scheduling.algorithms.hrrn import HRRN
from scheduling.algorithms.rr import RR
from scheduling.algorithms.spn import SPN
from scheduling.algorithms.srt import SRT


def print_result(algorithm):
    print(f"\n{algorithm}\n")

    t = Texttable()
    t.set_deco(Texttable.HEADER | Texttable.BORDER)
    t.add_row(['time', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'IO1', 'IO2'])

    for i in range(1, len(algorithm.CPUs[0])):
        t.add_row(
            [i, algorithm.CPUs[0][i], algorithm.CPUs[1][i], algorithm.CPUs[2][i], algorithm.CPUs[3][i], algorithm.IOs[0][i], algorithm.IOs[1][i]])
    print(t.draw())

    print("\n")
    algorithm.get_processes_from_task(task_file)

    for i in range(len(algorithm.serve_time)):
        print(f"Время обслуживания процесса {i + 1}: {algorithm.serve_time[i]}")

    print("\n")
    turnoverTime = []
    for i in range(len(algorithm.processes)):
        turnoverTime.append(0)
        for j in range(len(algorithm.IOs)):
            for k in range(len(algorithm.IOs[j])):
                if algorithm.IOs[j][k] == (i + 1) and turnoverTime[i] <= k:
                    turnoverTime[i] = k
        print(f"Время оборота процесса {i + 1}: {turnoverTime[i] - (1 + i * 2)}")

    print("\n")
    for i in range(len(algorithm.processes)):
        print(f"Коэффициент голодания {i + 1}: {turnoverTime[i] / algorithm.serve_time[i]}")


def main(task_file):
    f = FCFS()
    f.process_scheduling(task_file)
    print_result(f)

    rr = RR(1)
    rr.process_scheduling(task_file)
    print_result(rr)

    rr = RR(4)
    rr.process_scheduling(task_file)
    print_result(rr)

    spn = SPN()
    spn.process_scheduling(task_file)
    print_result(spn)

    srt = SRT()
    srt.process_scheduling(task_file)
    print_result(srt)

    hrrn = HRRN()
    hrrn.process_scheduling(task_file)
    print_result(hrrn)


if __name__ == "__main__":
    assert len(sys.argv) == 2, "Wrong arguments: main.py <task_file>"
    _, task_file = sys.argv
    main(task_file)
