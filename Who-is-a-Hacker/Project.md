# 🔐 Vulnerability Audit Suite

**Vulnerability Audit Suite** is an all-in-one network scanning and vulnerability reporting tool. It streamlines the cybersecurity auditing process by integrating popular tools like `nmap`, `nikto`, `arp-scan`, and `OpenVAS`, and enhances reporting with AI-generated summaries using **LLaMA 3.2**.

![Hero](./screenshots/screenshot-hero.png)

---

## 🚀 Features

* **Run Network Scans**: Automatically detect devices, open ports, OS, and services.
* **Nikto + OpenVAS**: Perform in-depth vulnerability and web scanning.
* **AI Report Generator**: Generate professional, business-ready summaries of raw scan data using LLaMA via Ollama.
* **Exportable Word Reports**: Instantly download summaries in `.docx` format.
* **Modern UI**: Clean, dark-themed interface with TailwindCSS styling and responsive layout.

---

## 📸 Screenshots

### 🎯 Dashboard

A central hub for scanning, uploading, and generating reports.
![Dashboard](./screenshots/screenshot-dashboard.png)

### 📄 AI-Generated Summary

Get human-readable, NIST-compliant vulnerability and asset summaries.
![AI Summary](./screenshots/screenshot-ai-summary.png)

### 🧪 Full Technical Scan Output

Detailed logs from `nmap`, `nikto`, and more.
![Scan Summary](./screenshots/screenshot-scan-summary.png)

### 🧾 Exportable Word Report

Professional `.docx` reports downloadable in one click.
![Download Word Report](./screenshots/screenshot-docx.png)

---

## 🛠️ Stack

* **Frontend**: Next.js (App Router) + TailwindCSS
* **Backend**: Node.js API routes (`/api/ollama`)
* **AI Engine**: Local Ollama server (LLaMA 3.2)
* **Document Generation**: `docx` NPM package
* **Scan Tools**: `nmap`, `nikto`, `OpenVAS`, `arp-scan`

---

## 🧠 How It Works

1. 📡 **Scan**: The system discovers active hosts and runs vulnerability scans.
2. 🤖 **Generate**: Raw results are summarized using AI via Ollama (`/api/generate`).
3. 📝 **Report**: Markdown-style output is converted into a downloadable `.docx` Word document.
4. 📥 **Review**: The user can preview or download the summary directly from the UI.

---

## 🧪 Local Setup

```bash
git clone https://github.com/yourname/vulnerability-audit-suite
cd scan-frontend
npm install
npm run dev
```

### 🧠 Requirements

* Node.js + npm
* Local Ollama instance (`ollama run llama3.2`)
* Scan data in `../reports/scan_results.json`

---

## 📂 Folder Structure

```
/public            # Static assets like summary.docx
/app/api/ollama    # AI summarization + docx generation API
/components/       # Reusable UI components
/reports/          # Scan data (expected relative to root)
```

---

## 📦 TODO

* [ ] Add PDF export
* [ ] Add scan scheduler
* [ ] Integrate with CVE database API
* [ ] Authentication & access control

---

## 🛡️ License

MIT License — free to use, modify, and distribute.
