import subprocess

def create_topic(topic_name):
    try:
        subprocess.run([  # this is the command to create a topic in kafka
            "docker", "exec", "kafka",
            "/usr/bin/kafka-topics",
            "--create", "--topic", topic_name,
            "--bootstrap-server", "kafka:9092",  # Correction : remplacement de localhost par kafka
            "--partitions", "1",
            "--replication-factor", "1"
        ], check=True)
        print(f"Topic '{topic_name}' is created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating topic '{topic_name}': {e}")

def produce_messages(topic_name):
    try:
        subprocess.run([  # this one is to produce messages to the topic
            "docker", "exec", "kafka",  # we remove "it" to avoid interactive mode but you can add it back if you use a specific terminal like bash or sh
            "/usr/bin/kafka-console-producer",
            "--topic", topic_name,
            "--bootstrap-server", "kafka:9092"  # Correction de l'adresse
        ], text=True, input="hi, Producer Neva in charge \n", check=True)
        print(f"Produced message to topic '{topic_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"there is an error while producing messages: {e}")

def consume_messages(topic_name):
    try:
        subprocess.run([  # and that last one is to consume messages from the topic
            "docker", "exec", "kafka",
            "/usr/bin/kafka-console-consumer",
            "--topic", topic_name,
            "--from-beginning",
            "--bootstrap-server", "kafka:9092"
        ])
    except subprocess.CalledProcessError as e:
        print(f"Error while consuming messages from this topic '{topic_name}': {e}")
