import time
from argparse import ArgumentParser
import csv

NUM_SAMPLES = 10
SAMPLE_ITERATIONS = [10 ** i for i in range(8)]
SAMPLE_ITERATIONS_IO = [10 ** i for i in range(5)]
FILE_NAME = 'hoge.txt'


def increment(n: int):
    v = 0
    for _ in range(n):
        v += 1
    return v




def write_file(n: int):
    v = 0
    for i in range(n):
        with open(FILE_NAME, 'w') as f:
            v += 1
            f.write(str(v))
    return


def with_measure(func):
    # 時間計測開始
    time_sta = time.perf_counter()
    # 処理
    result = func()
    # 時間計測終了
    time_end = time.perf_counter()
    # 経過時間（秒）
    tim = time_end - time_sta
    return result, tim


def measure_without_io(out: str, num_sample: int):
    print('WITHOUT IO')
    data = []
    for _ in range(num_sample):
        results = []
        for n in SAMPLE_ITERATIONS:
            res, tim = with_measure(lambda: increment(n))
            # res, tim = with_measure(lambda: write_file(n))
            results.append(tim)

        data.append(results)

    with open(out, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(SAMPLE_ITERATIONS)
        writer.writerows(data)


def measure_with_io(out: str, num_sample: int):
    print('WITH IO')

    data = []
    for _ in range(num_sample):
        results = []
        for n in SAMPLE_ITERATIONS_IO:
            # res, tim = with_measure(lambda: increment(n))
            res, tim = with_measure(lambda: write_file(n))
            results.append(tim)

        data.append(results)

    with open(out, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(SAMPLE_ITERATIONS)
        writer.writerows(data)


def main():
    parser = ArgumentParser()
    parser.add_argument('out')
    parser.add_argument('--io', default=False)
    args = parser.parse_args()

    if args.io:
        measure_with_io(out=args.out, num_sample=NUM_SAMPLES)
    else:
        measure_without_io(out=args.out, num_sample=NUM_SAMPLES)


if __name__ == '__main__':
    main()
