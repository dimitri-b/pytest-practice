pytest-nice : A plugin for pytest
=================================

Make failure notification more politically correct and less offensive.

Features
--------

- Adds ``--nice`` command line option, which will:
    - turn ``F`` into ``WN`` for 'Work Needed'
    - ditto, but spelled out when using ``-v`` option

Installation
------------

Same as any other, using pip from .tar.gz file.

.. code-block:: bash

    $ pip install PATH/pytest-nice-0.1.0.tar.gz ​ 
    $ pip install --no-index --find-links PATH pytest-nice ​

Usage
-----

.. code-block:: bash

    $pytest --nice
