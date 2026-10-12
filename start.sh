#!/usr/bin/env bash
# Startet die Netzwerk-Speed-App auf Linux.
#
# Die virtuelle Umgebung liegt NICHT im Projektordner, weil das NAS keine
# Symlinks mag. Darum zeigt dieses Skript auf den Ordner im Home.
VENV="/home/theo/.venvs/netzwerk-speed"
cd "$(dirname "$0")" || exit 1

if [ ! -x "$VENV/bin/flet" ]; then
  echo "Flet nicht gefunden. Einmalig einrichten:"
  echo "  python3 -m venv --copies $VENV"
  echo "  $VENV/bin/pip install flet"
  exit 1
fi

exec "$VENV/bin/flet" run app.py
