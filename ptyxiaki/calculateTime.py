

def read_times():
    times = []
    with  open('./execution_time.txt', 'r') as f:
        for lines in f:
            times.append(lines.split())
    return times

def calculate_time(times):
    time_dict = {}
    for time in times:
        time_dict[time[0]] = 0.0
    for time in times:
        time_dict[time[0]] += float(time[1])
    for item in time_dict:
        time_dict[item] = time_dict[item]/5.0
    print(time_dict)
    write_times(time_dict,times)


def write_times(t_dict,times):
    with open('CRS_time.txt', 'w') as f:
        for key,value in t_dict.items():
            f.write("%s\t%s\n" % (key,value))


if __name__ == '__main__':
    times = read_times()
    calculate_time(times)
    # print(times)
