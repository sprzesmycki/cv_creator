alembic upgrade head -> applies migrations
alembic revision --autogenerate -m "name for revision" -> detects new changes and creates migration


alembic stamp head -> indicates that the current state of the db represents the application of all migrations