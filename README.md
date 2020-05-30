Steps to execute project:

python3 CreateDb.py
python3 app.py

Description :

CreateDb.py : 
File to create in memeory database(sqllite3) in python.

app.py :  
	1. It is a main file to handle post call to post story with attribute detail as a form-data and image/video . On the post call it will call function of Compress.py to compress image/video.
	It will insert data of story into database and for image type , creates foler with StoryID(1,2...) on the device having Original image/ Origianl Video and Cropped Image/Cropped Video.
	
	2. Get call to get all stories sorted by date(newset uploaded story came on top).
	
	3. Get Call to get compressed image/Compressed video uploaded by user.
	
Compress.py
This file comprises of two functions : one to resize image of size 1200px(height),600px(width) . One to reduce video size of max 480p.

*Postman Collections are attached to demo how to make a rest Call : 

POST http://localhost:8080/CreateStory 
i/p Select form-data in body ( add required attributes ,to send image (type = image , image(key) and select value as image .jpeg),to send video(type = video , video(key) and select value as video .mp4))
o/p message : story created successfully with storyid(use this story id to get image/video)

GET http://localhost:8080/stories
It will give all stories with latest first.

GET http://localhost:8080/stories/{StoryId : created at POST call}
o/p compressed image / video

*TestDb.db 
Attached db file to look on the table structure and attributes for creating story.

Sample  Result 

On POST call : folder 1 created with Original jpeg and compressed jpeg 
On GET call :  return compressed jpeg.

*USed module : flask to create REST aPI , moviepy for video compression , pillow for image compression






