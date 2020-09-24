# LRU Cache Python Implementation
[LRU Cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)) implementation in Python3 without using [functools](https://docs.python.org/3/library/functools.html) or any third-party packages.

## Set up and running tests
To create the virtual environment, run:
```
pip3 install --upgrade pip
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```
Then to run tests:
```
pytest . -vv -s 
```

## Future improvements
* **TTL implementation:** To create a basic TTL policy for the cache (rather than using a read count policy), we can add a key/timestamp to a secondary `OrderedDict()`. Then when we request a given key, we can write a conditional to return it from the cache if the current date is less than 30 seconds after the item was added to the cache i.e. `self.cache.pop(key) if datetime.now() > self.cache_ttl[key] + timedelta(seconds=30) else None`.
* **Test coverage**: Add updated test coverage html report to repo automatically on merged PR using [pytest-cov](https://pypi.org/project/pytest-cov/).
* **Dockerize**: Dockerize solution so no set up is required and solution can be run on any machine.
