# django-voikko-experiments

Install libvoikko
=================

macOS
-----

Requires Homebrew.

```
brew install libvoikko
wget http://www.puimula.org/htp/testing/voikko-snapshot-v5/dict-morphoid.zip
# if you have libvoikko < 4, use this:
# wget http://www.puimula.org/htp/testing/voikko-snapshot/dict-morphoid.zip

# Install dictionaries to home directory
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
