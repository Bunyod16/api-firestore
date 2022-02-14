sqlite3 whitelist.db <<EOF
.headers on 
.mode csv 
.output whitelist.csv 
SELECT * FROM whitelist;
EOF
