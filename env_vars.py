import os

db_user = os.environ.get('DB_User')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)