from sqlalchemy import create_engine
import sqlite3

conn = sqlite3.connect("stock.db")

disk_engine = create_engine('sqlite:///stock.db')
