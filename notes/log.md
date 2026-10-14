First response was successful: Anna Smith 99.9

second response failed: Traceback (most recent call last):
  File "/Users/quwam/Desktop/main/projects/thesis/consumer.py", line 8, in <module>
    response.raise_for_status()
  File "/Users/quwam/Desktop/main/projects/thesis/.venv/lib/python3.12/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Client error '404 Not Found' for url 'http://127.0.0.1:8002/users/1'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404