import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="demo_logs.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def login():
    logging.warning("login success")

def logout():
    logging.critical("log off success")

def cart():
    logging.info("Added to cart")
    
def cal():

    logging.debug("Sample")

login()
logout()
cart()
cal()
