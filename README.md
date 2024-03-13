docker compose up -d
docker exec -i esearch_one-postgres-1 psql -U esearch_one -d esearch_one < postgresql.sql
docker exec -i esearch_one-back-1 ./manage.py search_index --rebuild

первое задание (форум) по адресу http://localhost:8000/
второе (организации) http://localhost:8000/org/

Координаты для поиска по радиусу

широта 55.05
долгота 82.9
