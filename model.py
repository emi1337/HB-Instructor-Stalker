from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///checkins.db", echo = False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

def authenticate(email, password):
    print "0000000000000000000000000000000000000000000000"
    user_info = session.query(User).filter_by(email=email, password=password).one()
    print user_info
    if user_info:
        print user_info.email, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        print user_info.password, "BBBBBBBBBBBBBBBBBBBBBBBBBBB"
        print user_info
        return user_info.id

    if result:
      fields = ["id", "email", "password", "username"]
      print "You've been authorized!"
      return dict(zip(fields, result))
    else:
      return None


### Class declarations go here
class User(Base):
    # informs SQLAlchemy that instances of this class will be stored in table named users
    __tablename__ = "users"


    # tells SQLAlchemy to add column to table named "id" as primary key
    id = Column(Integer, primary_key = True)
    # nullable = True means that the information isn't required
    email = Column(String(64))
    password = Column(String(64))
    name = Column(String(64))
    img_color_url = Column(String(128), nullable = True)
    img_color_bw = Column(String(128), nullable = True)
    role = Column(Integer) # 1 = instructor, 0 = student, other
    status = Column(Integer, nullable = True) # 2 = "in the office" 1 = "out but available online", 0 = "out"
    
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key = True)
    # declaring it to be a ForeignKey = references another column in another table (the users.id column)
    event_user_id = Column(Integer, ForeignKey('users.id'))
    creator_user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(128), nullable = True)
    add_time = Column(Date)
    start_time = Column(DateTime, nullable = True)
    end_time = Column(DateTime, nullable = True)


    event_user = relationship("User", primaryjoin=event_user_id==User.id, backref=backref("events"))
    creator_user = relationship("User", primaryjoin=creator_user_id==User.id)
    # backref=backref("events", order_by=id), 


### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
