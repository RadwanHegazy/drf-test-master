# drf_test_master

`drf_test_master` is a Django package providing reusable test case classes for testing various scenarios of REST API endpoints. It is designed to help you quickly and consistently test authentication, permissions, CRUD operations, and error handling in your Django REST Framework projects.

## Features

- Predefined test cases for:
  - List, Retrieve, Create, Update (PUT/PATCH), and Delete endpoints
  - Authentication and permission checks (unauthorized, forbidden, admin-only, etc.)
  - Handling of empty bodies, invalid data, and not found resources
- Easy integration with your own models and endpoints
- Reduces boilerplate code in your API tests

## Installation
Clone the Repo 

```
git clone https://github.com/RadwanHegazy/drf-test-master
```

Add `drf_test_master` to your Django project (copy the `drf_test_master` directory into your project).

You can delete the directory `drf-test-master` after copy the app into your project.

Make sure to add `'drf_test_master'` to your `INSTALLED_APPS` 


```python
INSTALLED_APPS = [
    # ...
    'drf_test_master',
    # ...
]
```

## Usage

To use the test cases, subclass the relevant test case classes from `drf_test_master.testcases` and implement the required methods (`model_creation`, `get_url`, `get_body`, etc.).

**Example:**

```python
from drf_test_master.testcases.get import list
from django.urls import reverse
from example.models import ExampleModel

class TestExampleNoAuthEndpoint(
    list.TestGetEmptyResults,
    list.TestGetNotEmptyResults
):
    def model_creation(self):
        return ExampleModel.objects.create(name='test')

    def get_url(self):
        return reverse('list-no-auth')
```

You can find more usage examples in the [example/test/](example/test/) directory, such as:

- [example/test/test_list.py](example/test/test_list.py)
- [example/test/test_create.py](example/test/test_create.py)
- [example/test/test_retrieve.py](example/test/test_retrieve.py)
- [example/test/test_put.py](example/test/test_put.py)
- [example/test/test_patch.py](example/test/test_patch.py)
- [example/test/test_delete.py](example/test/test_delete.py)

These files demonstrate how to use the test case classes for different API endpoints and scenarios.

## Test Case Structure

The main test case modules are:

- [`drf_test_master.testcases.get.list`](drf_test_master/testcases/get/list.py): List endpoint tests
- [`drf_test_master.testcases.get.retrieve`](drf_test_master/testcases/get/retrieve.py): Retrieve endpoint tests
- [`drf_test_master.testcases.create.create`](drf_test_master/testcases/create/create.py): Create endpoint tests
- [`drf_test_master.testcases.update.put`](drf_test_master/testcases/update/put.py): Update (PUT) endpoint tests
- [`drf_test_master.testcases.update.patch`](drf_test_master/testcases/update/patch.py): Update (PATCH) endpoint tests
- [`drf_test_master.testcases.delete.delete`](drf_test_master/testcases/delete/delete.py): Delete endpoint tests

Each module provides base classes for common scenarios (unauthorized, forbidden, not found, success, etc.).

## License

MIT License

---

For more details and advanced usage, see the example tests in [example/test/](example/test/).
