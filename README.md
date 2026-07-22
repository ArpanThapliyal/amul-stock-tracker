# 🥛 Amul Protein Buttermilk Stock Tracker

An automated stock monitoring bot that checks the availability of **Amul High Protein Buttermilk** and sends an instant email notification when the product comes back in stock.

## Why I Built This

I'm a regular consumer of **Amul High Protein Buttermilk**, but one recurring problem was that it was almost always **out of stock** on the official Amul website.

Whenever the product became available, it usually sold out quickly. Manually refreshing the website multiple times a day wasn't practical.

Instead of checking the website repeatedly, I decided to automate the entire process.

This project was built to solve a real problem I personally faced:
- Automatically check the product availability.
- Notify me immediately when the product is back in stock.
- Run continuously without requiring my computer to stay on.

---

# Features

- Checks stock availability automatically
- Uses Playwright for browser automation
- Sends email notifications instantly
- Runs automatically using GitHub Actions
- Prevents duplicate notifications using state tracking
- Secure credential management using GitHub Secrets
- Environment variable support

---

# Tech Stack

- Python
- Playwright
- GitHub Actions
- Gmail SMTP
- GitHub Secrets
- Python Dotenv

---

# How It Works

```
GitHub Actions
        │
        ▼
Launch Playwright
        │
        ▼
Open Amul Product Page
        │
        ▼
Enter Delivery Pincode
        │
        ▼
Check Stock Status
        │
        ▼
Compare with Previous State
        │
        ▼
If Stock Changed
        │
        ▼
Send Email Notification
```

---

# Project Structure

```
amul-stock-tracker/

├── .github/
│   └── workflows/

├── logs/

├── src/
│   ├── config.py
│   ├── main.py
│   ├── notifier.py
│   └── tracker.py

├── .env
├── requirements.txt
├── state.json
└── README.md
```

---

# Challenges Faced

Although the final application looks simple, several real-world challenges had to be solved.

### Browser Automation

The Amul website dynamically loads product information after entering a delivery pincode. Reliable automation required handling asynchronous page loading and dynamic elements.

### GitHub Actions

Running Playwright on a cloud runner required additional configuration compared to running locally.

### Email Authentication

Google no longer supports basic username/password authentication, so Gmail App Passwords and secure environment variables were configured.

### Preventing Duplicate Alerts

A small state management system was implemented so users receive notifications only when the stock status changes instead of every scheduled run.

---

# Future Improvements

This repository represents **Version 1** of the project.

The next version (**NotifyStock**) will transform this personal automation into a complete service featuring:

- Multiple users
- Different pincodes per user
- Web interface
- FastAPI backend
- MongoDB database
- Subscription management
- Telegram notifications
- Admin dashboard
- Public deployment

---

# Lessons Learned

This project taught me much more than browser automation.

I learned about:

- CI/CD using GitHub Actions
- Secret management
- Environment variables
- Cloud automation
- Production debugging
- Writing automation that runs unattended
- Designing software around a real-world problem

---

# Status

✅ Version 1 Complete

Currently working on Version 2 (NotifyStock).
