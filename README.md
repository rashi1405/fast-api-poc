# 📦 FastAPI + S3 Multipart Upload (POC)

This is a **FastAPI backend POC** for uploading large files (e.g. videos) directly from a React frontend to **Amazon S3** using **multipart upload with presigned URLs**.

---

## 🔹 Flow

1. **Frontend** splits file into chunks.
2. **Backend (FastAPI)** provides:

   * `initiate-upload/` → get `uploadId`
   * `generate-presigned-url/` → get chunk upload URL
   * `complete-upload/` → finalize upload
   * `download/{filename}` → Download the result file
3. **Frontend** uploads chunks directly to S3 using presigned URLs.
4. Backend returns final **file URL**. ✅

---


# 1. Clone repo
git clone <your-repo-url>
cd backend

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run FastAPI server
uvicorn app_server:app --reload --host 0.0.0.0 --port 8000


Docs available at 👉 `http://localhost:8000/docs`

---
