from sqlalchemy import create_engine
import pandas as pd

table = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']


def engine_base():
    _engine = create_engine("",
                            connect_args={"charset": "utf8"})
    return _engine


def query_by_name(name, tb="one"):
    print('start')
    sql = """
      select * from {tb} where `Name` like '%%{name}%%'
    """.format(tb=tb, name=name)
    return pd.read_sql(sql, engine_base())


def get_by_id(id, tb="one"):
    sql = """
        select * from {tb} where id='{id}'
    """.format(tb=tb, id=id)
    df = pd.read_sql(sql, engine_base())
    df = df.fillna('-')
    if not df.empty:
        return df.to_dict(orient='records')[0]
    else:
        return {}


if __name__ == '__main__':
    name = get_by_id(id='39184')
    pass
