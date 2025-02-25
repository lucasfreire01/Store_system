CREATE VIEW IF NOT EXISTS users_role AS 
                    SELECT
                    Users.id AS user_id,
                    Users.username AS username,
                    Users.email AS email,
                    Users.has_role AS has_role,
                    Users.password_hash AS password_hash,
                    Users.role_id AS role_id,
                    Users.created_at AS created_at,
                    Users.last_login AS last_login,
                    Roles.id AS roles_id,
                    Roles.name AS role_name,
                    Roles.description AS role_description
                    FROM 
                    Users
                    LEFT JOIN 
                    Roles ON Users.has_role = Roles.id
               