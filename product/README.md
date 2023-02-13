```bash
poetry run python -m pytest -s -vv
```


To generate proto file:
```bash
poetry run python manage.py generateproto --model django_app.models.ProductModel --file proto/product.proto
```
