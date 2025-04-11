# 🕵️‍♂️ Selenium Scraper App

This project is a web scraping application built using **Selenium**. It automates the process of searching for items on a specified website, scrolling through lazy-loaded content, and extracting relevant data such as card name, price, category, rarity, and ID number.

---

## 📂 Project Structure

```
selenium-scraper-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── scraper          # Module for scraping logic
│   │   ├── __init__.py  # Initialization file for the scraper module
│   │   └── scraper.py   # Contains the Scraper class with scraping methods
│   ├── utils            # Module for utility functions
│   │   ├── __init__.py  # Initialization file for the utils module
│   │   └── helpers.py   # Contains helper functions for the scraper
├── requirements.txt      # Lists project dependencies
├── .env                  # Contains environment variables
└── README.md             # Documentation for the project
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/selenium-scraper-app.git
   cd selenium-scraper-app
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Update the `.env` file with any required environment variables.

---

## 🚀 Usage

To run the application, execute the following command:
```bash
python src/main.py
```

---

## ✨ Features

- 🔍 **Automated Searching**: Searches for items on a specified website.
- 📜 **Lazy Loading Support**: Scrolls through lazy-loaded content to ensure all items are loaded.
- 📊 **Data Extraction**: Extracts detailed information about each item, including:
  - 🃏 **Card Name**
  - 💲 **Price**
  - 📂 **Category**
  - ⭐ **Rarity**
  - 🆔 **ID Number**

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

For questions or support, please contact [kisstudios98@gmail.com](mailto:kisstudios98@gmail.com).

---

### © 2025 Kisstudios Production
