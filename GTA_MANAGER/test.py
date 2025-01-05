import redis

r = redis.Redis(host='localhost', port=6379, db=0)

try:
    r.ping()
    print("Redis is running!")
except redis.ConnectionError as e:
    print(f"Cannot connect to Redis: {e}")
