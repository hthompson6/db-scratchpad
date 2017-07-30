from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return ("<User(name='{0}', fullname='{1}', password='{2}'").format(self.name,
                                                                           self.fullname,
                                                                           self.password)

first_user = User(name='monty', fullname='Monty Python', password='elderberries')

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Adding objects
session.add(first_user)


