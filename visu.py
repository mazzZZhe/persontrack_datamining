from readdata import parsefile
import argparse

class Draw:
	def __init__(self,filename,interval_time,numofcamera,posofcameras):
		self.list = parsefile(filename)
		#[time0,time2,...]
		self.statelist = []
		#interval time
		self.interval_time = interval_time
		#pos
		self.posofcameras = posofcameras
		self.numofcamera = numofcamera
	def parse_frame_list(self,frame):

		#output:the STATE of this frame
		#{'camera':str,'pos':[],'frame':int,'numofpeople':int}
		#total state{'c1':camera_state,'c2':camera_state,...}
		total_state = {}
		for i in range(self.numofcamera):
			camera_state = {'camera':"",'pos':[],'frame' : frame,'numofpeople' : 0}
			camera_state['camera'] = 'c'+str(i)
			camera_state['pos'] = self.posofcameras[i]
			total_state['c'+str(i)] = camera_state

		for i in range(self.numofcamera):
			print(total_state['c'+str(i)])
		print('-------------------------------------')
		for person_state in self.list:
			#['p1', ['c1', 's1', 15, 55], ['c2', 's1', 80, 2000], ['c5', 's1', 2300, 2400], ['c4', 's1', 2600, 3800], ['c6', 's1', 3200, 3500]]
			for cameraNo in range(1,len(person_state)):
				person_camera_state = person_state[cameraNo]
				start = person_camera_state[2]
				finish = person_camera_state[3]
				if start < frame and finish > frame:
					total_state[person_camera_state[0]]['numofpeople'] += 1
					break
		for i in range(self.numofcamera):
			print(total_state['c'+str(i)])
		

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--frame',help = 'current frame',type = int,default = 30)
	args = parser.parse_args()
	frame = args.frame
	d = Draw('swdata.txt',40,6,[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]])
	d.parse_frame_list(frame)
