import pandas as pd
from IPython.display import display


# line_chart_convert - Convert data to json of line chart
def line_chart_convert(df_p, plot_parm):

    # Rename data column to x, y
    df_p = df_p.rename(columns={ plot_parm['x']: 'x', plot_parm['y']: 'y' })

    # Group data by columns and turn the data to suitable format
    datasets = []

    for sub, df_p_sub in df_p.groupby(plot_parm['group_by']):

        data_dict = {
            'values': df_p_sub[['x', 'y']].to_dict('records'),
            'label': sub
        }

        datasets.append(data_dict)

    result = {
        'dataSets': datasets
    }

    return result


# bar_chart_convert - Convert data to json of bar chart
def bar_chart_convert(df_p, plot_parm):

    # Rename data column to x, y
    df_p = df_p.rename(columns={ plot_parm['x']: 'x', plot_parm['y']: 'y' })

    # Turn the data to suitable format
    result = {
        'dataSets': [{
            'values': df_p[['y']].to_dict('records'),
            'label': 'TML'
        }],
        'xAxis': {
            'valueFormatter': df_p['x'].tolist()
        }
    }

    return result


# stacked_bar_chart_convert - Convert data to json of stacked bar chart
def stacked_bar_chart_convert(df_p, plot_parm):

    # Rename data column to x, y
    df_p = df_p.rename(columns={ plot_parm['x']: 'x', plot_parm['y']: 'y' })

    # Group data by columns and turn the data to suitable format
    datasets = []
    stacklabels = []

    for sub, df_p_sub in df_p.groupby(plot_parm['group_by']):
        
        data_dict = {
            'y': df_p_sub['y'].to_list(),
        }

        datasets.append(data_dict)
        stacklabels.append(sub)

    x_axis = df_p.groupby('x').agg({'y': 'first'}).reset_index()

    result = {
        'dataSets': [{
            'values': datasets,
            'label': 'Sub Category',
            'config': {
                'stackLabels': stacklabels
            }
        }],
        'xAxis': {
            'valueFormatter': x_axis['x'].tolist()
        }
    }

    return result


# scatter_chart_convert - Convert data to json of scatter chart
def scatter_chart_convert(df_p, plot_parm):

    # Rename data column to x, y
    df_p = df_p.rename(columns={ plot_parm['x']: 'x', plot_parm['y']: 'y' })

    # Group data by columns and turn the data to suitable format
    datasets = []

    for sub, df_p_sub in df_p.groupby(plot_parm['group_by']):

        data_dict = {
            'values': df_p_sub[['x', 'y']].to_dict('records'),
            'label': sub
        }

        datasets.append(data_dict)

    result = {
        'dataSets': datasets
    }

    return result