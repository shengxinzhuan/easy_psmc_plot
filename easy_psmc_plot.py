import click
import matplotlib.pyplot as plt

#====================================================================================================================
# Author: Alfred Hou
# E-mail: 825526231@qq.com
# Any question can send the e-mail to me
# Time: 2020/11/17
#====================================================================================================================
#====================================================================================================================
# This script is aim to plot the PSMC result by an easy way.
# To use this script, "click" and "matplotlib" are required in the path
# Usage: python easy_psmc_plot.py --psmc_file_list sample.list
#====================================================================================================================

#====================================================================================================================
# command paramter
#====================================================================================================================
@click.command()
@click.option("--psmc_file_list", prompt=False, help = "a list with all samples name and line color, seperate by \t(This parameter are required!)")
@click.option("--bin_size", default=100, help="Bin size used to generate the imput of PSMC (default: 100)")
@click.option("--mutation_rate", default=4.78e-9, help="Mutation rate per generation(Default: 4.78e-9)")
@click.option("--generation_time", default=20, help="Number of year per generation(Default: 20)")
@click.option("--x_min", default=1e4, type = float, help="Size of the plot xlim lower(Default: 1e4)")
@click.option("--x_max", default=1e8, type = float, help="Size of the plot xlim upper(Default: 1e8)")
@click.option("--y_min", default=0, type = float, help="Size of the plot ylim lower(Default: 0)")
@click.option("--y_max", default=30e4, type = float, help="Size of the plot ylim upper(Default: 30e4)")
@click.option("--line_width", default=2.0, type = float, help= "The line width(Default: 2.0)")
@click.option("--length", default=10, type = float, help="Length of the plot(Default:10)")
@click.option("--height", default=5, type = float, help="Height of the plot(Default:5)")
@click.option("--picture_dpi", default=300, type= int, help="Output picture dpi(Default:300)")
#====================================================================================================================
# Plot function
#====================================================================================================================
def plot_func(psmc_file_list, bin_size, mutation_rate, generation_time, x_min, x_max, y_min, y_max, line_width, length, height, picture_dpi):
    # Read file list
    psmc_file = open(psmc_file_list, "r")

    # Plot psmc result
    fig = plt.figure(figsize = (length,height))
    plt.style.use("classic")
    ax = fig.add_subplot(111)
    for i in psmc_file:
        i = i.rstrip()
        PSMC_RESULT = str(i.split("\t")[0])
        line_color = str(i.split("\t")[1])
        (estimated_times, estimated_sizes) = psmc_fun(PSMC_RESULT, bin_size, mutation_rate, generation_time)
        ax.step(estimated_times, estimated_sizes, where = 'post', linestyle = "-", color = line_color, linewidth = line_width)

    ax.set_xlabel("Time in years (g = 20, μ = 4.78 x 10^-9)")
    ax.set_ylabel("Effective size (x 10^4)")
    ax.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
    ax.grid(False)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    plt.legend(loc = "best")
    ax.set_xscale('log')
    plt.savefig("psmc.plot.pdf", dpi = picture_dpi)

#====================================================================================================================
# Set up the function to psmc result
#====================================================================================================================
def psmc_fun(filename, size, mutation, generation_time):
    
    # Read the raw file
    psmc_rlt = open(filename, "r")
    result = psmc_rlt.read()
    psmc_rlt.close()
    
    
    # Getting the time windows and the lambda values
    last_block = result.split('//\n')[-2]
    last_block = last_block.split('\n')
    time_windows = []
    estimated_lambdas = []
    for line in last_block:
        if line[:2] =="RS":
            time_windows.append(float(line.split('\t')[2]))
            estimated_lambdas.append(float(line.split('\t')[3]))
            
            
    # Getting the estimations of theta for computing N0
    result = result.split('PA\t') # The 'PA' lines contain the values of the estimated parameters
    
    result = result[-1].split('\n')[0]
    result = result.split(' ')
    theta = float(result[1])
    N0 = theta/(4*mutation)/size
    
    # Scalling times and sizes
    times = [generation_time * 2 * N0 * i for i in time_windows]
    sizes = [N0 * i for i in estimated_lambdas]
    
    # Remove the false positive result
    raw_dict = {}
    false_result = sizes[-1]

    for i in range(len(sizes)):
        raw_dict[times[i]] = sizes[i]
    
    times = []
    sizes = []

    for k, v in raw_dict.items():
        if str(v) != str(false_result):
            times.append(k)
            sizes.append(v)
        else:
            break
    
    return(times, sizes)


#======================================================================================================================
# Main function
#======================================================================================================================

if __name__ == '__main__':
    
    plot_func()