from django.core.cache import caches


# cache_kwargs:key_prefix,key_param,expire(s),cache(where)
def cache_check(**cache_kwargs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):
            CACHE = caches['default']
            if 'cache' in cache_kwargs:
                CACHE = caches[cache_kwargs['cache']]
            key_prefix = cache_kwargs['key_prefix']
            key_param = cache_kwargs['key_param']
            expire = cache_kwargs.get('expire', 30)
            # 获取视图传参中的指定参数
            cache_key = key_prefix + kwargs[key_param]
            print('----cache key id %s' % (cache_key))
            res = CACHE.get(cache_key)
            if res:
                print('return %s cache' % (cache_key))
                return res
            # 没有缓存
            res = func(self, request, *args, **kwargs)
            CACHE.set(cache_key, res, expire)
            return res
        return wrapper
    return _cache_check
