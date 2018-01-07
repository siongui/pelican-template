===============
How to Develope
===============

.. image:: https://travis-ci.org/USERNAME/REPO.png?branch=master
    :target: https://travis-ci.org/USERNAME/REPO

.. See how to add travis ci image from https://raw.githubusercontent.com/demizer/go-rst/master/README.rst
   https://github.com/demizer/go-rst/commit/9651ab7b5acc997ea2751845af9f2d6efee825df

Development Tool: Pelican_ (static site generator written in Python)

Development Environment: `Ubuntu 17.10`_


First-time Setup
----------------

1. Install git_ and pip_:

   .. code-block:: bash

     $ sudo apt-get install git
     $ sudo apt-get install python-pip

2. Install language packages to add locale (English, Traditional Chinese, and
   Thai in this example):

   .. code-block:: bash

     $ sudo apt-get install language-pack-en
     $ sudo apt-get install language-pack-zh-hant
     $ sudo apt-get install language-pack-th

3. git clone source code:

   .. code-block:: bash

     $ cd
     $ mkdir dev
     $ cd ~/dev/
     $ git clone https://github.com/siongui/pelican-template.git YOUR_REPO

4. Install Python tools:

   .. code-block:: bash

     $ cd ~/dev/YOUR_REPO/
     $ sudo pip install -r requirements.txt

5. Install Pelican `i18n_subsites`_ plugin and download `normalize.css`_:

   .. code-block:: bash

     $ cd ~/dev/YOUR_REPO/
     $ make download

6. Generate CSS file:

   .. code-block:: bash

     $ cd ~/dev/YOUR_REPO/
     $ make scss


Auto-deploy by `Travis CI`_
---------------------------

See `GitHub Pages Deployment - Travis CI`_.

First save your `personal access token`_ in `repository settings`_.

For User Pages, the following is sample config:

.. code-block:: yaml

  deploy:
    provider: pages
    repo: USERNAME/USERNAME.github.io
    target_branch: master
    skip_cleanup: true
    github_token: $GITHUB_TOKEN
    local_dir: output
    on:
      branch: master

For Project Pages, the following is sample config:

.. code-block:: yaml

  deploy:
    provider: pages
    skip_cleanup: true
    github_token: $GITHUB_TOKEN
    local_dir: output
    on:
      branch: master


Daily Development
-----------------

.. code-block:: bash

    # start edit and develope
    $ cd ~/dev/YOUR_REPO/
    # If something changes, re-generate the website:
    $ make html
    # start dev server
    $ make serve
    # open your browser and preview the website at http://localhost:8000/


Note for `Google Adsense`_
++++++++++++++++++++++++++

Edit the following three files to include your code:

- `theme/templates/layout/includes/adsense.html <theme/templates/layout/includes/adsense.html>`_
- `theme/templates/layout/includes/adsense_page_level.html <theme/templates/layout/includes/adsense_page_level.html>`_
- `plugins/adsense/adsense.py <plugins/adsense/adsense.py>`_

Add ``:adsense: yes`` to the articles that you want to put ads in. See
`content/articles/2016/02/16/c-hello-world%en.rst <content/articles/2016/02/16/c-hello-world%en.rst>`_
for example.
Or use directive to include ads in articles. See raw file of
`content/articles/2016/02/16/c-hello-world%zh.rst <content/articles/2016/02/16/c-hello-world%zh.rst>`_
for example.


UNLICENSE
---------

All works, including posts and code, of Siong-Ui Te are released in public domain.
Please see UNLICENSE_.


References
----------

.. [1] `Deploy Website by Pelican, Travis CI, and GitHub Pages <https://siongui.github.io/2016/01/05/deploy-website-by-pelican-travis-ci-github-pages/>`_

.. [2] JINJA_FILTERS in `Settings — Pelican documentation <http://docs.getpelican.com/en/latest/settings.html>`_

       `Jinja custom filters documentation <http://jinja.pocoo.org/docs/dev/api/#custom-filters>`_


.. _Pelican: http://blog.getpelican.com/
.. _Ubuntu 17.10: http://releases.ubuntu.com/17.10/
.. _UNLICENSE: http://unlicense.org/
.. _git: https://git-scm.com/
.. _pip: https://pypi.python.org/pypi/pip
.. _i18n_subsites: https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites
.. _normalize.css: https://necolas.github.io/normalize.css/
.. _Travis CI: https://travis-ci.org/
.. _GitHub Pages Deployment - Travis CI: https://docs.travis-ci.com/user/deployment/pages/
.. _personal access token: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
.. _repository settings: https://docs.travis-ci.com/user/environment-variables#Defining-Variables-in-Repository-Settings
.. _Google Adsense: https://www.google.com/search?q=Google+AdSense
