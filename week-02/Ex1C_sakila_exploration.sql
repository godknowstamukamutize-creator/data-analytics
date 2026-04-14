/*
a) The actor table includes actor_id, first_name, last_name, and last_update columns.

b) The film table includes film_id, title, description, release_year, language_id, rental_duration, rental_rate, 
   length, replacement_cost, rating, and special_features.

c) The film_actor table contains columns for both actor_id and film_id, linking actors to the films they appeared in.

d) The rental table includes rental_id, rental_date, inventory_id, customer_id, return_date, and staff_id. The information is hard to read because it uses ID numbers instead of actual names, so you cannot tell what film or customer is involved without looking up those IDs elsewhere.

e) The inventory table includes inventory_id, film_id, 
   store_id, and last_update. It tracks which specific 
   copies of films are available at which store.

f) To find the names of all films rented on a specific date, 
   you need the rental table (for the rental date and 
   inventory_id), the inventory table (to link inventory_id 
   to film_id), and the film table (to get the film title). 
   These tables are related through shared ID columns rental links to inventory via inventory_id, and inventory 
   links to film via film_id.
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;