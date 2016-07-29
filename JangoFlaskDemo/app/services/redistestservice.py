import  redis
# client = redis.Redis()  #defual host is localhost default port is 6379
client = redis.Redis(host='localhost', port=6379, db=0)


def get_by_key(key):
    item = client.get(key)
    return item

def set_by_key(key, val):
    item = get_by_key(key)
    if item is not None:
        client.delete(key)
    client.set(key, val)


    # pipeline操作
    # 管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器 - 客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。
    #
    # >> > p = r.pipeline() - -创建一个管道
    # >> > p.set('hello', 'redis')
    # >> > p.sadd('faz', 'baz')
    # >> > p.incr('num')
    # >> > p.execute()
    # [True, 1, 1]
    # >> > r.get('hello')
    # 'redis'
    #
    # >> > p = r.pipeline() - -创建一个管道
    # >> > p.set('hello', 'redis')
    # >> > p.sadd('faz', 'baz')
    # >> > p.incr('num')
    # >> > p.execute()
    # [True, 1, 1]
    # >> > r.get('hello')
    # 'redis'
    # 管道的命令可以写在一起，如：
    #
    # >> > p.set('hello', 'redis').sadd('faz', 'baz').incr('num').execute()
    # 1
    # >> > p.set('hello', 'redis').sadd('faz', 'baz').incr('num').execute()
    # 默认的情况下，管道里执行的命令可以保证执行的原子性，执行pipe = r.pipeline(transaction=False)
    # 可以禁用这一特性。