from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt


def plot(file1: str, file2: str):
    # plt.yscale('log')
    # plt.xscale('log')
    plt.xlabel('num iterations')
    plt.ylabel('time per iteration [sec]')
    plt.gca().ticklabel_format(style="sci", scilimits=(0, 0), axis="y")

    data_host = pd.read_csv(file1)
    data_guest = pd.read_csv(file2)

    # print(list(map(lambda x: int(x), data_host.columns)))
    # print(data_host)
    # print(data_host.div(list(map(lambda x: int(x), data_host.columns))))

    # print(data_host.mean(axis=0))
    # print(data_guest.mean(axis=0))

    time_per_iter_host = data_host.div(list(map(lambda x: int(x), data_host.columns)))
    time_per_iter_guest = data_guest.div(list(map(lambda x: int(x), data_guest.columns)))

    # time_per_iter_host.mean(axis=0)[1:].plot(label="host")
    # time_per_iter_guest.mean(axis=0)[1:].plot(label="guest")

    # print(data_host.std(axis=0)[1:])
    plt.errorbar(x=data_host.columns[1:], y=time_per_iter_host.mean(axis=0)[1:],
                 yerr=time_per_iter_host.std(axis=0)[1:], label='host')
    plt.errorbar(x=data_guest.columns[1:], y=time_per_iter_guest.mean(axis=0)[1:],
                 yerr=time_per_iter_guest.std(axis=0)[1:], label='guest')

    plt.legend()
    plt.show()

    # print(data_host)
    # print(data_guest)


def main():
    parser = ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('guest')
    args = parser.parse_args()

    plot(file1=args.host, file2=args.guest)


if __name__ == '__main__':
    main()
