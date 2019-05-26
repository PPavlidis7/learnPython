def create_dicts():
    time_dict = {
        'CSR': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        },
        'CSC': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        },
        'COO': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        },
        'CSR3': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        },
        'COO3': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        },
        'Diagonal': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0
        },
    }

    read_time_dict = {
        'comprese_v2': {
            '5000': 0, '7000': 0, '9000': 0, '11000': 0, '13000': 0, '15000': 0,
            '17000': 0, '19000': 0, '21000': 0, '23000': 0
        }
    }
    return time_dict, read_time_dict


def read_exec_times():
    times = []
    with open('./execution_time.txt', 'r') as f:
        for lines in f:
            times.append(lines.split())
    return times


def read_read_times():
    times = []
    with open('./read_time.txt', 'r') as f:
        for lines in f:
            times.append(lines.split())
    return times


def calculate_time(times,time_dict,type):
    for time in times:
        time_dict[time[0]][time[1]] += float(time[2])

    for item in time_dict:
        for inner_item in time_dict[item]:
            if item != 'Diagonal':
                time_dict[item][inner_item] = time_dict[item][inner_item]/5.0

    # print(time_dict)
    write_times(time_dict,type)


def write_times(t_dict, type):
    file_name = 'exec_times_final.txt'
    if type == 'read':
        file_name = 'read_times_final.txt'

    with open(file_name, 'w') as f:
        for key, inner_dict in t_dict.items():
            for key_inner, value in inner_dict.items():
                f.write("%s\t%s\t%s\n" % (key, key_inner, value))


if __name__ == '__main__':
    exec_time, read_time = create_dicts()
    exec_times_file = read_exec_times()
    calculate_time(exec_times_file,exec_time, 'exec')
    read_times_file = read_read_times()
    calculate_time(read_times_file, read_time, 'read')
