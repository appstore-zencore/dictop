dictop
======

.. image:: https://travis-ci.org/appstore-zencore/dictop.svg?branch=master
    :target: https://travis-ci.org/appstore-zencore/dictop

DICT-OPERATION allow you select data value from a dict-instance with dot separated path, and update.


Required Python Version
-----------------------

- python 2.7
- python 3.6

Install
-------

::

    pip install dictop


Usage
-----

::

    from dictop import update
    from dictop import select

    data = {}
    update(data, "a.b.c", 2)
    assert select(data, "a.b.c") == 2

Core Functions
--------------

1. select

        select(target, path, default=None, slient=True)

2. update

        update(target, path, value)

