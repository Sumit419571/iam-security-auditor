# 🔐 IAM Security Auditor

> Automated AWS IAM security auditing tool that detects 
> misconfigurations and security risks across your AWS account  
> reducing manual security review time from hours to seconds.

---

## 🚨 The Problem

In any AWS environment, IAM misconfigurations are one of the 
biggest security risks:
- Developers forget to enable MFA
- Old access keys never get rotated
- Users accumulate admin privileges over time

Manually checking each user in the AWS console is slow, 
error-prone, and doesn't scale.

## ✅ The Solution

This tool automatically scans your entire AWS account and 
instantly detects:

| Security Check | Description |
|---------------|-------------|
| 🔑 MFA Status | Detects users without Multi-Factor Authentication |
| 👑 Admin Access | Flags users with AdministratorAccess policy |
| 🗝️ Old Access Keys | Identifies access keys older than 90 days |
| 🕐 Last Login | Shows last login time for each user |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **AWS SDK:** boto3
- **AWS Service:** IAM

---

## 📊 Sample Output
```
🔐 IAM Security Audit Report
==================================================
👤 User: john.doe
   MFA Enabled : NO ⚠️
   Admin Access: YES ⚠️
   Old Keys    : ['AKIAIOSFODNN7EXAMPLE']
   Last Login  : 2025-11-25 12:19:13+00:00

👤 User: jane.smith
   MFA Enabled : YES ✅
   Admin Access: No ✅
   Old Keys    : None ✅
   Last Login  : 2026-03-01 09:45:00+00:00
==================================================
✅ Audit Complete!
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- AWS CLI installed and configured
- IAM user with read permissions

### Installation

1. Clone the repository
git clone https://github.com/Sumit419571/iam-security-auditor.git

2. Navigate to project folder
cd iam-security-auditor

3. Install dependencies
pip install boto3

4. Configure AWS credentials
aws configure

5. Run the tool
python auditor.py

---

## 📁 Project Structure
```
iam-security-auditor/
├── auditor.py      # Main script
├── .gitignore      # Ignores sensitive files
└── README.md       # Project documentation
```

---

## 🔒 Security

- No credentials are stored in the code
- Tool uses read-only IAM API calls
- AWS credentials managed via AWS CLI

---

## 💰 AWS Cost

100% Free — only uses IAM read-only API calls within AWS Free Tier

---

## 👨‍💻 Author

**Sumit Verma**