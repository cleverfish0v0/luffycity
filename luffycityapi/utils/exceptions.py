from rest_framework.views import exception_handler
from django.db import DatabaseError
from redis import RedisError
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger('django')

def custom_exception_handler(exc, context):
    """
    自定义异常处理工具函数
    :param exc: 异常类
    :param context: 抛出异常的执行上下文
    :return: Response响应对象
    """
    # 先调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)

    if response is None:
        view = context['view']
        # 判断是否发生了数据库异常
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error('mysql数据库异常！[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        elif isinstance(exc, RedisError):
            logger.error('redis数据库异常！[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        elif isinstance(exc, ZeroDivisionError):
            response = Response({'message': '0不能作为除数！'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response