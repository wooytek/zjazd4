import requests
import json
import time

def fetch_weather_data(station_id: str):
    try:
        print(f"Pobieranie danych dla pary {station_id}...")

        response = requests.get(f"http://127.0.0.1:8000/currency/{station_id}")

        if response.status_code == 200:
            data = response.json()



            return data
        else:
            print(f"Błąd: {response.status_code}")
            # obsługa błędów
            return None
    except Exception as e:
        print(f"Błąd: {e}")
        # obsługa błędów
        return None

def start_consuming():
        try:
            with open('weather_data.csv', 'a') as f:
                if f.tell() == 0:
                    f.write("timestamp,  currency,  quote\n")
                while True:
                    # msg = self.consumer.poll(1.0)
                    #
                    # if msg is None:
                    #     continue
                    # if msg.error():
                    #     if msg.error().code() == KafkaError._PARTITION_EOF:
                    #         continue
                    #     else:
                    #         print(f"Błąd: {msg.error()}")
                    #         break
                    try:
                        data = fetch_weather_data("eurusd")
                        currency = data["currency"]
                        quote = data["quote"]
                        timestamp = data["timestamp"]
                        # print(f"Otrzymano zadanie dla stacji: {station_id}")

                        # weather_data = fetch_weather_data(station_id, False)
                        # if weather_data:
                        #     temperature = weather_data['currency']
                        #     quote = weather_data['quote']
                        #     timestamp = weather_data['timestamp']
                        #     print(f"Stacja {station_id} temperatura: {temperature:.2f}'C timestamp: {timestamp}")
                        f.write(f"{timestamp},{currency},{quote}\n")
                        f.flush()
                    except Exception as e:
                        print(f"Błąd przetwarzania wiadomości: {e}")
                    time.sleep(60)
        except Exception as e:
            print(f"Błąd konsumpcji: {e}")

if __name__ == "__main__":
    print(fetch_weather_data("eurusd"))
    # data = fetch_weather_data("eurusd")
    # print(data["quote"])
    start_consuming()