# FastAPI Web Push API 🚀

Welcome to the FastAPI Web Push API repository! This project showcases a powerful API built using Python and the FastAPI framework, specifically designed to streamline web push notification integration. Stay connected with your users in real-time and deliver timely updates with ease.

Demo: <a href="https://web-push.mehdiabdi.com" target="_blank">Web Push Demo</a>

## Key Features:

- Seamless Python integration
- Leveraging the efficiency of the FastAPI framework
- Effortless web push notification implementation
- Auto-generated Swagger UI for interactive API documentation with OpenAPI 3 specification.

Get started with enhancing your user engagement today! Feel free to explore the codebase, contribute, and customize the API to suit your notification needs.

## 🔧 Installation and Usage:

1. Clone the repository
```bash
git clone https://github.com/m-abdi/web-push-python
```
2. Install dependencies 
```bash
pip install -r requirements.txt
```

3. Run the API 
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
3. Visit https://localhost:8000 to send notifications to client

4. There is a Swagger UI for interactive with api in http://localhost:8000/docs

## 🚀 Proudction Considerations

- For production use, replace the contents of “private_key.pem” and “public_key.pem”files with some other keys. You can use [this service](https://vapidkeys.com) to generate random keys for you. Also, set the “SUBJECT” environment variable to something like “mailto: m.abdi.public@gmail.com”

- Sending bulk messages is handled by BackgroundTasks from FastAPI, which is based on the BackgroundTask object in starlette. Although it works nicely, it is not fast enough for a lot of messages. Celery can be a good option for that.


## 🤝 Contributions:
Contributions, issues, and feature requests are welcome! Create a pull request to collaborate with us on advancing this project further.

## 📄 License:
This project is licensed under the MIT license.