define([
    'base/js/namespace'
], function(Jupyter) {
    function load_ipython_extension() {
        if (Jupyter.notebook.get_cells().length === 1) {
            Jupyter.notebook.insert_cell_above('code', 0).set_text(`import numpy as np
from scipy import signal, interpolate
import pandas as pd
import matplotlib.pyplot as plt
import os, sys, glob
import tables

%load_ext autoreload
%autoreload 2`);
            Jupyter.notebook.insert_cell_above('code', 1).set_text("%matplotlib notebook")
        }
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
