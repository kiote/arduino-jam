from fabric.api import *
import fabric_gunicorn as gunicorn

# the user to use for the remote commands
env.user = 'apps'
# the servers where the commands are executed
env.hosts = ['62.75.191.219']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/arduino-jam.tar.gz')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir /tmp/arduino-jam')
    with cd('/tmp/arduino-jam'):
        run('tar xzf /tmp/arduino-jam.tar.gz')
        # now setup the package with our virtual environment's
        # python interpreter
        run('/var/www/arduino-jam/env/bin/python setup.py install')
    # now that all is set up, delete the folder again
    run('rm -rf /tmp/arduino-jam /tmp/arduino-jam.tar.gz')
    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    gunicorn.restart