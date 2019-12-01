class User:
    
    def get_permission(self):
        if permission_dict().get('super_user'):
            return "Super user permission."
        else:
            return "Normal user permission."

def permission_dict():
    return 


