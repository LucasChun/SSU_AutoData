from setuptools import setup

setup(
    name='AutoDataClean',
    version='0.0.1',
    description='pip install test',
    url='https://github.com/LucasChun/SSU_AutoData.git',
    author='chunhyeonu',
    author_email='hyeonu.chun@gmail.com',
    license='hyeonu',
    packages=['AutoDataClean'],
    zip_safe=False,
    install_requires=[
        'loguru',
        'ujson',
        'torch',
        'numpy',
        'scikit-learn',
        'pandas',
        'tqdm'
    ]
)
