# python3

def parallel_processing(n, m, data):
    #output = []
    time = 0
    task = 0
    schedule = [0] * n
    for task_time in data:
        time = time + task_time

    for i in range(time):
        for j in range(n):
            if (schedule[j]<=i and task < m):
                schedule[j] = data[task] + i
                print(j,i)
                task = task + 1


    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    #return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    data = []

    text = input()
    text2 = []
    text2 = text.split()
    n = int(text2[0])
    m = int(text2[1])
    text = input()
    data = [int(x) for x in text.split()]


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line


if __name__ == "__main__":
    main()
