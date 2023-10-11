-- a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_items AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - new.number WHERE name = new.item_name;
