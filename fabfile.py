from fabric.api import *
from contextlib import contextmanager

env.hosts = ['host_name']
env.user = 'user_name'
env.keyfile = ['$HOME/.ssh/private_key']
env.directory = '/path/to/project'
env.activate = 'source /path/to/virtualenv/bin/activate'
env.uwsgi_pid = '/tmp/project_name.pid'
env.target_env = 'prod'


@contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


def pull_data():
    with virtualenv():
        run('git pull origin master')
        run('cp -f midnight/env/%s/settings_local.py midnight/settings_local.py' % env.target_env)


def pip_install():
    with virtualenv():
        run('pip install -e .')


def bower_install():
    with virtualenv():
        run('bower install')


def collect_static():
    with virtualenv():
        run('./manage.py collectstatic --noinput')


def migrate():
    with virtualenv():
        run('./manage.py migrate')


def reload_uwsgi():
    run('uwsgi --reload '+env.uwsgi_pid)


def deploy():
    execute(pull_data)
    execute(pip_install)
    execute(bower_install)
    execute(collect_static)
    execute(migrate)
    execute(reload_uwsgi)
