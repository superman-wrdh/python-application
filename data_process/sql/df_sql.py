from sqlalchemy import create_engine
import pandas as pd


def engine_wsw():
    _engine = create_engine("mysql+pymysql://root:wsw@2018@47.98.146.17:8612/user_info",
                            connect_args={"charset": "utf8"})
    return _engine


def engine_hc():
    _engine = create_engine("mysql+pymysql://root:hcissuperman88@118.24.0.98:8612/user_info",
                            connect_args={"charset": "utf8"})
    return _engine


def get_date():
    sql = """
      select * from one limit 10 
    """
    df = pd.read_sql(sql, engine_wsw())
    return df


def bach_insert(df):
    df.to_sql(name='one', con=engine_hc(), if_exists='append')


if __name__ == '__main__':
    df = get_date()
    bach_insert(df)
