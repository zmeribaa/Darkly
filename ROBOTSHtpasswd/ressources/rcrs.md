# Using `robots.txt` to Find Hidden Directories and Retrieve a Flag

## Step 1: Discovering Hidden Directory
The target website had a `robots.txt` file, which listed disallowed directories. One such directory was: /whatever


## Step 2: Accessing Sensitive File
Inside `/whatever`, we found a file named `.htpasswd` containing: root:437394baff5aa33daa618be47b75cb49


This is a hashed password for the `root` user.

## Step 3: Decrypting the Password
We decrypted the hash and found the password: qwerty123@


## Step 4: Logging into Admin Panel
We then visited the admin panel at: /admin

Using the credentials:

- **Username:** root  
- **Password:** qwerty123@

This successfully gave us access and revealed the **flag**.

## Explanation
The attack exploited information disclosure through `robots.txt` and weak password protection. By checking hidden directories and decrypting credentials, we could access the admin panel and retrieve the flag.
