import requests
import tkinter as tk
from datetime import datetime
import threading
import time

import ntplib
from time import ctime

def get_ntp_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        return ctime(response.tx_time)
    except Exception as e:
        return f"Error: {e}"



def update_clock():
    while True:
        current_time = get_ntp_time()
        label.config(text=current_time)
        time.sleep(1)

# --- GUI ---
root = tk.Tk()
root.title("Jam Atom UTC")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Mengambil waktu...", font=("Helvetica", 24))
label.pack(expand=True)

# Jalankan update di thread terpisah agar GUI tidak freeze
thread = threading.Thread(target=update_clock, daemon=True)
thread.start()

root.mainloop()

# harus install : pip install ntplib
