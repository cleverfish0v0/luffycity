# from django.test import TestCase
#
# # Create your tests here.
# from django.shortcuts import render
#
# # Create your views here.
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django_redis import get_redis_connection
# # 对日志调用
# import logging
# # seting logger set
# logger = logging.getLogger("django")
#
#
# # Create your views here.
# class HomeAPIView(APIView):
#     def get(self, request):
#         """测试代码，测试完成以后将来可以删除"""
#         # 测试日志功能
#         logger.debug("debug信息")
#         logger.info("info信息")
#         redis = get_redis_connection("sms_code")
#         print(1)
#         brother = redis.lrange("brother", 0, -1)
#         # brother = {'longbatian': 111}
#         return Response(brother, status.HTTP_200_OK)