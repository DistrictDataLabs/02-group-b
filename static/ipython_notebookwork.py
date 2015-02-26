from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///:memory:')

pd.read_csv("mvp020715", header=None, skiprows=61,sep=r"\s+")
