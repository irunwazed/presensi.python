#!/bin/bash

# Cek apakah folder run ada
if [ ! -d "run" ]; then
    echo "Membuat virtual environment..."
    python3 -m venv run
fi

echo "Mengaktifkan virtual environment..."
source run/bin/activate

echo "Meng-upgrade pip dan menginstall dependencies..."
pip install --upgrade pip
pip install mitmproxy netifaces

echo "Menjalankan mitmdump..."
mitmdump -s run.py
