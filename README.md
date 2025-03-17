# Image Generator API

A lightweight FastAPI backend that generates images from a given prompt using [Pollinations AI](https://image.pollinations.ai/). The images are streamed directly to the client without being stored on the server.

## 🚀 Features
- Generates AI images on demand.
- No image storage—streams directly from the source.
- Fast and efficient with FastAPI.

## 🔧 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/image-generator-api.git
   cd image-generator-api
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn httpx
   ```
3. Run the server:
   ```sh
   uvicorn server:app --host 0.0.0.0 --port 8000 --reload
   ```

## 📡 Usage
Send a `GET` request to generate an image:

```http
GET http://127.0.0.1:8000/generate-image/?prompt=A+cyberpunk+cityscape
```

### Example Response
- **Content-Type:** `image/jpeg` or `image/png`
- **Body:** The requested image.

## 📜 License
This project is licensed under the MIT License.

---

💡 **Contributions are welcome!** Feel free to fork the repo and submit pull requests.
