# django-voikko-experiments

Install libvoikko
=================

macOS
-----

Requires Homebrew.

```
# Install libvoikko and dictionaries to home directory
brew install libvoikko
wget http://www.puimula.org/htp/testing/voikko-snapshot-v5/dict-morphoid.zip
mkdir ~/.voikko
unzip -d ~/.voikko/ dict-morphoid.zip

# In the same directory where this README.md is:
python3 -m venv venv
source venv/bin/activate
cd services/django_server/
pip install -r  requirements.txt -r requirements-dev.txt
python manage.py runserver
```

Ubuntu
------

```
sudo apt-get install libvoikko-dev voikko-fi
# Create venv and stuff like above(?)
```

Docker
------

```
docker-compose build
docker-compose up
```
