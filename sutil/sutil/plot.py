import matplotlib.pyplot as plt

def plot(x, y, ns, **kwargs):
    """One function to rule them all, and in the darkness, bind them"""
    if isinstance(x, str):
        x = [x]
    if isinstance(y, str):
        y = [y]
    
    def data_lookup(arr):
        arr_data = []
        arr_label = []
        for a_ in arr:
            if isinstance(a_, str):
                arr_label.append(a_)
                arr_data.append(ns[a_])
            else:
                arr_data.append(a_)
                arr_label.append('')
                
        return arr_label, arr_data

    xlabel, xdata = data_lookup(x)
    ylabel, ydata = data_lookup(y)
    
    if len(x) == 1:
        N = len(y)
        fig, axes = plt.subplots(N, 1, sharex=True)
        for k in range(N):
            axes[k].plot(xdata[0], ydata[k], **kwargs)
            axes[k].set_ylabel(ylabel[k])
        axes[-1].set_xlabel(xlabel[0])
    elif len(y) == 1:
        N = len(x)
        fig, axes = plt.subplots(1, N, sharey=True)
        for k in range(N):
            axes[k].plot(xdata[k], ydata[0], **kwargs)
            axes[k].set_xlabel(xlabel[k])
        axes[0].set_ylabel(ylabel[0])
    return fig, axes
