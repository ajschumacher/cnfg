.. image:: https://coveralls.io/repos/ajschumacher/cnfg/badge.svg
   :target: https://coveralls.io/r/ajschumacher/cnfg
   :alt: test coverage

====
cnfg
====

Simple configuration should be simple. Here's ``example.py``::

  import cnfg
  settings = cnfg.load('.examplerc')
  print(settings['message'])

Relative paths are awful. Not all systems have ``/etc``. The only
reasonable place to put configuration is in your home directory.

JSON and YAML are not Python. ``eval`` is not so bad. Here's
``.examplerc``::

  # It's Python, so you can use comments (and more)
  {"message": "My custom message."}

Now all of these work, with relative directories as implied::

  ./example.py
  python ../example.py
  cat example/example.py | python


What about default settings?
----------------------------

It's up to you, but it's easy, especially if you're keeping all your
configuration in a dict::

  settings = {"message": "Default message!"}
  settings.update(cnfg.load('.examplerc'))


What about environment variables?
---------------------------------

It's up to you, but it's easy::

  import os
  some_var = os.getenv("SOME_VAR", "some default value")


What about “``from config import settings``,” like confire_?
------------------------------------------------------------

It's up to you, but it's easy. Just make a file called ``config.py``
and define ``settings`` in it.

.. _confire: https://github.com/bbengfort/confire


Where's my home directory?
--------------------------

On a Mac or Linux machine, ``echo ~``. On Windows, ``echo
%userprofile%``.


This is so abstract!
--------------------

Check out the example_.

.. _example: https://github.com/ajschumacher/cnfg/tree/master/example


This is so trivial!
-------------------

Yes, it's as simple as possible, and it's useful all over the place
and the right level of complexity for a lot of projects.
