class RoleBasedAccessControl:
    def __init__(self):
        self.roles = {
            "admin": ["create", "edit", "delete", "view"],
            "editor": ["edit", "view"],
            "viewer": ["view"]
        }
        self.users = {}

    def add_user(self):
        """Allow users to add their names and assign roles automatically with permissions."""
        username = input("Enter username: ").strip()
        print(f"Available roles: {', '.join(self.roles.keys())}")
        role = input(f"Enter role for {username} (admin/editor/viewer): ").strip().lower()

        if role in self.roles:
            self.users[username] = role
            print(f"✅ User '{username}' added as '{role}'.")
            print(f"🔹 Permissions: {', '.join(self.roles[role])}")
        else:
            print("❌ Invalid role! Please choose from admin, editor, or viewer.")

    def check_access(self):
        """Check if a user has permission for an action."""
        username = input("Enter username: ").strip()
        permission = input("Enter permission (create/edit/delete/view): ").strip().lower()

        role = self.users.get(username)
        if role and permission in self.roles[role]:
            print(f"✅ Access granted for {username} to {permission}.")
        else:
            print(f"❌ Access denied for {username} to {permission}.")

# Menu-based system
rbac = RoleBasedAccessControl()

while True:
    print("\n1. Add User")
    print("2. Check Access")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        rbac.add_user()
    elif choice == "2":
        rbac.check_access()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice. Please try again.")
