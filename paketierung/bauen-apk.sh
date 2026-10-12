#!/bin/bash
# Netzwerk-Speed als Android-APK bauen (arm64-v8a, fuer moderne Handys / Android 16).
#
# Einmalige Voraussetzungen:
#   - Temurin JDK 17 unter /home/theo/java/17.0.13+11 (flet verlangt JDK 17)
#   - Android SDK unter /home/theo/Android/Sdk mit:
#       platform-tools  platforms;android-35  build-tools;34.0.0
#       platforms;android-36  build-tools;36.0.0
#   - flet im venv /home/theo/.venvs/netzwerk-speed
#
# WICHTIG: Es wird aus einem SAUBEREN Quellordner gebaut. Liegt im
# App-Verzeichnis noch ein flatpak-app/ (Rootfs-Spiegel), haengt flet beim
# Schritt "Packaging Python app" (find_default_excludes folgt Symlinks).
#
# Ergebnis: <Buildordner>/build/apk/netzwerkspeed.apk  ->  Pakete/Netzwerk-Speed-0.1.0-arm64.apk

set -euo pipefail

QUELLE="/home/theo/NAS-Lager/Workspace_Migration/Coding/Kleine Tools/Netzwerk-Speed"
BUILD="/home/theo/netzwerk-speed-apk"
VENV="/home/theo/.venvs/netzwerk-speed/bin/flet"
export JAVA_HOME="/home/theo/java/17.0.13+11"
export ANDROID_HOME="/home/theo/Android/Sdk"

echo "==> 1/3 Sauberen Quellordner vorbereiten ($BUILD)"
rm -rf "$BUILD"
mkdir -p "$BUILD"
cp -r "$QUELLE/app.py" "$QUELLE/pyproject.toml" "$QUELLE/requirements.txt" "$QUELLE/LICENSE" "$BUILD/"
cp -r "$QUELLE/daten" "$BUILD/daten"
cp -r "$QUELLE/assets" "$BUILD/assets"
find "$BUILD" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null || true

echo "==> 2/3 APK bauen (flet build apk, arm64-v8a)"
(
  cd "$BUILD"
  "$VENV" build apk . --module-name app --yes --arch arm64-v8a \
    --android-adaptive-icon-background "#101716"
)

echo "==> 3/3 Nach Kopie auf das NAS"
mkdir -p "$QUELLE/Pakete"
cp "$BUILD/build/apk/netzwerkspeed.apk" "$QUELLE/Pakete/Netzwerk-Speed-0.1.0-arm64.apk"

echo "==> FERTIG:"
ls -la "$QUELLE/Pakete/Netzwerk-Speed-0.1.0-arm64.apk"
echo "Installieren: APK aufs Handy kopieren und oeffnen (Unbekannte Quellen erlauben)."
