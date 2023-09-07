from django.db import connections

# List the database names
database_names = list(connections.databases.keys())
print(database_names)