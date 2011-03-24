try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
    name = 'django-private-files',
    version = '0.1.1',
    packages = ['private_files', 'private_files.models'],
    author = 'Vasil Vangelovski',
    author_email = 'vvangelovski@gmail.com',
    license = 'New BSD License (http://www.opensource.org/licenses/bsd-license.php)',
    description = 'Protected files in django',
    long_description = open("README.rst").read(),
    url = 'https://bitbucket.org/vvangelovski/django-private-files',
    download_url = 'https://bitbucket.org/vvangelovski/django-private-files/downloads',
    include_package_data = True,
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
