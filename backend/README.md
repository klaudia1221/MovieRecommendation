# Lista serverów i jak je uruchamiać

## `movies_server.py`

`movies_server.py` - biblioteka do używania przez serwer

```python
import movies_server as ms

ms.movies_cold() # lista 20 filmów dla użytkownika, na początku do oceny

ms.get_movies_recommendations(list) # pobieranie wszystkich rekomendowanych filmów dla listy
```

## `server_aws.py`

- `server_aws.py` - serwer używany przez aws, ma wymuszenie certyfikatu oraz ścieżki do SSLa

### Uruchomienie serwera do testów

```python
python3 server_aws.py
```

### Uruchomienie serwera

```python
nohup python3 server_aws.py &
```

### Zabicie serwera

```python
ps -ef | grep server_aws.py
kill 1705
```

## `server_local.py`

`server_local.py` - serwer używane do lokalnego uruchamia`

Uruchmienie serwera:

```python
python3 server_local.py
```