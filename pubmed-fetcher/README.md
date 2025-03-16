# PubMed Fetcher

A Python tool to fetch PubMed research papers based on a search query, filter authors by affiliation, and save results to a CSV file.

## 🚀 Features
- Fetches research papers from **PubMed** using the **NCBI API**.
- Filters **non-academic authors** based on affiliations.
- Saves results to a **CSV file**.

---

## 📦 Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher
```

### 2️⃣ **Install Poetry (If Not Installed)**
```sh
pip install poetry
```

### 3️⃣ **Install Dependencies**
```sh
poetry install
```

---

## ⚙️ **Usage**
### **Run the script using Poetry:**
```sh
poetry run get-papers-list "cancer treatment" -f results.csv
```
or  
```sh
poetry run python -m pubmed_fetcher.cli "cancer treatment" -f results.csv
```

### **Example Output**
```
Fetching papers for query: cancer treatment
Results saved to results.csv
```

---

## 📜 **Results**
After running the script, **`results.csv`** will be created with details of research papers:

| PubmedID  | Title                 | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|-----------------------|------------------|------------------------|-------------------------|----------------------------|
| 12345678  | Cancer Research Paper | 2024-01-15       | John Doe, Jane Smith   | Pharma Inc.             | john.doe@example.com       |
| 98765432  | New Cancer Drug Study | 2023-12-20       | Alice Brown            | Biotech Corp.           | alice.brown@example.com    |

---

## 🔧 **Troubleshooting**
### **1️⃣ If `ModuleNotFoundError: No module named 'pubmed_fetcher'`**
```sh
poetry env remove python
poetry install
```
Then try running again.

### **2️⃣ If `get-papers-list` Command Not Found**
Run:
```sh
poetry run python -m pubmed_fetcher.cli "cancer treatment" -f results.csv
```

---

## 📄 **License**
This project is **open-source** and free to use under the **MIT License**.

---

## ❤️ **Contributing**
Feel free to submit **issues**, **feature requests**, or **pull requests**!  


