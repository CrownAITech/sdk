from deployment.server import start_server
from utils.logger import log_info

if __name__ == "__main__":
    log_info("Initializing Crown AI...")
    start_server()
