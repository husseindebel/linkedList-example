from setuptools import setup

setup(
    name='flask-example',
    packages=['app'],
    include_package_data=True,
    install_requires=[
	'pytest',
        'flask',
        'flask-login',
    ],
)
