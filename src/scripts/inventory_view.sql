CREATE VIEW IF NOT EXISTS inventory_view AS 
            SELECT
            categories.id AS category_id,
            categories.name AS category_name,
            categories.description AS category_description,
            
            item.id AS item_id,
            item.name AS item_name,
            item.description AS item_description,
            item.category_id AS item_category_id,
            item.sku AS item_sku,
            item.price AS item_price,
            item.supplier_id AS item_supplier_id,
            item.create_at AS item_create_at,
            item.updated_at AS item_updated_at,
            
            inventory.id AS inventory_id,
            inventory.item_id AS inventory_item_id,
            inventory.quantity AS inventory_quantity,
            inventory.location AS inventory_location,
            inventory.reorder_level AS inventory_reorder_level,
            inventory.last_updated AS inventory_last_updated,
            
            suppliers.id AS supplier_id,
            suppliers.name AS supplier_name,
            suppliers.email AS supplier_email,
            suppliers.phone AS supplier_phone,
            suppliers.address AS supplier_address
            
            FROM 
            categories
            LEFT JOIN 
            item ON categories.id = item.category_id
            LEFT JOIN 
            inventory ON item.id = inventory.item_id
            LEFT JOIN 
            suppliers ON item.supplier_id = suppliers.id
           
        
       
        
      