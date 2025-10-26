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
        'sqrt': math.sqrt,
        'pi': math.pi,
        'e': math.e
    }
    try:
        # Mengevaluasi string dengan environment yang aman
        return eval(f_string, {"__builtins__": None}, safe_dict)
    except (NameError, SyntaxError) as e:
        console.print(f"[bold red]Error pada fungsi F(X): {e}. Pastikan variabelnya hanya 'x'.[/bold red]")
        return None
    except Exception as e:
        console.print(f"[bold red]Error saat mengevaluasi fungsi: {e}[/bold red]")
        return None

def secant_method(f_string, x0, x1, e, N):
    """
    Fungsi utama untuk menjalankan algoritma Metode Secant.
    """
    table_data = []
    console.print(f"\n[bold yellow]Mengevaluasi fungsi f(x) = {f_string}[/bold yellow]\n")

    # Mulai iterasi dari i = 1
    for i in range(1, N + 1):
        y0 = f(x0, f_string)
        y1 = f(x1, f_string)
        
        # Jika evaluasi fungsi gagal, hentikan program
        if y0 is None or y1 is None:
            return None, "Gagal mengevaluasi f(x). Program berhenti."

        # Cek kondisi pembagian dengan nol untuk mencegah error
        if abs(y1 - y0) < 1e-12: # Angka yang sangat kecil
            return table_data, "Pembagian dengan nol terdeteksi (y1 - y0 sangat kecil). Metode gagal."

        # Algoritma Metode Secant sesuai flowchart
        xi = x1 - y1 * (x1 - x0) / (y1 - y0)
        f_xi = f(xi, f_string)

        if f_xi is None:
            return table_data, "Gagal mengevaluasi f(xi). Program berhenti."

        abs_f_xi = abs(f_xi)

        # Simpan semua data iterasi ke dalam list untuk ditampilkan di tabel
        table_data.append([i, x0, x1, y0, y1, xi, abs_f_xi])

        # Cek kondisi berhenti: jika |F(xi)| sudah lebih kecil dari toleransi error
        if abs_f_xi < e:
            return table_data, f"Solusi ditemukan! Akar penyelesaian adalah x = {xi:.6f}"

# Update nilai untuk iterasi selanjutnya
        x0 = x1
        x1 = xi

    # Jika loop selesai tapi solusi tidak ditemukan
    return table_data, f"Metode tidak konvergen setelah {N} iterasi."

def display_ui_and_get_input():
    """
    Fungsi untuk menampilkan UI dan mengambil input dari user.
    """
# Bersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Tampilkan banner/judul program
    banner = pyfiglet.figlet_format("Kalkulator\nMetode Secant", font="slant")
    console.print(f"[bold green]{banner}[/bold green]")
    console.print(Panel.fit("[bold]Masukkan detail persamaan dan parameter yang dibutuhkan[/bold]", style="green", border_style="yellow"))

    # Ambil semua input dari user
    f_string = console.input("[cyan]  Masukkan Fungsi F(X) (cth: x**3 - x - 2 atau 4*sin(x) - exp(x)): [/cyan]")
    x0 = float(console.input("[cyan]  Masukkan tebakan awal x0: [/cyan]"))
    x1 = float(console.input("[cyan]  Masukkan tebakan awal x1: [/cyan]"))
    e = float(console.input("[cyan]  Masukkan toleransi error (e), cth: 0.0001: [/cyan]"))
    N = int(console.input("[cyan]  Masukkan maksimum iterasi (N): [/cyan]"))

    return f_string, x0, x1, e, N

def display_table(data):
    """
    Fungsi untuk menampilkan data hasil iterasi dalam bentuk tabel.
    """
    if not data:
        return

    # Buat objek tabel dengan judul dan style
    table = Table(title="[bold]Tabel Iterasi Metode Secant[/bold]", show_header=True, header_style="bold magenta")
    
    # Definisikan kolom-kolom tabel sesuai permintaan
    table.add_column("i", style="dim", width=5, justify="center")
    table.add_column("x0", justify="right")
    table.add_column("x1", justify="right")
    table.add_column("y0 = F(x0)", justify="right")
    table.add_column("y1 = F(x1)", justify="right")
    table.add_column("xi", justify="right", style="cyan")
    table.add_column("|F(xi)|", justify="right", style="green")

    # Isi tabel dengan data dari setiap baris (iterasi)
    for row in data:
            table.add_row(
            f"{row[0]}",
            f"{row[1]:.6f}", # Format angka menjadi 6 desimal
            f"{row[2]:.6f}",
            f"{row[3]:.6f}",
            f"{row[4]:.6f}",
            f"{row[5]:.6f}",
            f"{row[6]:.6f}"
        )
    
    console.print(table)

#  Program Utama 
if __name__ == "__main__":
    # 1. Tampilkan UI dan dapatkan input
    f_string, x0, x1, e, N = display_ui_and_get_input()
    
    # 2. Jalankan metode Secant dengan input yang diberikan
    data, message = secant_method(f_string, x0, x1, e, N)
    
    # 3. Jika ada data hasil iterasi, tampilkan dalam tabel
    if data:
        display_table(data)
    
    # 4. Tampilkan pesan hasil akhir (apakah solusi ditemukan atau tidak)
    console.print(Panel(Text(message, justify="center"), title="[bold]Hasil Akhir[/bold]", border_style="green", padding=(1, 2)))
