# Shopping cart schema
## ER Disgram
<img src="https://i.imgur.com/fmldsvK.png"/>

For the index in `tb_item`, I think `ItemName`, `ImageUri` and  `Price` are often be queried in the system, including order history page drill down and item detail page, make them be indexed should let these kinds of queries faster.

## scenarios.sql

In `scenarios.sql`, I tried to do several SQL operations to ensure the correctness of schema.
* Query order history - Required
* Add shop item into shopping cart
* Add shopping cart items into order.
