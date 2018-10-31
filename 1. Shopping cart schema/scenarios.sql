-- Query order history
-- Here I suppose that current user can be queried from CurrentUser.UserGuid.
SELECT a.Receiver, a.Address, a.OrderedDate, SUM(b.Price * b.Count)
FROM tb_Order AS a, tb_OrderedItem AS b
WHERE a.UserGuid = CurrentUser.UserGuid
AND a.OrderGuid = b.OrderGuid
ORDER BY a.OrderedDate


-- Add shop item into shopping cart
-- Here I suppose that current selected item can be queried from CurrentItem.ItemGuid.
INSERT INTO tb_CartItemRelation(CiGuid, CartGuid, ItemGuid, Count)
    SELECT NEWID(), CartGuid, CurrentItem.ItemGuid, 1
    FROM tb_Cart
    WHERE UserGuid = CurrentUser.UserGuid


-- Add shopping cart items into order.
-- Both order and order items need to be added, delete items in shopping cart.
DECLARE @guid CHAR(36)

SET @guid = NEWID()

INSERT INTO tb_Order(OrderGuid, UserGuid, Receiver, Address, OrderedDate)
    SELECT @guid, CurrentUser.UserGuid, Receiver.Name, Address, GETDATE()
    FROM tb_Address
    WHERE AddressGuid = SelectedAddress.AddressGuid

INSERT INTO tb_OrderedItem(OrderItemGuid, OrderGuid, ItemName, Price, ImageUri, Count)
    SELECT NEWID(), @guid, c.ItemName, c.Price, c.ImageUri, a.Count
    FROM tb_CartItemRelation AS a, tb_Cart AS b
    INNER JOIN tb_Item AS c ON c.ItemGuid = a.ItemGuid
    WHERE b.UserGuid = CurrentUser.UserGuid AND a.CartGuid = b.CartGuid

DELETE tb_CartItemRelation 
FROM tb_CartItemRelation AS a
INNER JOIN tb_Cart AS b ON a.CartGuid = b.CartGuid
WHERE b.UserGuid = CurrentUser.UserGuid
