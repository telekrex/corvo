cd source
python -m PyInstaller Corvo.py -n Corvo --clean --noupx --noconfirm --onedir --add-data "domains.txt;_internal/domains.txt"