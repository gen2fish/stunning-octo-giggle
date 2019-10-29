FILE=/app/db/app.db

if [ ! -f "$FILE" ]; then
  python migrate.py db init
fi

python migrate.py db migrate
python migrate.py db upgrade
ls -lart db
gunicorn -b 0.0.0.0:5000 run:app
