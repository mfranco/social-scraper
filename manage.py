from scrapers.facebook import index_profiles_by_term as index_facebook_profiles
from scrapers.twitter import index_profiles_by_term as index_twitter_profiles
from users.views import run_app

import argparse
import fileinput

def syncdb(**kwargs):
    from common.models import get_engine
    from sqlalchemy.ext.declarative import declarative_base
    from users.models import User
    engine = get_engine()
    Base = declarative_base()
    User.metadata.create_all(engine)

def runserver():
    run_app()

def test(**kwargs):
    from test import init_test
    init_test()


def index_facebook():
    """
    Read terms from data.txt file and start to perform a search by every term on facebook
    """
    term_list = []
    for line in fileinput.input('data.txt'):
        if not line.startswith('#'):
            term_list.append(line)
    index_facebook_profiles(term_list)

def index_twitter():
    """
    Read terms from data.txt file and start to perform a search by every term on twitter
    """
    term_list = []
    for line in fileinput.input('data.txt'):
        if not line.startswith('#'):
            term_list.append(line[:-1])
    index_twitter_profiles(term_list)


def main():
    parser = argparse.ArgumentParser(description='flask user api demo')
    parser.add_argument('action', nargs='+', choices=['test', 'runserver', 'syncdb',
                                                      'index_facebook', 'index_twitter'] )
    args = parser.parse_args()
    kwargs = {}
    task_dict = {'syncdb': syncdb, 'test': test, 'runserver': runserver,
                 'index_facebook': index_facebook, 'index_twitter': index_twitter}
    task = args.action[0]
    task_dict[task](**kwargs)

if __name__ == '__main__':
    main()
