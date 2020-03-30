"""This module is the timing class. Its used to assess the speed of the different pipelines and stores and plots it.

Inputs: data paths to plot / store csv file of the data, batch size, total time and time for processing and loading the
data.
Output: 1 csv file, containing the data. 1 png image, containing the plotted data.
"""
import os

import pandas as pd
import matplotlib.pyplot as plt


class Timing:

    def __init__(self, processing_time, dataloading_time, batch_size, path_plot, path_csv, abs_time):
        # TODO: We need: Dataloading time, processing time, path to store plots + .csv... well see, more to come
        self.processing_time = processing_time
        self.dataloading_time = dataloading_time
        self.batch_size = batch_size
        self.path_plot = path_plot
        self.path_csv = path_csv
        self.abs_time = abs_time

    def write_time(self):
        file_exists = os.path.isfile(self.path_csv)

        df = {'process_time': [self.processing_time], 'loading_time': [self.dataloading_time],
              'batch_size': [self.batch_size], 'total_time': [self.abs_time]}
        df = pd.DataFrame(df, columns=['process_time', 'loading_time', 'batch_size', 'total_time'])
        if not file_exists:
            df.to_csv(self.path_csv, index=False, header=True)
        else:
            df.to_csv(self.path_csv, mode='a', index=False, header=False)

    def plot_time(self):
        df = pd.read_csv(self.path_csv)

        plt.plot(df.total_time, df.process_time, 'o', color='black', label="Processing Time")
        plt.plot(df.total_time, df.loading_time, 'x', color='red', label="Loading Time")

        plt.xlabel("Total time", fontsize=16)
        plt.ylabel("Time [s]", fontsize=16)
        plt.title("Loading and processing time [per Batch] Anynet", fontsize=18)

        # to avoid duplicate legends
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(), loc='upper right')
        plt.savefig(("{}{}{}").format(self.path_plot, "/", "timing_plot.png"))



