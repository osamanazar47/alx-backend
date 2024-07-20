# 0x00-pagination

This directory contains projects that explore various concepts of pagination in backend development. The tasks include implementing basic pagination, hypermedia pagination, and deletion-resilient pagination. Each task is designed to help you understand and implement different pagination strategies effectively.

## Tasks

### 0. Simple Helper Function
Objective: Write a function named index_range that takes two integer arguments: page and page_size.

Functionality:

Returns a tuple of size two containing the start index and end index for pagination.
Page numbers are 1-indexed (i.e., the first page is page 1).

### 1. Simple Pagination
Objective: Extend the previous task by implementing a Server class for paginating a dataset of popular baby names.

Class Details:

DATA_FILE points to "Popular_Baby_Names.csv"
Method dataset() loads and caches the dataset.
Method get_page() retrieves a specific page from the dataset.

### 2. Hypermedia Pagination
Objective: Implement a get_hyper method in the Server class to provide hypermedia pagination.

Method Details:

Returns a dictionary with:
page_size: length of the returned dataset page
page: current page number
data: dataset page
next_page: number of the next page, or None if no next page
prev_page: number of the previous page, or None if no previous page
total_pages: total number of pages in the dataset

### 3. Deletion-Resilient Hypermedia Pagination
Objective: Implement a get_hyper_index method to handle pagination in the presence of deletions.

Method Details:

Returns a dictionary with:
index: current start index of the return page
next_index: next index to query with
page_size: current page size
data: actual page of the dataset