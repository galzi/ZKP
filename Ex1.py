from tkinter import Tk, Label, Button, Text, END
import random, hashlib

class AgeVerify:
	def __init__(self, master):
		self.master = master
		master.title('Age Verify - a Zero-Knowledge Proof Exercise')

		# Seed
		self.seedLabel = Label(master, text = 'Seed: ')
		self.seedLabel.grid(row = 0, column = 0)
		
		self.seed = Label(master, text = '')
		self.seed.grid(row = 0, column = 1)

		self.seedButton = Button(master, text = 'Recreate seed', command = self.seeding)
		self.seedButton.grid(row = 0, column = 2)

		# Actual age
		self.ageLabel = Label(master, text = 'Actual Age: ')
		self.ageLabel.grid(row = 1, column = 0)
		
		self.age = Text(master, height = 1, width = 3)
		self.age.grid(row = 1, column = 1)

		self.ageButton = Button(master, text = 'Create Proof', command = self.prove)
		self.ageButton.grid(row = 1, column = 2)
		
		self.proofLabel = Label(master, text = '')
		self.proofLabel.grid(row = 1, column = 3)
		
		# Actual age
		self.agePLabel = Label(master, text = 'Age to Proove: ')
		self.agePLabel.grid(row = 2, column = 0)
		
		self.ageP = Text(master, height = 1, width = 3)
		self.ageP.grid(row = 2, column = 1)

		self.agePButton = Button(master, text = 'Create Challenge', command = self.challenge)
		self.agePButton.grid(row = 2, column = 2)
		
		self.challengeLabel = Label(master, text = '')
		self.challengeLabel.grid(row = 2, column = 3)
		
		# Verify
		self.VerifyLabel = Button(master, text = 'Verify Challenge', command = self.verify)
		self.VerifyLabel.grid(row = 3, column = 0)
		
		self.verify = Label(master, text = '')
		self.verify.grid(row = 3, column = 1)
		
		self.result = Label(master, text = '')
		self.result.grid(row = 3, column = 2)
		
		# Exit
		self.close = Button(master, text = 'Exit', command = master.quit)
		self.close.grid(row = 4, column = 0)
		
		self.seeding()
		
	def seeding(self, zeros = 32, randoms = 32):
		self.seed['text'] = '0' * zeros + ''.join(random.choices(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'), k = randoms))

	def hashchain(self, seed, links):
		h = seed
		
		for i in range(links):
			h = hashlib.sha256(h.encode('utf-8')).hexdigest()
		return h

	def prove(self):
		self.proofLabel['text'] = self.hashchain(self.seed['text'], int(self.age.get("1.0", END)) + 1)

	def challenge(self):
		self.challengeLabel['text'] = self.hashchain(self.seed['text'], int(self.age.get("1.0", END)) + 1 - int(self.ageP.get("1.0", END)))

	def verify(self):
		self.verify['text'] = self.hashchain(self.challengeLabel['text'], int(self.ageP.get("1.0", END)))
		
		if self.proofLabel['text'] == self.verify['text']:
			self.result['text'] = 'VERIFIED!'
		else:
			self.result['text'] = 'FAILED!'

root = Tk()
my_gui = AgeVerify(root)
root.mainloop()