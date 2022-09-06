from redis import Redis

class RedisService:
    """
    RedisService integrates with redis to act as K-V store , cache
    and distributed lock system to various operations
    """
    def __init__(self,url:str) -> None:
        self.client =  Redis(url)

    def get(self,key:str)->str:
        value =  self.client.get(key)
        return value.decode("utf-8") if value else None
    
    def set(self,key:str,value:str):
        self.client.set(key,value)

    def get_lock(self,key:str,ttl=1000,blocking=False):
        """
        Lock with key  with a ttl specified in seconds 
        """
        lock = self.client.lock(key,ttl)
        acquired = lock.acquire(blocking=blocking)
        return lock if acquired else None