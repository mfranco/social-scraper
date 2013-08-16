from common.models import BaseModel, JSONEncodedDict

from sqlalchemy import Column, String


class AuthenticationError(Exception):
    pass

class User(BaseModel):
    username = Column(String(256), index=True, unique=True, nullable=False)
    name = Column(String(256), nullable=False)
    json_context = Column(JSONEncodedDict())

    def add(self):
        super(User, self).add()

    def __repr__(self):
        return '<User> {0}-{1}'.format(self.username, self.name)
