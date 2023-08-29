import subprocess
import redis_server


def install_redis_server(redis_version):
    try:
        subprocess.check_call(["pip", "install", f"redis-server=={redis_version}"])
        print(f"Redis server version {redis_version} installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Redis server.")
        exit(1)


def start_redis_server():
    try:
        redis_server_path = redis_server.REDIS_SERVER_PATH
        subprocess.Popen([redis_server_path])
        print("Redis server started successfully.")
    except Exception as e:
        print("Failed to start Redis server:", str(e))
        exit(1)


def main():
    redis_version = "6.0.9"
    install_redis_server(redis_version)
    start_redis_server()


if __name__ == "__main__":
    main()
