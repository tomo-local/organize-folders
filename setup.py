from setuptools import setup, find_packages

setup(
  name='organizedFile',
  version='1.0',
  description='ファイルを日付ごとに整理する',
  author='Togashi Tomohiro',
  author_email='shinsi4545@gmail.com',
  url='https://github.com/Totoro-moroku/organize_folders',
  packages=find_packages(),
  entry_points="""
    [console_scripts]
    clearfiles = origanizeFilePackage.main:main
  """
)