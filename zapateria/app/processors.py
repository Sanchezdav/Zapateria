
def get_avatar(request):
	user = request.user
	avatar = user.avatar
	return dict(avatar=avatar)