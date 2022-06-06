from setuptools import setup


setup(
    name='mypackage',
    entry_points={
        'sphinx.builders': [
            'custom = mypackage:MyBuilder',
        ],
    },
    py_modules=['mypackage']
)
