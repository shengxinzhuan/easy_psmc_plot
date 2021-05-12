# easy_psmc_plot

* this script is aim to plot the PSMC result by an easy way
* To use this script, "click" and "matplotlib" are required in the path
* Usage: python easy_psmc_plot.py --psmc_file_list sample.list

# input format(sample name , color and label which seperate by tab)
* sample_1.diploid.psmc	#e9c46a label1
* sample_2.diploid.psmc	#ff7c7c label2


# command line
```
python easy_psmc_plot.py --help
Usage: easy_psmc_plot.py [OPTIONS]

Options:
  --psmc_file_list TEXT      a list with all samples name and line color,
                             seperate by        (This parameter are required!)

  --bin_size INTEGER         Bin size used to generate the imput of PSMC
                             (default: 100)

  --mutation_rate FLOAT      Mutation rate per generation(Default: 4.78e-9)
  --generation_time INTEGER  Number of year per generation(Default: 20)
  --x_min FLOAT              Size of the plot xlim lower(Default: 1e4)
  --x_max FLOAT              Size of the plot xlim upper(Default: 1e8)
  --y_min FLOAT              Size of the plot ylim lower(Default: 0)
  --y_max FLOAT              Size of the plot ylim upper(Default: 30e4)
  --line_width FLOAT         The line width(Default: 2.0)
  --length FLOAT             Length of the plot(Default:10)
  --height FLOAT             Height of the plot(Default:5)
  --picture_dpi INTEGER      Output picture dpi(Default:300)
  --span_min FLOAT           the span of xlim selection region's min
                             value(Default:None)

  --span_max FLOAT           the span of xlim selection region's max
                             value(Default:None)

  --span_color TEXT          the span color(Default:purple)
  --span_alpha FLOAT         the span clolor transparency(Default:0.3)
  --help                     Show this message and exit.

```
# example 
```
 python easy_psmc_plot.py --psmc_file_list sample_list.txt --mutation_rate 7.8e-9 --generation_time 6 --x_max 7e4 --y_max 0.5e4 --x_min 1e3 --span_min 1.5e3 --span_max 1.9e3 --span_color yellow
```
# example result
![](https://github.com/shengxinzhuan/easy_psmc_plot/blob/main/example_result.png)
