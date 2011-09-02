from distutils.core import setup

name = 'jquery'

setup(
    name=name,
    version='1.6.2',
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % name,
    url='http://github.com/asteven/%s/' % name,
    description='Package jquery and jquery-ui for use with django staticfiles',
    packages=[name],
    package_data={
        name: [
            'static/jquery/js/*.js',
            'static/jquery/css/smoothness/*.css',
            'static/jquery/css/smoothness/images/*.png',
        ]
    },
)

