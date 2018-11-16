from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#SIGNUP VIEW
def signup(request):
	print('test111')

	if request.method == "POST":
		print('test')
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if (username):
			user = User.objects.create_user(username, email, password)
			# user.first_name = firstname
			user.save()
			print('success')
			return render(request, "registration/success.html")
		else:
			error = True
			print('regex fail')
			return render(request, 'registration/signup.html', {'error':error})
	else:
		return render(request, 'registration/signup.html')


def index(request):
	# user = ScrumyUser.objects.get(id=2)
	# userGoal = user.scrumygoals_set.filter(scrumy_status=1)
	# context ={
	# 		'user': user,
	# 		'userGoal': userGoal			
	# 		}	
	return render(request, 'gnu/index.html')

