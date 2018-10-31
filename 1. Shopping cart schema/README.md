# Shopping cart schema
## ER Disgram
<img src="https://i.imgur.com/BmrfRGc.png"/>

For the index in `tb_Item`, since a searching engine must be implemented in a shopping system, `ItemName` and `Price` are the most frequent used in searching, make them be indexed should let these kinds of queries faster.

## scenarios.sql

In `scenarios.sql`, I tried to do several SQL operations to ensure the correctness of schema.
* Query order history - Required
* Add shop item into shopping cart
* Add shopping cart items into order.
