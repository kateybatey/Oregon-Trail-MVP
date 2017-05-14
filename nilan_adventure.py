print '\n    You May:'
print '    1 - Travel the trail '
print '    2 - End'
print '\n  '

choice = int(raw_input('What is your choice: '))

if choice == 1:
	print "\n"
	print "Let's get started!"
	print 'Try taking a journey by covered wagon across 200 miles of plains,rivers,and mountains.'
	print 'Try! On the plains, will you slosh your oxen through mud and water-filled ruts or will you plod through dust six inches deep?'
	print 'How will you cross the rivers? If you have money, you might take a ferry. Or you can ford the river and hope you and your wagon are not swallowed alive!'
	print 'What about supplies? Well, if you are low on food you can hunt. You might get a buffalo...you might. And there are bear in the mountains.'
	print 'If for some reason you do not survive -- your wagon burns, or theives steal your oxen, or you run out of provisions, or you die of cholera  -- do not give up! Try again..and again...'
	print "\n"

	username = raw_input("Now that you've learned about the journey, What's your name? : ")

	print "Many different kinds of people traveled the trail, %s" % (username)
	print "\n"
	print "Let's get you into character!:"
	print "\n"
	print "If you would like to be a banker from Boston, choose '1'."
	print "If you would like to be a carpenter from Ohio, choose '2'."

	character = int(raw_input("Who would you like to be?: "))

	if character == 1: 
		print " %s you are a banker from Boston with $1600." % (username)
		print " It is 1848. Your jumping off place for Oregon is Independence, Missouri. Your journey begins in March."
		print " Before leaving Independence you should buy equipment and supplies. You have $1600 in cash."
		print "\n"
		print " But you don't have to spend it all now."
		print "\n"
		print " You can buy whatever you need at Matt's general store."
		print "\n"
		print " If you would like to buy oxen, choose '1'."
		print " If you would like to buy food, choose '2'."
		print " If you would like to skip supplies and start traveling, choose '3'."

		supplies = int(raw_input("> "))

		if supplies == 1 or supplies == 2 or supplies == 3:
			print "Well %s you're ready to start. Good luck! You have a long and difficult journey ahead of you." % (username)
			print"\n"

		print "You are now at the Kansas River crossing."
		print "You must cross the river in order to continue."
		print "The river is currently 643 feet across, and 6.9 feet deep in the middle."
		print "You may:"
		print "\n"
		print '1. Pay for a ferry across the river.'
		print '2. Ford the river'
		print "What is your choice?:"

		river_choice = int(raw_input("> "))

		if river_choice == 1:
			print "The ferry got your party and your wagon safely across the river!" 
			print "\n"
		elif river_choice == 2:
			print "You drown %s! Game over!!" % (username)

		print " You've arrived at Fort Kearny %s" % (username)
		print " Would you like to look around?"
		print " Choose 1 for yes"
		print " Choose 2 for no"
		print " What is your choice?:"

		fort_kearny = int(raw_input("> "))

		if fort_kearny == 1:
			print "Beth has cholera, and your wagon gets sick. Game over!"

		elif fort_kearny == 2:
			print " You have died of dysentary." 

	elif character == 2: 
		print " %s you have died of Dysentary." % (username)

elif choice == 2:
	print "You have died of dysentary. Bye!"

		

	







