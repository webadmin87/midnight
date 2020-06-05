from setuptools import setup, find_packages
import os


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python :: 3.4',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
]

INSTALL_REQUIREMENTS = [
    'psycopg2',
    'docutils',
    'Pillow',
    'django==1.11.29',
    'django-mptt==0.8.0',
    'sorl-thumbnail==12.3',
    'django-assets==0.11',
    'django-bootstrap-pagination==1.5.1',
    'django-bootstrap-form',
    'django-simple-captcha==0.5.1',
    'django-registration-redux==1.3',
    'django-debug-toolbar==1.4',
    'django-precise-bbcode==1.1.1',
    'django-grappelli==2.7.3',
    'django-filebrowser==3.6.1',
    'django-ckeditor==5.0.2',
    'jsmin',
    'cssmin',
    'django-haystack==2.4.0',
    'django-autocomplete-light==3.0.2',
]

setup(
    author='Churkin Anton',
    author_email='webadmin87@gmail.com',
    name='midnight',
    version='0.1.1-alpha',
    description='Amazing cms powered by Django framework',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/webadmin87/midnight',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
