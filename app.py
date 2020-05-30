import io
import base64
import os
import sqlite3
from flask import jsonify
from flask import Flask
from flask import flash, request
from flask import send_file
from PIL import Image
from Compress import compressVideo
from Compress import compressImg
import json 

app = Flask(__name__)	

@app.route('/CreateStory', methods=['POST'])
def add_emp():
	_json = request.form
	_name = _json['name']
	_description = _json['description']
	_duration = _json['duration']
	_type = _json['type']
	_latitude = _json['latitiude']
	_longitude = _json['longitude']
	
	sqlQuery = "INSERT INTO Stories(name,description,duration,type,latitude,longitude) VALUES(?,?,?,?,?,?)"
	bindData = (_name, _description, _duration, _type, _latitude, _longitude)
	conn = sqlite3.connect('TestDB.db')
	cursor = conn.cursor()
	cursor.execute(sqlQuery, bindData)
	storyID = cursor.lastrowid
	storyID = str(storyID)
	conn.commit()
	
	folder = storyID
	parent_dir = "."
	path = os.path.join(parent_dir, folder)
	if not os.path.exists(path):
		os.mkdir(path)
	print(path)
	
	if _type == 'video':
		picture = request.files.get('video')
		output = open(path+"/Original.mp4","wb")
		output.write(picture.read())
		compressVideo(storyID ,path+"/Original.mp4")
		output.close()
		
	
	if _type == 'image' : 
		picture = request.files.get('image')
		output = open(path+"/Original.jpeg","wb")
		output.write(picture.read())
		compressImg(storyID, path+"/Original.jpeg")
		output.close()
		
	respone = jsonify({"storyID":storyID, "msg": "Story added successfully!"})
	respone.status_code = 200
	cursor.close() 
	conn.close()
	return respone
		
@app.route('/stories')
def getAllStories():
	try:
		
		conn = sqlite3.connect('TestDB.db')
		cursor = conn.cursor()
		cursor.execute("SELECT StoryId, name,description,duration,type,latitude,longitude,timestamp FROM Stories order by timestamp DESC")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
	
		
@app.route('/stories/<StoryId>')
def getStory(StoryId):

	conn = sqlite3.connect('TestDB.db')
	cursor = conn.cursor()
	cursor.execute("SELECT type FROM Stories where StoryId=?",[int(StoryId)])
	print(int(StoryId))
	details = cursor.fetchall()
	detail = details[0]
	print(detail)
	
	if detail[0] == 'video':
		filename = StoryId+'/Compressed.mp4'
		return send_file(filename, mimetype='video/mp4')
		
	if detail[0] == 'image' :
		filename = StoryId+'/Compressed.jpeg'
		return send_file(filename, mimetype='image/jpeg')
	    	
	#respone = json_object
	#respone.status_code = 200
	cursor.close() 
	conn.close()
	#return respone
		 
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
