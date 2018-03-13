# -*- encoding: utf-8 -*-
import sqlalchemy.ext.declarative


engine = sqlalchemy.create_engine("mysql+pymysql://root:hc123456@106.15.224.136:3308/sqlalchemy_study", encoding="utf8", echo=False)
BaseModel = sqlalchemy.ext.declarative.declarative_base()


# 构建数据模型User
class User(BaseModel):
    __tablename__ = "Users"         # 表名
    __table_args__ = {
        "mysql_engine": "InnoDB",   # 表的引擎
        "mysql_charset": "utf8",    # 表的编码格式
    }

    # 表结构,具体更多的数据类型自行百度
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column("name", sqlalchemy.String(50), nullable=False)
    age = sqlalchemy.Column("age", sqlalchemy.Integer, default=0)

    # 添加角色id外键,关联到表Roles的id属性
    role_id = sqlalchemy.Column("role_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("Roles.id"))

    # 添加关系属性,关联到本实例的role_id外键属性上
    role = sqlalchemy.orm.relationship("Role", foreign_keys="User.role_id")

    # 添加关系属性,关联到本实例的role_id外键属性上,如果使用了这种方式,Role模型中的users可以省略
    # role = sqlalchemy.orm.relationship("Role", foreign_keys="User.role_id", backref=sqlalchemy.orm.backref("users"))


# 构建数据模型Role
class Role(BaseModel):
    __tablename__ = "Roles"         # 表名
    __table_args__ = {
        "mysql_engine": "InnoDB",   # 表的引擎
        "mysql_charset": "utf8",    # 表的编码格式
    }

    # 表结构,具体更多的数据类型自行百度
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column("name", sqlalchemy.String(50), unique=True)

    # 添加关系属性,关联到实例User的role_id外键属性上
    # users = sqlalchemy.orm.relationship("User", foreign_keys="User.role_id")


DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)   # 创建会话类
session = DBSessinon()


# 创建数据库表
def create_table():
    BaseModel.metadata.create_all(engine)


# 新增数据
def insert():
    role = Role(id=1, name="admin")
    role2 = Role(id=2, name="manager")
    role3 = Role(id=3, name="user")
    session.add(role)
    session.add(role2)
    session.add(role3)

    user = User(name="hc2", age=22, role_id=role.id)
    user2 = User(name="hc2", age=22, role_id=role3.id)
    session.add(user)
    session.add(user2)

    session.commit()


# 删除数据
def remove():
    session.query(User).filter(User.id ==2).delete()
    session.commit()


def update():
    # 修改数据
    user = session.query(User).get(1)
    user.name = "superman"
    session.merge(user)  # 使用merge方法,如果存在则修改,如果不存在则插入
    #session.query(User).filter(User.id == user.id).update({User.name: "Allen"})  # 使用update方法
    #session.query(User).filter(User.id == user.id).update({User.age: User.age + 1})  # 使用update方法,自增操作
    session.commit()


def query():
    user = session.query(User).get(1)
    role = session.query(Role).get(1)
    # print(user)
    # print(role)
    # 其他高级查询,这里以Users表为例
    users = session.query(User).filter(User.id > 6)  # 条件查询
    users = session.query(User).filter(User.id > 6).all()  # 条件查询,返回查询的全部数据
    user = session.query(User).filter(User.id > 6).first()  # 条件查询,返回查询数据的第一项
    users = session.query(User).filter(User.id > 6).limit(10)  # 条件查询,返回最多10条数据
    users = session.query(User).filter(User.id > 6).offset(2)  # 条件查询,从第3条数据开始返回

    users = session.query(User).filter(User.id > 6, User.name == "Kobe")  # 条件查询,and操作
    users = session.query(User).filter(User.id > 6).filter(User.name == "Kobe")  # 条件查询,and操作
    users = session.query(User).filter(sqlalchemy.or_(User.id > 6, User.name == "Kobe"))  # 条件查询,or操作
    users = session.query(User).filter(User.id.in_((1, 2)))  # 条件查询,in操作
    users = session.query(User).filter(sqlalchemy.not_(User.name))  # 条件查询,not操作

    user_count = session.query(User.id).count()  # 统计全部user的数量
    user_count = session.query(sqlalchemy.func.count(User.id)).scalar()  # scalar操作返回第一行数据的第一个字段
    session.query(sqlalchemy.func.count("*")).select_from(User).scalar()  # scalar操作返回第一行数据的第一个字段
    session.query(sqlalchemy.func.count(1)).select_from(User).scalar()  # scalar操作返回第一行数据的第一个字段
    session.query(sqlalchemy.func.count(User.id)).filter(User.id > 0).scalar()  # filter() 中包含 User，因此不需要指定表

    session.query(sqlalchemy.func.sum(User.age)).scalar()  # 求和运算,运用scalar函数
    session.query(sqlalchemy.func.avg(User.age)).scalar()  # 求均值运算,运用scalar函数
    session.query(sqlalchemy.func.md5(User.name)).filter(User.id == 1).scalar()  # 运用md5函数

    users = session.query(sqlalchemy.distinct(User.name))  # 去重查询,根据name进行去重
    users = session.query(User).order_by(User.name)  # 排序查询,正序查询
    users = session.query(User).order_by(User.name.desc())  # 排序查询,倒序查询
    users = session.query(User).order_by(sqlalchemy.desc(User.name))  # 排序查询,倒序查询的另外一种形式

    users = session.query(User.id, User.name)  # 只查询部分属性
    users = session.query(User.name.label("user_name"))  # 结果集的列取别名


if __name__ == '__main__':
    #create_table()
    #insert()
    #remove()
    #update()
    query()
