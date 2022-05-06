from setuptools import setup

setup(
    name='AutoClean',
    version='0.0.1',
    description='pip install test',
    url='https://github.com/LucasChun/SSU_AutoData.git',
    author='chunhyeonu',
    author_email='hyeonu.chun@gmail.com',
    license='hyeonu',
    packages=['AutoClean'],
    zip_safe=False,
    install_requires=[
        'ujson',
        'py-AutoClean',
        'datawig==0.2.0',
        'torch',
        'scipy==1.5.4'
    ]
)
