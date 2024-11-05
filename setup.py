from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    tests_require=['unittest'],
    test_suite='tests',
    author='Prashanth Gadwala',
    author_email='prashanth.gadwala@fau.de',
    description='Homework 2 for data science and practicing Git version system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prashanthgadwala/dsss_homework_2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)