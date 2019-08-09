import random
from PIL import Image
import time


score_mag_as = 0
score_mag_bsk = 0
score_mag_bs = 0
score_mag_fsk = 0
score_mag_fs = 0
score_mag_vb = 0

score_interesse_as = 0
score_interesse_bs = 0
score_interesse_bsk = 0
score_interesse_fsk = 0
score_interesse_fs = 0
score_interesse_vb = 0

totalDuration=0

def rotateImages():
	angles = [0,90,180,270]
	fileNames = pool.files()
	for fileName in fileNames:
		path = getFilePath(fileName)
		angle = random.choice(angles)
		image = Image.open(path)
		newImage = image.rotate(angle)
		newImage.save(path)
		print("%s rotate %s degrees" %(fileName, angle))

def showExperiment(fileName,canvas):
	global totalDuration
	
	startTime = time.time()
	print("fileName: " + fileName)
	showPic(fileName,canvas)
	showMagChoiceQuestion(fileName)
	showInteressiertChoiceQuestion(fileName)
	endTime = time.time()
	duration = endTime - startTime
	print("duration: "+str(duration))
	totalDuration = totalDuration + duration
	
def showPic(fileName,canvas):
	canvas.image(getFilePath(fileName), center=True, x=20, y=-120, scale=0.7, rotation=None)
	canvas.show()
	clock.sleep(1000)
	canvas.clear()
	
def showMagChoiceQuestion(fileName):
	form = buildForm(fileName, "Wie <b><i>gefällt</i></b> Ihnen dieses Muster")
	rating_scale = RatingScale(
	nodes=["überhaupt nicht 1","2", "3", "4", "5", "6","7sehr gut"], click_accepts=True,
	orientation=u'horizontal', var='result')
	form.set_widget(rating_scale, (0, 2))
	
	form._exec()
	print("mag:" + str(self.get("result")))
	mag_score(fileName, self.get("result"))
	#sum_mag_score(fileName, self.get("result"))
	
def showInteressiertChoiceQuestion(fileName):
	form = buildForm(fileName, "Wie <b><i>interessant</i></b> finden Sie dieses Muster")
	rating_scale = RatingScale(
	nodes=["überhaupt nicht\ninteressant 1","2", "3", "4", "5", "6","7sehr interessant"], click_accepts=True,
	orientation=u'horizontal', var='result')
	form.set_widget(rating_scale, (0, 2))
	
	form._exec()
	print("interessiert:" + str(self.get("result")))
	#sum_interesse_score(fileName, self.get("result"))
	interesse_score(fileName, self.get("result"))
	
def buildForm(fileName, name):
	form = Form(
	cols=[1], rows=[4,1,1,1],
	margins=(150,10,50,50), spacing=30
	)
	image = ImageWidget(path=getFilePath(fileName), adjust=True, frame=False)
	form.set_widget(image, (0, 0))
	
	label = Label(name+"?")
	form.set_widget(label, (0, 1))
	return form
def mag_score(fileName, score):
#def sum_mag_score(fileName, score):
	global score_mag_as
	global score_mag_bsk
	global score_mag_bs
	global score_mag_fsk
	global score_mag_fs
	global score_mag_vb
	
	if fileName.startswith("AS"):
		score_mag_as += score
	elif fileName.startswith("BSK"):
		score_mag_bsk += score
	elif fileName.startswith("BS"):
		score_mag_bs += score
	elif fileName.startswith("FSK"):
		score_mag_fsk += score
	elif fileName.startswith("FS"):
		score_mag_fs += score
	elif fileName.startswith("VB"):
		score_mag_vb += score

#def sum_interesse_score(fileName, score):
def interesse_score(fileName, score):
	global score_interesse_as
	global score_interesse_bsk
	global score_interesse_bs
	global score_interesse_fsk
	global score_interesse_fs
	global score_interesse_vb
	
	if fileName.startswith("AS"):
		score_interesse_as += score
	elif fileName.startswith("BSK"):
		score_interesse_bsk += score
	elif fileName.startswith("BS"):
		score_interesse_bs += score
	elif fileName.startswith("FSK"):
		score_interesse_fsk += score
	elif fileName.startswith("FS"):
		score_interesse_fs += score	
	elif fileName.startswith("VB"):
		score_interesse_vb += score	

def buildLog():
#	self.log("score_mag_as," + str(score_mag_as))
#	self.log("score_mag_bs," + str(score_mag_bs))
#	self.log("score_mag_bsk," + str(score_mag_bsk))
#	self.log("score_mag_fs," + str(score_mag_fs))
#	self.log("score_mag_fsk," + str(score_mag_fsk))
#	self.log("score_mag_vb," + str(score_mag_vb))
#	
#	self.log("score_interesse_as," + str(score_interesse_as))
#	self.log("score_interesse_bs," + str(score_interesse_bs))
#	self.log("score_interesse_bsk," + str(score_interesse_bsk))
#	self.log("score_aktiv_fs," + str(score_aktiv_fs))
#	self.log("score_aktiv_fsk," + str(score_aktiv_fsk))
#	self.log("score_aktiv_vb," + str(score_aktiv_vb))

	self.log("subject_panasB_neg,subject_panasB_pos,score_mag_as,score_mag_bs,score_mag_bsk,score_mag_fs,score_mag_fsk,score_mag_vb,score_interesse_as,score_interesse_bs,score_interesse_bsk,score_interesse_fs,score_interesse_fsk,score_interesse_vb,total_duration")
	self.log(str(exp.subject_panasB_neg)+","+str(exp.subject_panasB_pos)+","+str(score_mag_as)+","+str(score_mag_bs)+","+str(score_mag_bsk)+","+str(score_mag_fs)+","+str(score_mag_fsk)+","+str(score_mag_vb)+","+str(score_interesse_as)+","+str(score_interesse_bs)+","+str(score_interesse_bsk)+","+str(score_interesse_fs)+","+str(score_interesse_fsk)+","+str(score_interesse_vb)+","+str(totalDuration))
	
def start():
	canvas = Canvas()
	fileNames = pool.files()
	random.shuffle(fileNames)
	
	rotateImages()
	
	for fileName in fileNames:
		showExperiment(fileName,canvas)
		
	buildLog()
	
def getFilePath(fileName):
	return exp.pool[fileName]
		
start()
