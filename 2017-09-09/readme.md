# Hackers Mangaluru Web-scraping Training

## Pre-requisites

* [Python3](!https://www.python.org/downloads/)
* [pip3](!https://bootstrap.pypa.io/get-pip.py)
* [bs4](!https://www.crummy.com/software/BeautifulSoup/bs4/download/4.6/beautifulsoup4-4.6.0.tar.gz) (Also known as Beautiful Soup)
* [requests](!https://pypi.python.org/packages/b0/e1/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d09/requests-2.18.4.tar.gz#md5=081412b2ef79bdc48229891af13f4d82)
* [virtualenv](!https://pypi.python.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz#md5=44e19f4134906fe2d75124427dc9b716)

## Installation Instructions

* Download and install python3 from the given link

* Setting path is necessary in Windows system to access data from any folder location.

* Download pip3 from the above given link
  * Run `python3 get-pip.py`. Use Superuser mode if neccessary.

* Install virtualenv
  * `pip install virtualenv`

  * `mkdir web-scraping`

  * `virtualenv web-scraping`

  * `cd web-scraping; source ./bin/activate`
    * Console prompt should be like `(web-scraping) machine-name@user-name$` 

* Installing requests and bs4
  * `pip3 install bs4 requests lxml`. Use Superuser mode if required. <br/>
  OR
  * Download zip file from above link and Run
    * `python path-to-folder/setup.py install`

The setup is complete

## Testing installation

* `which python`

* `which pip`

* `which python3`

* `which pip3`

* `$ python`

```python
>>> import requests
>>> import bs4
>>> 
```

## Getting Started with requests

requests package is used to do Http Requests from the machine to any website.

Using requests you can make requests for several method like GET, POST, PUT, DELETE, etc...
Each of these methods have a functions defined in requests package that takes several arguments.

### The GET method

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
response = requests.get('https://www.httpbin.org/ip')

# To recieve text response
text_data = response.text
print(text_data)
# Expected output is 
# {
#    "origin": "159.91.150.12"
# }

# To receive binary response
binary_data = response.content
# Expected output is b'{\n  "origin": "159.91.150.12"\n}\n'

# If the response is in json, and to convert to python data-type.
# If response is not in json it will throw JSONDecodeError
python_dtype_data = response.json()
## Expected output is {"origin": "159.91.150.12"} a Python dict
```

## Exercise-1

Download data from https://example.com as save it in a file

## Introduction to bs4

```python
import re
from bs4 import BeautifulSoup as bsoup4
filename = 'path-to-file/filename'
with open(filename, mode='r') as handle:
     # markup fields accepts str, or file opener
     html_doc = """
         <html><head><title>The Dormouse's story</title></head>
          <body>
          <p class="title"><b>The Dormouse's story</b></p>
          <p class="story">Once upon a time there were three little sisters; and their names ˓→were
          <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
          <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
          <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
          and they lived at the bottom of a well.</p>
          <p class="story">...</p>
    """
     soup = bsoup4(markup=handle, features='lxml')

print(soup.prettify())

print(soup.title, type(soup.title))

print(soup.title.name, type(soup.title.name))

print(soup.title.string, type(soup.title.string))

print(soup.title.text, type(soup.title.text))

# attributes
print(soup.head.meta.attrs)

print(soup.find(name='a', href='http://example.com/tillie'))

print(soup.find_all(name='a', recursive=False, limit=2))
```

### Moving Forward in HTML Tree

Property | Corresponding Function
------------ | -------------
`next` (Depricating) | `find_next` or `find_all_next` or `find` or `find_all`
`next_element` or `next_elements` | `find_next_element` or `find_next_elements`

### Moving Backwards in HTML Tree

Property | Corresponding Function
------------ | -------------
`previous` (Depricating) | `find_previous` or `find_all_previous`
`previous_element` or `previous_elements` | `find_previous_element` or `find_previous_elements`

### Moving side ways in the same node level in HTML

Property | Corresponding Function
------------ | -------------
`next_sibling` _or_ `next_siblings` | `find_next_sibling` _or_ `find_next_siblings`
`previous_sibling` _or_ `previous_siblings` | `find_previous_sibling` _or_ `find_previous_siblings`

### Moving up in the HTML Tree

Property | Corresponding Function
------------ | -------------
`parent` _or_ `parents` | `find_parent` _or_ `find_parents`


### Moving down in the HTML Tree

Property | Corresponding Function | Meaning
------------ | ------------ | -------------
`children` or `contents` | `find_children` | _Direct Children_
`decendants` | `find_decendants` | _Direct children and children of direct children recursively_
`string` | `tag_object.find(string=True)` | If a tag has only one child and is of type NavigableString, this works
`strings` | `tag_object.find_all(string=True)`
`stripped_strings` | - | returns generator with trimmed strings

