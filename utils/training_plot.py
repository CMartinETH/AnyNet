""" This module is used to plot the training loss and validation loss after every epoch and store it in a file.

It stores a csv file with epoch, train losses from all stages, validation losses from all stages. It also plots these
values after every finished epoch / after the validation step.
"""
import os

import pandas as pd
import matplotlib.pyplot as plt


def csv_writer_plotter(path_csv_train, filepath_plot, input_row, epoch, train=True):
    file_exists = os.path.isfile(path_csv_train)
    if train:
        if not file_exists:
            df = {'st0_train': [input_row[0]], 'st1_train': [input_row[1]], 'st2_train': [input_row[2]],
                  "st3_train": [input_row[3]], "epoch": [epoch]}
            df = pd.DataFrame(df, columns=['st0_train', 'st1_train', 'st2_train', "st3_train", "st0_val", "st1_val",
                                                                                        "st2_val", "st3_val", "epoch"])
            df.to_csv(path_csv_train, index=False, header=True)

        if file_exists:
            df2 = {'st0_train': [input_row[0]], 'st1_train': [input_row[1]], 'st2_train': [input_row[2]],
                  "st3_train": [input_row[3]], "epoch": [epoch]}
            df2 = pd.DataFrame(df2, columns=['st0_train', 'st1_train', 'st2_train', "st3_train", "st0_val", "st1_val",
                                           "st2_val", "st3_val", "epoch"])
            df2.to_csv(path_csv_train, mode='a', index=False, header=False)

    else:

        df = pd.read_csv(path_csv_train)
        last_val = len(df.st0_val)
        df.loc[(last_val-1), 'st0_val'] = input_row[0]
        df.loc[(last_val-1), 'st1_val'] = input_row[1]
        df.loc[(last_val-1), 'st2_val'] = input_row[2]
        df.loc[(last_val-1), 'st3_val'] = input_row[3]
        df.to_csv(path_csv_train, index=False)

        loss_plotter(filepath_plot, path_csv_train)


def loss_plotter(filepath_plot, filepath_csv):
    df = pd.read_csv(filepath_csv)

    plt.plot(df.epoch, df.st0_train, 'o', color='black')
    plt.plot(df.epoch, df.st1_train, 'o', color='red')
    plt.plot(df.epoch, df.st2_train, 'o', color='blue')
    plt.plot(df.epoch, df.st3_train, 'o', color='green')

    plt.plot(df.epoch, df.st0_val, 'x', color='black')
    plt.plot(df.epoch, df.st1_val, 'x', color='red')
    plt.plot(df.epoch, df.st2_val, 'x', color='blue')
    plt.plot(df.epoch, df.st3_val, 'x', color='green')

    plt.xlabel("Epoch", fontsize=16)
    plt.ylabel("Loss", fontsize=16)
    plt.title("Test and Validation Loss Training Anynet", fontsize=20)
    plt.savefig(("{}{}{}").format(filepath_plot, "/", "training_plot.png"))
