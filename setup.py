from setuptools import setup

setup(
  name = 'colorlover',
  packages = ['colorlover'], # this must be the same as the name above
  version = '0.3.0',
  description = 'Color scales for IPython notebook',
  author = 'Jack Parmer',
  author_email = 'jack@plot.ly',
  url = 'https://github.com/jackparmer/colorlover', # use the URL to the github repo
  keywords = ['ipython notebook','color scales'], # arbitrary keywords
  classifiers = [
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
  ],
)
