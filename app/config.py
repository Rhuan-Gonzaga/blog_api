import os

class Config:
    #Banco subindo no XAMP
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/blog_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False