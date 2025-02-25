CREATE VIEW IF NOT EXISTS orders_view AS 
                            SELECT
                            orders.id AS orders_id,
                            orders.user_id AS orders_user_id,
                            orders.order_date AS order_date,
                            orders.status AS order_status,
                            orders.total_amount AS order_total_amount,
                            orders.shipping_address AS shipping_address,
                            orders.billing_address AS billing_address,
                            orders.create_at AS order_create_at,
                            orders.update_at AS order_update_at,
                
                            order_items.id AS order_items_id,
                            order_items.order_date AS order_items_date,
                            order_items.item_id AS order_item_id,
                            order_items.quantity AS order_quantity,
                            order_items.price_at_purchase AS order_price,
                
                            order_statuses.id AS statuses_id,
                            order_statuses.status AS statuses_status
                            
                            FROM 
                            orders
                            LEFT JOIN 
                            order_items ON orders.id = order_items.id
                            LEFT JOIN 
                            order_statuses ON orders.status = order_statuses.status
                        