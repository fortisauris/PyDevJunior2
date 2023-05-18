# redis_variables.md


## Strings
SET user:1 Andrej
SET user:2 Jozef
GET

SET info:23 "\"{'username': "jonas", 'id':453734}\"" EX 100

INCRBY /

LIMIT = NAJVIAC 512MB

## LISTS

LPUSH / RPUSH
RPOP / LPOP

LLEN

LIMIT 4miliardy clenov

## SETS

SADD
SREM 
SISMEMBER  1 True 0 False
SINTER


# HASHES

HSET key VALUES
HGET key VALUE
HGETALL key

HINCRBY

# SORTED SETS
ZADD key VALUES
ZRANGE 

# STREAMS
XADD key VALUES

XREAD 
XRANGE
XLEN

# GEOSPATIAL

GEOADD
GEOSEARCH

# HYPERLOG

#BITMAPS  -- uklada statusove bity

SETBIT
GETBIT
BITOP bitwise opfr