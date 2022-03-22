SELECT * FROM auth_user
SELECT * FROM authtoken_token
SELECT * FROM init_finalapi_inventory
SELECT * FROM init_finalapi_employee
SELECT * FROM init_finalapi_customer
SELECT * FROM init_finalapi_picklistline

UPDATE auth_user SET is_staff=True 
WHERE id=6