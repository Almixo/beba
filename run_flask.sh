#!/bin/bash

echo "=========================================="
echo " Spustanie Flask aplikacie (automaticky)"
echo "=========================================="
echo

# Change to script directory
cd "$(dirname "$0")"

# Check/create virtual environment
if [ ! -d ".venv" ]; then
    echo "Vytvaram virtualne prostredie..."
    python3 -m venv .venv
fi

echo "Aktivujem virtualne prostredie..."
source .venv/bin/activate

echo "Aktualizujem pip..."
python -m pip install --upgrade pip > /dev/null 2>&1

echo "Kontrolujem potrebne balicky..."
python -c "import flask" 2>/dev/null || pip install flask
python -c "from flask_wtf import FlaskForm" 2>/dev/null || pip install flask-wtf
python -c "from flask_sqlalchemy import SQLAlchemy" 2>/dev/null || pip install flask-sqlalchemy

echo "Kontrola flasku..."
which flask
echo "Kontrola pythonu..."
which python

echo "=========================================="
echo " Spustam Flask aplikaciu..."
echo "=========================================="
echo

export FLASK_APP=main
export FLASK_ENV=development

flask run --debug --host=0.0.0.0 --port=5000

echo "==== CHYBA FLASKU ALEBO UKONCENE ===="
read -p "Stlac enter pre pokracovanie..."