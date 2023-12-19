# BlogIgnition

## Overview

BlogIgnition is a dynamic blogging web application that empowers users to create accounts, post blogs, edit, and delete them. The platform offers an interactive space for users to express their thoughts, and readers can explore diverse blogs from various authors.

## Features

- User account creation
- Blog posting, editing, and deletion
- About Me page
- Payment page using the Stripe API for secure transactions
- User profile view to explore all blogs posted by an individual

## How to Run

### Method 1: Using Docker

**Prerequisites:**
1. Docker

**Command:**
```bash
docker run -d -p 5000:5000 devsaini/blogignition
```

**Access:** 
Visit [localhost:5000](http://localhost:5000) in your web browser.

### Method 2: Manual Setup

**Prerequisites:**
1. Python
2. Flask
3. SQLite

**Commands:**
```bash
pip install -r requirements.txt
py app.py
```

**Access:**
Visit [localhost:5000](http://localhost:5000) in your web browser.

## Contribution

Feel free to contribute by opening issues or submitting pull requests.

Happy Blogging!
