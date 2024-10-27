# Pagination Project

This project demonstrates various techniques for paginating a dataset of popular baby names. The dataset is stored in a CSV file named `Popular_Baby_Names.csv`. The project is divided into several tasks, each implementing a different pagination strategy.

## Files

- `0-main.py`: Entry point for the simple helper function.
- `0-simple_helper_function.py`: Contains the `index_range` function used to calculate the start and end indices for pagination.
- `1-main.py`: Entry point for simple pagination.
- `1-simple_pagination.py`: Implements a basic pagination system using the `Server` class.
- `2-main.py`: Entry point for hypermedia pagination.
- `2-hypermedia_pagination.py`: Implements hypermedia pagination using the `Server` class.
- `3-main.py`: Entry point for deletion-resilient hypermedia pagination.
- `3-hypermedia_del_pagination.py`: Implements deletion-resilient hypermedia pagination using the `Server` class.
- `Popular_Baby_Names.csv`: The dataset used for pagination.

## Pagination Techniques

### Simple Pagination

Implemented in [`1-simple_pagination.py`](0x00-pagination/1-simple_pagination.py), this technique uses the `Server` class to paginate the dataset. The `get_page` method returns a specific page of the dataset based on the page number and page size.

### Hypermedia Pagination

Implemented in [`2-hypermedia_pagination.py`](0x00-pagination/2-hypermedia_pagination.py), this technique extends simple pagination by providing additional metadata. The `get_hyper` method returns a dictionary containing the page size, current page number, dataset page, next page number, previous page number, and total number of pages.

### Deletion-Resilient Hypermedia Pagination

Implemented in [`3-hypermedia_del_pagination.py`](0x00-pagination/3-hypermedia_del_pagination.py), this technique ensures that pagination remains consistent even when items are deleted from the dataset. The `get_hyper_index` method returns a dictionary containing the current index, dataset page, page size, and the next index.

## Usage

To run any of the main scripts, use the following command:

```sh
python3 <main_script>.py