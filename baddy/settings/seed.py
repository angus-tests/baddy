import os

# Should we seed ALL data (will override other seed settings)
SEED_ALL = os.getenv("SEED_ALL", "false").lower() == "true"

# Should we seed admin
SEED_ADMIN = os.getenv("SEED_ADMIN", "false").lower() == "true"

# Should we seed groups
SEED_GROUPS = os.getenv("SEED_GROUPS", "false").lower() == "true"

# If we are seeding admin we need the username, email and password
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
