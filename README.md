# django-voikko-experiments

Install libvoikko
=================

Mac Os X
--------

You need Home Brew.

```
brew install libvoikko
wget http://www.puimula.org/htp/testing/voikko-snapshot/dict-morphoid.zip

# Install dictionaries globally available:
sudo mkdir /etc/voikko
sudo unzip -d /etc/voikko/ dict-morphoid.zip

# Install to home directory
mkdir ~/.voikko
unzip -d ~/.voikko/ dict-morphoid.zip
```

Ubuntu
------

```
sudo apt-get install libvoikko-dev voikko-fi
```

libvoikkoX.py
=============

libvoikko2.py is Python2 compatible version of the library and libvoikko3.py
is Python3 compatible. Both are slightly modified versions of original
libvoikko.py.

Changes:
- tabs are replaced with spaces
- Voikko.__getLib() is fixed to work in MacOsX (in addition to windows and
  linux)
