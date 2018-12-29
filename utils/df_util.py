import sys
import re


class DataFrameHelper:
    @staticmethod
    def to_dict(dataframe, usage='graphic', **kwargs):
        """
        DataFrame 封装成便于 前端直接操作的格式
        :param df:
        :param usage:
        :param kwargs:
        :return:
        """
        data = []
        if usage == 'graphic':
            values_key = kwargs.get('values_key', 'series')
            category_key = kwargs.get('category_key', 'categories')
            for col in dataframe.columns:
                col_data = {'name': col, 'data': dataframe[col].tolist()}
                data.append(col_data)
            return {values_key: data, category_key: dataframe.index.tolist()}
        elif usage == 'table':
            rename_columns = kwargs.get('rename_columns', dataframe.columns.tolist())
            index_name = kwargs.get('index_name', 'row_name')
            dataframe[index_name] = dataframe.index
            column_dict = dict(zip(rename_columns + ['row_name'], dataframe.columns.tolist()))
            dataframe.rename(columns=dict(zip(dataframe.columns.tolist(), rename_columns + ['row_name'])), inplace=True)
            return {'data': dataframe.to_dict(orient='records'), 'columns': column_dict}

    @staticmethod
    def to_sql(tb_name, conn, dataframe, type="update", chunksize=2000):
        """
        Dummy of pandas.to_sql, support "REPLACE INTO ..." and "INSERT ... ON DUPLICATE KEY UPDATE (keys) VALUES (values)"
        SQL statement.

        Args:
            tb_name: str
                Table to insert get_data;
            conn:
                DBAPI Instance
            dataframe: pandas.DataFrame
                Dataframe instance
            type: str, optional {"update", "replace", "ignore"}, default "update"
                Specified the way to update get_data. If "update", then `conn` will execute "INSERT ... ON DUPLICATE UPDATE ..."
                SQL statement, else if "replace" chosen, then "REPLACE ..." SQL statement will be executed; else if "ignore" chosen,
                then "INSERT IGNORE ..." will be excuted;
            chunksize: int
                Size of records to be inserted each time;
            **kwargs:

        Returns:
            None
        """

        df = dataframe.copy()
        df = df.fillna("None")
        df = df.applymap(lambda x: re.sub('([\'\"\\\])', '\\\\\g<1>', str(x)))
        cols_str = sql_cols(df)
        for i in range(0, len(df), chunksize):
            # print("chunk-{no}, size-{size}".format(no=str(i/chunksize), size=chunksize))
            df_tmp = df[i: i + chunksize]
            if type == "replace":
                sql_base = "REPLACE INTO `{tb_name}` {cols}".format(
                    tb_name=tb_name,
                    cols=cols_str
                )
                sql_val = sql_cols(df_tmp, "format")
                vals = tuple([sql_val % x for x in df_tmp.to_dict("records")])
                sql_vals = "VALUES ({x})".format(x=vals[0])
                for i in range(1, len(vals)):
                    sql_vals += ", ({x})".format(x=vals[i])
                sql_vals = sql_vals.replace("'None'", "NULL")

                sql_main = sql_base + sql_vals

            elif type == "update":
                sql_base = "INSERT INTO `{tb_name}` {cols}".format(
                    tb_name=tb_name,
                    cols=cols_str
                )
                sql_val = sql_cols(df_tmp, "format")
                vals = tuple([sql_val % x for x in df_tmp.to_dict("records")])
                sql_vals = "VALUES ({x})".format(x=vals[0])
                for i in range(1, len(vals)):
                    sql_vals += ", ({x})".format(x=vals[i])
                sql_vals = sql_vals.replace("'None'", "NULL")

                sql_update = "ON DUPLICATE KEY UPDATE {0}".format(
                    sql_cols(df_tmp, "values")
                )

                sql_main = sql_base + sql_vals + sql_update

            elif type == "ignore":
                sql_base = "INSERT IGNORE INTO `{tb_name}` {cols}".format(
                    tb_name=tb_name,
                    cols=cols_str
                )
                sql_val = sql_cols(df_tmp, "format")
                vals = tuple([sql_val % x for x in df_tmp.to_dict("records")])
                sql_vals = "VALUES ({x})".format(x=vals[0])
                for i in range(1, len(vals)):
                    sql_vals += ", ({x})".format(x=vals[i])
                sql_vals = sql_vals.replace("'None'", "NULL")

                sql_main = sql_base + sql_vals

            if sys.version_info.major == 2:
                sql_main = sql_main.replace("u`", "`")
            sql_main = sql_main.replace("%", "%%")
            conn.execute(sql_main)


def sql_cols(df, usage="sql"):
    cols = tuple(df.columns)
    if usage == "sql":
        cols_str = str(cols).replace("'", "`")
        if len(df.columns) == 1:
            cols_str = cols_str[:-2] + ")"  # to process dataframe with only one column
        return cols_str
    elif usage == "format":
        base = "'%%(%s)s'" % cols[0]
        for col in cols[1:]:
            base += ", '%%(%s)s'" % col
        return base
    elif usage == "values":
        base = "%s=VALUES(%s)" % (cols[0], cols[0])
        for col in cols[1:]:
            base += ", `%s`=VALUES(`%s`)" % (col, col)
        return base


if __name__ == '__main__':
    import pandas as pd

    df = pd.DataFrame(data={"年化收益率": ["1", "2", "3", "4"],
                            "累计收益": ["1", "3", "2", "1"]}, index=["今年以来", "近六月", "近三月", "近一年"])
    d = DataFrameHelper.to_dict(df, usage='table')
    pass
