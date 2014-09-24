#!/usr/bin/env python
import os, sys, datetime, math, itertools, urllib2, json

title='''
          _ __  _____ __  _ 
   ____ _(_) /_/ __(_) /_(_)
  / __ `/ / __/ /_/ / __/ / 
 / /_/ / / /_/ __/ / /_/ /  
 \__, /_/\__/_/ /_/\__/_/   
/____/ 
'''

kitty=[
[0,0,0,4,0,0,0,0,4,0,0,0],
[0,0,4,2,4,4,4,4,2,4,0,0],
[0,0,4,2,2,2,2,2,2,4,0,0],
[2,2,4,2,4,2,2,4,2,4,2,2],
[0,0,4,2,2,3,3,2,2,4,0,0],
[2,2,4,2,2,2,2,2,2,4,2,2],
[0,0,0,3,4,4,4,4,3,0,0,0]]

creeper=[
[2,1,1,2,1,1,1,2],
[1,4,4,1,1,4,4,1],
[2,4,4,1,2,4,4,1],
[1,1,1,4,4,1,2,1],
[1,2,4,4,4,4,1,1],
[1,1,4,4,4,4,2,2],
[2,1,3,1,1,3,1,2]]

oneup=[
[0,4,4,4,4,4,4,4,0],
[4,3,2,2,1,2,2,3,4],
[4,2,2,1,1,1,2,2,4],
[4,3,4,4,4,4,4,3,4],
[4,4,1,4,1,4,1,4,4],
[0,4,1,1,1,1,1,4,0],
[0,0,4,4,4,4,4,0,0]]

oneup2=[
[0,0,4,4,4,4,4,4,4,0,0],
[0,4,2,2,1,1,1,2,2,4,0],
[4,3,2,2,1,1,1,2,2,3,4],
[4,3,3,4,4,4,4,4,3,3,4],
[0,4,4,1,4,1,4,1,4,4,0],
[0,0,4,1,1,1,1,1,4,0,0],
[0,0,0,4,4,4,4,4,0,0,0]]

hackerschool=[
[4,4,4,4,4,4],
[4,3,3,3,3,4],
[4,1,3,3,1,4],
[4,3,3,3,3,4],
[4,4,4,4,4,4],
[0,0,4,4,0,0],
[4,4,4,4,4,4]]

octocat=[
[0,0,0,4,0,0,0,4,0],
[0,0,4,4,4,4,4,4,4],
[0,0,4,1,3,3,3,1,4],
[4,0,3,4,3,3,3,4,3],
[0,4,0,0,4,4,4,0,0],
[0,0,4,4,4,4,4,4,4],
[0,0,4,0,4,0,4,0,4]]

octocat2=[
[0,0,4,0,0,4,0],
[0,4,4,4,4,4,4],
[0,4,1,3,3,1,4],
[0,4,4,4,4,4,4],
[4,0,0,4,4,0,0],
[0,4,4,4,4,4,0],
[0,0,0,4,4,4,0]]

hello=[
[0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,4],
[0,2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,4],
[0,3,3,3,0,2,3,3,0,3,0,3,0,1,3,1,0,3],
[0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,3],
[0,3,0,3,0,3,3,3,0,3,0,3,0,3,0,3,0,2],
[0,2,0,2,0,2,0,0,0,2,0,2,0,2,0,2,0,0],
[0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,4]]

hireme=[
[1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[3,3,3,0,2,0,3,3,3,0,2,3,3,0,0,3,3,0,3,0,0,2,3,3],
[4,0,4,0,4,0,4,0,0,0,4,0,4,0,0,4,0,4,0,4,0,4,0,4],
[3,0,3,0,3,0,3,0,0,0,3,3,3,0,0,3,0,3,0,3,0,3,3,3],
[2,0,2,0,2,0,2,0,0,0,2,0,0,0,0,2,0,2,0,2,0,2,0,0],
[1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1]]

ascii_to_number = {
  '_': 0,
  '_': 1,
  '~': 2,
  '=': 3,
  '*': 4
}

def str_to_sprite(content):
  # Break out lines and filter any excess
  lines = content.split('\n')
  def is_empty_line(line):
    return len(line) != 0
  lines = filter(is_empty_line, lines)

  # Break up lines into each character
  split_lines = map(list, lines)

  # Replace each character with its numeric equivalent
  for line in split_lines:
    for index, char in enumerate(line):
      line[index] = ascii_to_number.get(char, 0)

  # Return the formatted str
  return split_lines

oneup_str = str_to_sprite("""
 ******* 
*=~~-~~=*
*~~---~~*
*=*****=*
**-*-*-**
 *-----* 
  *****  
""")

images={
'kitty':kitty,
'creeper':creeper,
'oneup':oneup,
'oneup2':oneup2,
'hackerschool':hackerschool,
'octocat':octocat,
'octocat2':octocat2,
'hello':hello,
'hireme':hireme,
'oneup_str':oneup_str
}

def load_images(imgNames):
	"""loads user images from given file(s)"""
	if imgNames[0]=='':
		return dict()
	for imageName in imgNames:
		img = open(imageName)
		loadedImgs = {}
		imgList = ''
		imgLine = ' '
		name = img.readline().replace('\n', '')
		name = name[1:]

		while True:
			imgLine = img.readline()
			if imgLine == '':
				break
			imgLine.replace('\n', '')
			if(imgLine[0] == ':'):
				loadedImgs[name] = json.loads(imgList)
				name = imgLine[1:]
				imgList = ''
			else:
				imgList += imgLine
	loadedImgs[name] = json.loads(imgList)
	return loadedImgs

def get_calendar(username):
	"""retrieves the github commit calendar data for a username"""
	BASEURL='https://github.com/'
	url = BASEURL + 'users/' + username + '/contributions_calendar_data'
	page = urllib2.urlopen(url)
	return json.load(page)

def max_commits(input):
	"""finds the highest number of commits in one day"""
	output = set()
	for i, j in enumerate(input):
		output.add(input[i][1])
	output = list(output)
	output.sort()
	output.reverse()
	return output[0]

def multiplier(max_commits):
	"""calculates a multiplier to scale github colors to commit history"""
	m = max_commits/4.0
	if m == 0: return 1
	m = math.ceil(m)
	m = int(m)
	return m

def get_start_date():
	'''returns a datetime object for the first sunday after one year ago today at 12:00 noon'''
	d = datetime.datetime.today()
	date = datetime.datetime(d.year-1, d.month, d.day, 12)
	weekday = datetime.datetime.weekday(date)
	while weekday < 6:
		date = date + datetime.timedelta(1)
		weekday = datetime.datetime.weekday(date)
	return date

def date_gen(start_date, offset=0):
	'''generator that returns the next date, requires a datetime object as input. The offset is in weeks'''
	start = offset * 7
	for i in itertools.count(start):
		yield start_date + datetime.timedelta(i)

def values_in_date_order(image, multiplier=1):
	height = 7
	width = len(image[0])
	for w in range(width):
		for h in range(height):
			yield image[h][w]*multiplier

def commit(content, commitdate):
	template = '''echo %s >> gitfiti\nGIT_AUTHOR_DATE=%s GIT_COMMITTER_DATE=%s git commit -a -m "gitfiti"\n''' 
	return template	% (content, commitdate.isoformat(), commitdate.isoformat())

def fake_it(image, start_date, username, repo, offset=0, multiplier=1):
	template = ('#!/bin/bash\n'
				'REPO=%s\n'
				'git init $REPO\n'
				'cd $REPO\n'
				'touch README.md\n'
				'git add README.md\n'
				'touch gitfiti\n'
				'git add gitfiti\n'
				'%s\n'
				'git remote add origin git@github.com:%s/$REPO.git\n'
				'git pull\n'
				'git push -u origin master\n')
	strings = []
	for value, date in zip(values_in_date_order(image, multiplier), date_gen(start_date, offset)):
		for i in range(value):
			strings.append(commit(i, date))
	return template % (repo, "".join(strings), username)

def save(output, filename):
	"""Saves the list to a given filename"""
	f = open(filename, "w")
	f.write(output)
	f.close()

def main():
	global images
	print title
	print 'Enter your github username:'
	username = raw_input(">")
	cal = get_calendar(username)
	m = multiplier(max_commits(cal))

	print 'Enter name of the repo to be used by gitfiti:'
	repo = raw_input(">")
	
	print 'Enter number of weeks to offset the image (from the left):'
	offset = raw_input(">")
	if offset == None: offset = 0
	else: offset = int(offset)

	print ('By default gitfiti.py matches the darkest pixel to the highest\n'
			'number of commits found in your github commit/activity calendar,\n'
			'\n'
			'Currently this is : %s commits\n'
			'\n'
			'Enter the word "gitfiti" to exceed your max\n'
			'(this option generates WAY more commits)\n'
			'Any other input will cause the default matching behavior') % (max_commits(cal),)
	match = raw_input(">")
	if match == "gitfiti": match = m
	else: match = 1

	print 'enter file(s) to load images from (blank if not applicable)'
	imgNames = raw_input(">").split(' ')
	images = dict(images, **load_images(imgNames))

	print 'enter the image name to gitfiti'
	print 'images: ' + ", ".join(images.keys())
	image = raw_input(">")
	if image == None: image = images['kitty']
	else:
		try: image = images[image]
		except: image = images['kitty']

	output = fake_it(image, get_start_date(), username, repo, offset, m*match)
	save(output, 'gitfiti.sh')
	print 'gitfiti.sh saved. Create a new(!) repo at: https://github.com/new and run it.'

if __name__=='__main__':
	main()
