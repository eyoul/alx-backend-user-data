id = Column(Integer, primary_key=True)
email = Column(String(250), nullable=False)
hashed_password = Column(String(250), nullable=False)
session_id = Column(String(250), nullable=True)
reset_token = Column(String(250), nullable=True)

def __rep__(self):
    return "<User(email='%s', hashed_password='%s', \
        session_id='%s', reset_token'%s')>" % (
        self.email, self.hashed_password,
        self.session_id, self.reset_token)
