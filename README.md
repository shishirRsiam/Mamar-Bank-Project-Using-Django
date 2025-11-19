# Mamar Bank 🏦

A comprehensive banking management system built with Django. This project allows users to manage bank accounts, perform transactions, apply for loans, and more, all within a secure and user-friendly interface.

---

## Live Demo 🌐

**Live Link**: [http://94.136.186.18:8000/](http://94.136.186.18:8000/)

---

## Features 🚀

### User Features

* **User Registration & Login** with full account details.
* **Profile Management** with activity logs and achievements.
* **Deposit, Withdraw, and Send Money** with instant confirmation emails.
* **Loan Applications** with purpose, priority, and repayment frequency.
* **Full Transaction Reports** including date-range filtering.
* **Daily Bonus System** with automated email templates and cache-based checks.
* **Password Change Email Alerts**.
* **TailwindCSS UI + Django Templates** for clean UX.
* **PostgreSQL Support** with optimized queries.
* **Real-time Notifications** (via email for key financial actions).
* **Desktop Web Only**: Designed to be used on PC or laptop web browsers; not optimized for mobile.

### Admin Features

* **Loan Request Management**: Approve, reject, or review.
* **User Account Oversight**: View and manage user activities.
* **Transaction Monitoring**: Full visibility into operations.
* **Superuser-Exclusive Controls**.
* **Deposit Money to Users**: Admin can directly add funds to any user's account.

---

## New Additions ✨

* **Celery Task Queue Integration** for asynchronous processing of:

  * Account creation emails
  * Loan request emails to users and admin
  * Deposit and withdrawal confirmations
  * Money transfer confirmations
  * Daily bonus notifications
  * Password change alerts
* **Cache-based Daily Bonus System**: Prevents multiple bonuses in a day per user.
* **Cron Jobs** for automated background tasks.
* **Dockerized Deployment** with separate containers for Django, Redis, Celery, PostgreSQL and Pgadmin.
* **Dedicated Worker & Beat Services** for background operations.
* **Log Management System** using Bash scripts & cron.
<!-- * **Rate Limiting Support** (Python-based decorators). -->
* **User Activity Tracking** for profile dashboard.

  * Welcome
  * Account Information
  * Settings
  * Change Password
  * Recent Activity
  * Achievements

---

## Technologies Used 🛠️

* **Backend**: Django Framework
* **Task Queue**: Celery
* **Broker/Backend**: Redis
* **Database**: PostgreSQL
* **Frontend**: TailwindCSS + HTML Templates
* **Deployment**: Docker & Docker Compose
* **Email System**: SMTP with templated messages

---

This project showcases a secure, modern, and scalable online banking system built to handle real financial operations with reliability and performance. The focus is on backend functionality rather than frontend design.
