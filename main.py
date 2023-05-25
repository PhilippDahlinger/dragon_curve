import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

from dragon_curve_gen import dragon_next_iteration, first_iteration, terdragon_next_iteration
from rendering import print_curve, plot_curve


def plot_4_curves(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, color="blue", start_dir=0)
    plot_curve(ax, d, color="red", start_dir=1)
    plot_curve(ax, d, color="green", start_dir=2)
    plot_curve(ax, d, color="purple", start_dir=3)
    # plot_curve(ax, d, color="all", start_dir=0)
    # plot_curve(ax, d, color="all", start_dir=1)
    # plot_curve(ax, d, color="all", start_dir=2)
    # plot_curve(ax, d, color="all", start_dir=3)
    plt.show()
    plt.close()


def plot_single_curve(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, color="all", start_dir=1)
    plt.show()
    plt.close()

def animate_single_curve(d):
    plt.ion()
    plt.cla()
    plot_curve(plt.gca(), d, color="all", start_dir=1)
    plt.pause(1.0)



def triangular_curve(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, angle_divisor=3, color="all", start_dir=1)
    plt.show()
    plt.close()

def hexagonal_curve(d):
    fig, ax = plt.subplots()
    plot_curve(ax, d, angle_divisor=6, color="all", start_dir=1)
    plt.show()
    plt.close()

if __name__ == '__main__':

    # next_iteration = terdragon_next_iteration
    next_iteration = dragon_next_iteration


    dragon_curves = [first_iteration()]
    for i in range(20):
        dragon_curves.append(next_iteration(dragon_curves[-1]))
        d = dragon_curves[-1]
        # print_curve(d)

        plot_single_curve(d)
        # plot_4_curves(d)
        # animate_single_curve(d)
        # triangular_curve(d)
        # hexagonal_curve(d)




