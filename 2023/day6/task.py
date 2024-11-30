
time = [48,93,84,66]
Distance=[261,1192,1019,1063]

if __name__ == '__main__':
    results = 1
    for i, record in zip(time, Distance):
        dist = []
        for sec in range(i):
            remain = i - sec
            dist.append(sec * remain)
        results *= sum([d > record for d in dist])
    print("task 1", results)

    results = 1
    i = 48938466
    record = 261119210191063
    for sec in range(i):
        remain = i - sec
        dist.append(sec * remain)
    results *= sum([d > record for d in dist])
    print("task 2", results)