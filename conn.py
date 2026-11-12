class DBConnection:
    """Holds the parameters needed to connect to a database."""

    def __init__(self, hostname, port, user, password):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.password = password

    def show_parameters(self):
        print("Connection parameters:")
        print(f"  Hostname: {self.hostname}")
        print(f"  Port:     {self.port}")
        print(f"  User:     {self.user}")
        print(f"  Password: {'*' * len(self.password)}")


if __name__ == "__main__":
    conn = DBConnection(
        hostname="localhost",
        port=5432,
        user="user",
        password="password",
    )
    conn.show_parameters()
