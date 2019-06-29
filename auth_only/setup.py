from setuptools import setup


setup(
    name='dashboard',
    version='0.1.0',
    install_requires=['dash', 'dash-daq', 'gunicorn', 'pyjwt'],
    packages=['auth', 'dashboard', 'dashboard.callbacks', 'dashboard.layout'],
    package_data={'auth': ['templates/login.html']},
    entry_points={
        'console_scripts': [
            'auth_server = auth.app:main',
            'dashboard_server = dashboard.app:main',
        ]},
)
