from flask import request
from sqlalchemy import create_engine, text
from flask import request
import hashlib

db_string = "mysql+pymysql://6dodeptmo0rbxmzr2qms:pscale_pw_6UHZHXqyci9GtuVL38R7l7tJxmIcOihvuxtv9heGRVB@aws.connect.psdb.cloud/test_flask?charset=utf8mb4"

engine = create_engine( db_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def get_db():
  data1 = request.form
  req = data1.get('rp')
  z = hashlib.sha256(req.encode('utf-8')).hexdigest()
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM USER WHERE username = :user and upassword = :ps and urole = :ur"),
        user=data1.get('ru'),
        ps=z,
        ur=data1.get('ur')
    )
  if result.fetchall() == []:
      return False
  else:
      return True


def insert_db():
    data = request.form
    password = data.get('rp')

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with engine.connect() as conn:
      result1 = conn.execute(text("SELECT count(*) FROM USER"))
      count_result = result1.fetchone()[0]
      idn = int(count_result)+2
      id = "AFGH"+str(idn)
      conn.execute(text("INSERT INTO USER (userid, uname, username, ulocation, uphone, urole, upassword) "
               "VALUES (:id, :fn, :ru, :location, :ph, :ur, :rp)"),
          id = id,
          fn=data.get('fn'),
          ru=data.get('ru'),
          rp=hashed_password,
          location = data.get('location'),
          ph=data.get('ph'),
          ur=data.get('ur')
      );

def get_user_id(username):
  with engine.connect() as conn:
      result = conn.execute(text("SELECT userid FROM USER WHERE username = :user"), user=username)
      user_data = result.fetchone()
      if user_data:
          return user_data.userid
      else:
          return None



def convert_image_to_blob(image):
  image_bytes = image.read()
  blob = base64.b64encode(image_bytes)

  return blob