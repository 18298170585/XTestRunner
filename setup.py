# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('XTestRunner/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='XTestRunner',
    version=version,
    url='https://github.com/seldomQA/XTestRunner/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='Unittest-based HTML test report.',
    long_description="Unittest-based HTML test report.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2>=2.11.3',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    py_modules=['whyteboard'],
    scripts=[
        'XTestRunner/html/heading.html',
        'XTestRunner/html/mail.html',
        'XTestRunner/html/report.html',
        'XTestRunner/html/stylesheet.html',
        'XTestRunner/html/template.html',
    ],
)