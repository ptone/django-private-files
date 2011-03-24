try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
    name = 'django-private-files',
    version = '0.1.0',
    packages = ['private_files', 'private_files.models'],
    author = 'Vasil Vangelovski',
    author_email = 'vvangelovski@gmail.com',
    license = 'New BSD License (http://www.opensource.org/licenses/bsd-license.php)',
    description = 'Protected files in django',
    long_description = "A reusable django app that provides facilities for easy control over static file permissions.",
    url = 'https://bitbucket.org/vvangelovski/django-private-files',
    download_url = 'https://bitbucket.org/vvangelovski/django-private-files/get/v0.1.0.tar.gz',
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
