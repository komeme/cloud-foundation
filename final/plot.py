from matplotlib import pyplot as plt
from argparse import ArgumentParser
import pandas as pd


def plot(src: str):
    data = pd.read_csv(src)

    mean = data.mean(axis=0)
    std = data.std(axis=0)

    # Figureを設定
    fig = plt.figure()

    # グラフ描画領域を追加
    ax = fig.add_subplot(111)

    # Axesのタイトルを設定
    # ax.set_title("execution time for ", fontsize=16)

    # 軸範囲の設定
    ax.set_xlim(-1, 10)
    ax.set_ylim(300, 350)

    # 軸ラベルの設定
    ax.set_xlabel("trial no.", size=14, weight="light")
    ax.set_ylabel("execution time [ms]", size=14, weight="light")

    ax.bar(x=data.columns, height=mean, yerr=std, capsize=5)

    # plt.legend()
    # plt.show()


def main():
    parser = ArgumentParser()
    parser.add_argument('src')
    args = parser.parse_args()

    plot(src=args.src)


if __name__ == '__main__':
    main()
