# Rechen-Logik und Einheiten. Hier kann man Werte/Schreibweisen anpassen.

# ---------------------------------------------------------------
# Overhead: Wie viel von der "Brutto"-Geschwindigkeit real ankommt.
# Ethernet verliert rund 6 % durch Protokoll-Overhead -> 94 % nutzbar.
# Nur diese eine Zahl aendern, wenn du es anders haben willst.
# ---------------------------------------------------------------
EFF = 0.94

# Jede Einheit hat:
#   key          = interner Name (nicht aendern)
#   faktor       = Wert in bit/s, wenn man 1 davon nimmt (Byte = x8)
#   kurz         = Anzeigename
#   schreibweisen= die gaengigen Schreibweisen (werden im Rechner gezeigt)
#   art          = "bit" oder "byte"
#   hilfe        = welcher Lexikon-Eintrag an der Gluehbirne haengt
EINHEITEN = [
    {"key": "bit",   "faktor": 1.0,  "kurz": "bit/s",   "art": "bit",
     "schreibweisen": ["bit/s", "bps"], "hilfe": "bit"},
    {"key": "kbit",  "faktor": 1e3,  "kurz": "kbit/s",  "art": "bit",
     "schreibweisen": ["kbit/s", "kbps"], "hilfe": "kbit"},
    {"key": "mbit",  "faktor": 1e6,  "kurz": "Mbit/s",  "art": "bit",
     "schreibweisen": ["Mbit/s", "Mbps", "Mbit"], "hilfe": "mbit"},
    {"key": "gbit",  "faktor": 1e9,  "kurz": "Gbit/s",  "art": "bit",
     "schreibweisen": ["Gbit/s", "Gbps", "Gbit"], "hilfe": "gbit"},
    {"key": "byte",  "faktor": 8.0,  "kurz": "B/s",     "art": "byte",
     "schreibweisen": ["B/s"], "hilfe": "byte"},
    {"key": "kbyte", "faktor": 8e3,  "kurz": "kB/s",    "art": "byte",
     "schreibweisen": ["kB/s", "kBps"], "hilfe": "kbyte"},
    {"key": "mbyte", "faktor": 8e6,  "kurz": "MB/s",    "art": "byte",
     "schreibweisen": ["MB/s", "MBps", "MByte/s"], "hilfe": "mbyte"},
    {"key": "gbyte", "faktor": 8e9,  "kurz": "GB/s",    "art": "byte",
     "schreibweisen": ["GB/s", "GBps"], "hilfe": "gbyte"},
]

_EINHEIT_MAP = {e["key"]: e for e in EINHEITEN}

# Reihenfolge, in der die Ergebnisse angezeigt werden
ANZEIGE_REIHENFOLGE = ["gbit", "mbit", "kbit", "bit", "gbyte", "mbyte", "kbyte", "byte"]


def finde(key):
    """Gibt die Einheiten-Definition zu einem key zurueck."""
    return _EINHEIT_MAP[key]


def parse_zahl(text):
    """Macht aus einer Eingabe eine Zahl. Akzeptiert Komma UND Punkt.
    Gibt None zurueck, wenn es keine Zahl ist."""
    if text is None:
        return None
    text = str(text).strip().replace(" ", "")
    if text == "":
        return None
    text = text.replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


def umrechnen(wert, key):
    """Rechnet wert (in Einheit key) in ALLE Einheiten um.
    Gibt ein dict zurueck: key -> Zahl in dieser Einheit."""
    faktor = _EINHEIT_MAP[key]["faktor"]
    bps = wert * faktor          # immer erst alles in bit/s
    ergebnis = {}
    for e in EINHEITEN:
        ergebnis[e["key"]] = bps / e["faktor"]
    return ergebnis


def _fmt_zahl(n, d):
    """Deutsche Zahl: Punkt als Tausender, Komma als Dezimaltrenner."""
    s = f"{n:,.{d}f}"
    s = s.replace(",", "\u0000")   # Tausender-Trenner parken
    s = s.replace(".", ",")        # Dezimalpunkt -> Komma
    s = s.replace("\u0000", ".")   # Tausender-Trenner zurueck als Punkt
    return s


def fmt(n, d=None):
    """Formatiert eine Zahl lesbar. d = feste Nachkommastellen (optional)."""
    if d is None:
        a = abs(n)
        if a >= 1000:
            d = 0
        elif a >= 100:
            d = 1
        elif a >= 1:
            d = 2
        elif a >= 0.01:
            d = 3
        else:
            d = 5
    return _fmt_zahl(n, d)


def best_bit(bps):
    """bit/s in die schoenste Bit-Einheit bringen."""
    for faktor, name in [(1e9, "Gbit/s"), (1e6, "Mbit/s"), (1e3, "kbit/s"), (1, "bit/s")]:
        if bps >= faktor:
            return f"{fmt(bps / faktor)} {name}"
    return f"{fmt(bps)} bit/s"


def best_byte(Bps):
    """Byte/s in die schoenste Byte-Einheit bringen."""
    for faktor, name in [(1e9, "GB/s"), (1e6, "MB/s"), (1e3, "kB/s"), (1, "B/s")]:
        if Bps >= faktor:
            return f"{fmt(Bps / faktor)} {name}"
    return f"{fmt(Bps)} B/s"
