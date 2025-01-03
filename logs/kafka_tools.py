import logging

logging.basicConfig(
    filename="../logs/kafka.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Kafka tools are initialized, good job !!.")
