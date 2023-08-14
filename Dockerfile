FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ['alembic', 'revision', '--autogenerate', '-m', '"Your migration message here"']

# CMD ["alembic","upgrade","head"]

# CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

ENTRYPOINT ["bash","start.sh"]



