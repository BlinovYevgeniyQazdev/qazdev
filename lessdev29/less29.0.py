#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

# Определение модели
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Создание соединения с базой данных
engine = create_engine('sqlite:///:memory:')
# Создание таблицы
Base.metadata.create_all(engine)
# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление пользователя
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Запрос пользователей
users = session.query(User).all()
for user in users:
    print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')
