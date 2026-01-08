@echo off
echo ==========================================
echo  Spustanie Flask aplikacie (automaticky)
echo ==========================================
echo.

cd /d "%~dp0"

if not exist ".venv" (
    echo Vytvaram virtualne prostredie...
    py -3 -m venv .venv
)

echo Aktivujem virtualne prostredie...
call .venv\Scripts\activate

echo Aktualizujem pip...
python -m pip install --upgrade pip >nul

echo Kontrolujem potrebne balicky...
pip show flask >nul 2>&1 || pip install flask
pip show flask-wtf >nul 2>&1 || pip install flask-wtf
pip show flask-sqlalchemy >nul 2>&1 || pip install flask-sqlalchemy

echo Kontrola flasku...
where flask
echo Kontrola pythonu...
where python

echo ==========================================
echo  Spustam Flask aplikaciu...
echo ==========================================
echo.

set FLASK_APP=main
set FLASK_ENV=development

flask run --debug

echo ==== CHYBA FLASKU ALEBO UKONCENE ====
pause
