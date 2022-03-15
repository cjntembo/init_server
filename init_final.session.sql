SELECT * FROM auth_user
SELECT * FROM authtoken_token
SELECT * FROM init_finalapi_inventory
SELECT * FROM init_finalapi_employee
SELECT * FROM init_finalapi_customer

UPDATE auth_user SET is_superuser=True 
WHERE id=1