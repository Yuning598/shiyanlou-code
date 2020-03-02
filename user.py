from werkzeug import generate_password_hash, check_password_hash

class User:
	'''该类用于创建用户账号
	'''
	
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password_hash = self.save_password(password)
		
	def check_email(self, email):
		return self.email == email
		#判断邮箱
		
	def save_password(self, password):
		'''生成hash密码的方法
		'''
		return generate_password_hash(password)
		
	def check_password(self, password):
		'''检查hash密码的方法，返回布尔值
		'''
		return check_password_hash(self.password_hash,password)
		
def main():
	userList = []
	print('>>>>>>>欢迎<<<<<<<')
	while 1:
		choose = int(input('''
		请选择：
		1. 注册
		2. 登录
		3. 退出
		'''))
		if choose == 1:
			print('请输入：')
			name =  input('name:')
			email = input('email:')
			password = input('password:')
			newUser = User(name,email,password)
			userList.append(newUser)
		
		if choose == 2:
			print('请输入：')
			email = input('email:')
			password = input('password:')
			inList = False
			for user in userList:
				if user.check_email(email):
					inList = True
					if user.check_password(password):
						print('登录成功')
					else:
						print('用户名或密码错误')
					break
			if inList == False:
				print('请输入正确的email')
			
		if choose == 3:
			break
			
if __name__ == '__main__':
	main()
