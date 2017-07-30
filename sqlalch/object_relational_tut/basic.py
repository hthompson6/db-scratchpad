from sqlalchemy import Column, Integer, String, DateTime, Unicode, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Basic table
class Block(Base):
    __tablename__ = 'block'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Widget(Base):
    __tablename__ = 'widget'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)

    __mapper_args__ = {
                       'version_id_col': timestamp,
                       'version_id_generator': lambda v:datetime.now()
                      }

# New attribute definitions
Block.data = Column('data', Unicode)
# Block.related = relationship(RelatedInfo)

# Using standard MetaData object
engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

# Using custom MetaData Object
# mymetadata = MetaData()
# Base = declarative_base(metadata=mymetadata)
