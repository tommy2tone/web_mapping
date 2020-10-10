from setuptools import setup, find_packages

requires = [
    'pandas',
    'folium',


]

setup(
    name='web_mapping',
    version='',
    packages=find_packages(),
    keywords='python pandas folium',
    url='',
    license='',
    author='Tom Hildebrand',
    author_email='t1manster@gmail.com',
    description='Web mapping to visually depict population density and volcanos.',
    install_requires=requires
)
