# Serverless Transaction Processing Platform (AWS)

A high-performance, event-driven API platform built with Python and AWS Serverless. This system processes transactional requests with sub-second latency and includes full audit logging.

## 🚀 Architecture
- **API Gateway**: RESTful entry point.
- **AWS Lambda**: Core logic (Python 3.9).
- **DynamoDB**: High-speed transaction state storage.
- **S3 Bucket**: Audit trail for raw transaction payloads.
- **CloudWatch**: Operational dashboards and DLQ monitoring.



## 🛠 Prerequisites
Before you begin, ensure you have:
1. An **AWS Account**.
2. **AWS CLI** configured (`aws configure`).
3. **AWS SAM CLI** installed.
4. **Python 3.9** installed.

## 📦 Deployment

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/transaction-platform.git](https://github.com/YOUR_USERNAME/transaction-platform.git)
   cd transaction-platform

2. **Build the application:**

   ```bash
   sam build

3. **Deploy to AWS:**

   ```bash
   sam deploy --guided

Follow the prompts. For the first deploy, accept the default suggestions.

## 🧪 Testing the API
Once deployed, SAM will output an ApiUrl. Use the following curl command to test:

  ```bash
  curl -X POST <YOUR_API_URL>/process \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user_123", "amount": 99.99}'