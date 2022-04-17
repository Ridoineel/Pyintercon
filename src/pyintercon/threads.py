import threading

class ConnexionThread(threading.Thread):
	def __init__(self, con, clients_list):
		""" set thread with arguments con and clients_list
			con: is socket.socket of socket.socket

		"""

		super().__init__()
		self.con = con
		self.clients_list = clients_list

	def run(self):
		clients_list = self.clients_list
		con = self.con

		while True:
			# accept client
			client, param = con.accept()
			# set a client timeout for future operation
			# on this: -> server waiting for receved request
			client.settimeout(.5)


			clients_list.append((client, param))

			print(f"\t{param} is connected ...")

class ResponseThread(threading.Thread):
	def __init__(self, clients_list, handleResponse):
		""" set thread with arguments clients_list and handleResponse

		"""

		super().__init__()
		self.clients_list = clients_list
		self.handleResponse = handleResponse

	def run(self):
		clients_list = self.clients_list

		while True:
			for client, param in clients_list:
				try:
					# receive request datas
					req = client.recv(10**9).decode()
					assert req

				except AssertionError:
					clients_list.remove((client, param))
					print(f"\t{param} is disconnected !")
				except:
					continue
				else:
					rep = self.handleResponse(req)
					client.send(str(rep).encode())