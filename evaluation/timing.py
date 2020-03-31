"""
This module is used to time the currently used network.
"""
import os

import pandas as pd
import matplotlib.pyplot as plt


# TODO: What this module is going to do: 1) It will be called by the network, when it receives the batch and when it
# TODO: finishes the batch. It will also call the network with the result. The result will be compared to the actual
# TODO: disparity of these images. Both the error and the speed will be plotted.


def batch_timing(path_csv_timing, input):
    file_exists = os.path.isfile(path_csv_timing)

    df = {'batch_time': [input[0]]}
    df = pd.DataFrame(df, columns=['batch_time'])
    if not file_exists:
        df.to_csv(path_csv_timing, index=False, header=True)
    else:
        df.to_csv(path_csv_timing, mode='a', index=False, header=False)


def time_plotter(filepath_plot, filepath_csv):
    df = pd.read_csv(filepath_csv)

    plt.plot(df.epoch, df.st0_train, 'o', color='black')

    plt.xlabel("Epoch", fontsize=16)
    plt.ylabel("Loss", fontsize=16)
    plt.title("Test and Validation Loss Training Anynet", fontsize=20)
    plt.savefig(("{}{}{}").format(filepath_plot, "/", "training_plot.png"))


if __name__ == '__main__':
    input = [1,2,3]
    batch_timing("/home/christophmartin/Documents/MA/git/AnyNet/evaluation/timing.csv", input)