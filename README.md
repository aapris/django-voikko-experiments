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

