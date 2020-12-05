#-*- coding: utf-8 -*-
# medicines 테이블에 관련된 쿼리문 작성하는 파일
from flask import request, jsonify, redirect
from flask_restx import Resource, fields, marshal
from sqlalchemy import and_
import json
import jwt
from datetime import time
from operator import itemgetter
from app.main import db
from app.main.model.schedules_common import Schedules_common
from app.main.model.users import Users
from ..config import jwt_key, jwt_alg

def post_schedules_common(data):
  """ Post Common information of alarm"""
  try:
    token = request.headers.get('Authorization')
    decoded_token = jwt.decode(token, jwt_key, jwt_alg)
    user_id = decoded_token['id']

    if decoded_token:
      new_schedules_common = Schedules_common(
        title=data['title'], 
        memo=data['memo'],
        startdate=data['startdate'],
        enddate=data['enddate'],
        cycle=data['cycle'],
        user_id=user_id,
        )
      db.session.add(new_schedules_common)
      db.session.commit() 
      
      results = {
        "new_schedules_common_id": new_schedules_common.id,
        "time": data['time']
      }
      response_object = {
        'status': 'OK',
        'message': 'Successfully get monthly checked.',
        'results': results
      }
      return response_object, 200
    else:
      response_object = {
        'status': 'fail',
        'message': 'Provide a valid auth token.',
      }
      return response_object, 401
      
  except Exception as e:
      response_object = {
        'status': 'Internal Server Error',
        'message': 'Some Internal Server Error occurred.',
      }
      return response_object, 500
