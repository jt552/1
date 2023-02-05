import pandas
import psutil as ps
import time

cpu_list = []
mem_list = []
counter = 1200
while counter > 1:
    cpu_list.append(ps.cpu_percent())
    mem_list.append(ps.virtual_memory().percent)
    time.sleep(0.1)
    counter -= 1

data_cpu = pandas.DataFrame(cpu_list)
data_mem = pandas.DataFrame(mem_list)

data_cpu.to_csv("cpu.csv", index=False)
data_mem.to_csv("mem.csv", index=False)
