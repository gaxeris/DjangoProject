def user_self_directory_path(instance, filename) -> str:
    """Is used to retrieve users model images directory path.
    Returns path string like: 'MEDIA_ROOT/user_<self.id>/<filename>'"""
    return "user_{0}/{1}".format(instance.id, filename)
