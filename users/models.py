from common.models import BaseModel, JSONEncodedDict

from sqlalchemy import Column, String, Integer


class AuthenticationError(Exception):
    pass

class User(BaseModel):
    SOURCE_ENUM = BaseModel.enum(FACEBOOK=1, TWITTER=2)
    username = Column(String(256), index=True, unique=True, nullable=False)
    name = Column(String(256), nullable=False)
    json_context = Column(JSONEncodedDict())
    source = Column(Integer, nullable=False)
    popularity_index = Column(Integer)

    def add(self):
        super(User, self).add()

    def to_serializable_dict(self):
        serialized_dict = {}
        serialized_dict['username'] = self.username
        serialized_dict['popularity_index'] = self.popularity_index
        if self.source == User.SOURCE_ENUM.FACEBOOK:
            serialized_dict['source'] = 'Facebook'
            serialized_dict['description'] = ''
        else:
            serialized_dict['source'] = 'Twitter'
            serialized_dict['description'] = ''

        return serialized_dict

    def __repr__(self):
        return '<User> {0}-{1}'.format(self.username, self.name)
