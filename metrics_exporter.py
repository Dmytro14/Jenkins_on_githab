from prometheus_client import start_http_server, Gauge
import random
import time

# Ініціалізуємо метрики
emotion_metric = Gauge('emotion', 'Emotion detected', ['emotion'])
age_metric = Gauge('age', 'Age detected')
gender_metric = Gauge('gender', 'Gender detected', ['gender'])
smile_probability_metric = Gauge('smile_probability', 'Smile probability detected')

def generate_random_data():
    data = {
        "emotion": random.choice(["happy", "sad", "angry", "neutral"]),
        "age": random.randint(1, 100),
        "gender": random.choice(["male", "female"]),
        "smile_probability": round(random.uniform(0, 1), 2)
    }
    return data

if __name__ == "__main__":
    start_http_server(8001)  # Запуск HTTP-сервера на порту 8000

    try:
        while True:
            random_data = generate_random_data()

            # Оновлюємо метрики
            emotion_metric.labels(emotion=random_data['emotion']).set(1)
            age_metric.set(random_data['age'])
            gender_metric.labels(gender=random_data['gender']).set(1)
            smile_probability_metric.set(random_data['smile_probability'])

            print("Дані збережено: ", random_data)
            time.sleep(5)

    except KeyboardInterrupt:
        print("Програма завершена.")
