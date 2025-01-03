from kafka_tools import create_topic, produce_messages, consume_messages

def main():
    # Change this to your topic name before running the script
    topic_name = "CloudTopic" # i will dynamise this creating script to take in user input later
                              
    create_topic(topic_name)

    produce_messages(topic_name)

    consume_messages(topic_name)

if __name__ == "__main__":
    main()
