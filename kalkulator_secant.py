import os
import math
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import pyfiglet

# Inisialisasi console Rich untuk UI yang lebih bagus
console = Console()

def f(x_val, f_string):
    """
    Fungsi untuk mengevaluasi ekspresi matematika dari string dengan aman.
    Fungsi ini menggantikan 'x' dalam string dengan nilai numeriknya.
    """
    # Dictionary aman untuk fungsi matematika yang diizinkan
    safe_dict = {
        'x': x_val,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log,
        'log10': math.log10,
