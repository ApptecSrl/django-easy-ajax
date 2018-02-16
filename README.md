# django-easy-ajax

Django application that renders template block through AJAX calls


### Requirements

```
Python >= 2.7
Django >= 1.8.8
```

### Installing

Download and install package through Github

```
pip install -e git://github.com/ApptecSrl/django-easy-ajax#egg=django_easy_ajax
```

Add ``'django_ajax'`` and ``'django_easy_ajax'`` into the ``INSTALLED_APPS``

## Running the tests

The tests will be written shortly.


## USAGE

* Create a function that return a model object ( not a queryset) like this:


```python

from oscar.core.loading import get_model


def get_product(id=None):
    product = get_model('catalogue', 'Product')
    return product.objects.get(id=id)
```

* Create a template for render the object i.e ``ajax/my_ajax_product.html``

```
<h1> My AJAX product</h1>

<h3>{{ object }}</h3>

```

* In ``settings.py`` define a this dictionary

```python
EASY_AJAX = {
    'test_function': ['fooproject.utils.get_product', 'ajax/my_ajax_product.html']
}
```

* In ``urls.py`` open this url.

```python

url(r'easy_ajax/', include('django_easy_ajax.urls')),
```


* Call your ajax template using the template tag ``get_ajax_object`` and :

```
{% load easy_ajax %}

<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>

{% for product in products %}

    {% get_ajax_object 'test_function' product.id %}

{% endfor %}

</body>
</html>
```