from flask import request, redirect, jsonify, make_response
from flask_restx import Resource
from ..util.dto import MedicineDto
import requests
from ..service.medicines import post_medicine, post_schedules_common_medicines, upload_medicine , get_schedules_common_medicines

api = MedicineDto.api
# _medicines = MedicineDto.medicines

@api.route('')
class PostMedicine(Resource):
  def post(self):
    """Post Medicine API"""
    data = request.get_json().get('medicine') 
    return post_medicine(data)

@api.route('/upload')
class UploadMedicine(Resource):
  def post(self):
    """Post Medicine API"""
    print("request: ", request.files)
    if 'image' not in request.files:
      print('No File Part')
    file = request.files['image']
    if file.filename == '':
      print('No Selected File')
    elif file and file.filename:
      filename = secure_filename(file.filename)
      filestr = request.files['image'].read()
      print('file:',file)
      print('filename:',filename)
      print('type:',file.content_type)
      #print('filestr:',filestr)
      return upload_medicine(file)


@api.route('/schedules-medicines')
class SchedulesCommonMedicines(Resource):
  def get(self):
    """Get Clicked day Medicines Through Schedules-medicines API"""
    data = request.args.to_dict()
    return get_schedules_common_medicines(data)

  def post(self):
    """Post Schedules Common Medicines API"""
    data = request.get_json().get('schedules_common_medicines')
    return post_schedules_common_medicines(data)

