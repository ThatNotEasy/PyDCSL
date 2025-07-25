# PyDCSL 🛡️🔐  
*A compact Python tool to check if a Widevine device certificate (DCSL) is revoked or valid.*

## 📦 What is PyDCSL?
**PyDCSL** is a lightweight Python utility that interacts with a custom API to process **Widevine license components** — specifically `.wvd`, `client_id`, and `private_key` files — and fetch the corresponding DRM metadata.  
It acts as a tool for **DRM inspection**, metadata extraction, and license validation purposes. The tool provides both a command-line interface (CLI) and an importable Python module.

---

## ⚙️ Features

- 🧾 Accepts `.wvd`, `client_id`, and `private_key` inputs
- 🌐 Sends requests to a Widevine DCSL-compatible API
- 📊 Pretty-prints extracted metadata using `rich` (if available)
- 🧪 Supports both CLI and importable module
- 📁 Optionally saves results to a JSON file

---

## 🚀 Usage

### 🔧 Command-Line Interface

To get started with the CLI, simply run:

```bash
pydcsl -h
```

<img width="774" height="492" alt="CLI screenshot" src="https://github.com/user-attachments/assets/817e105f-c266-4381-89d9-12697c297ac7" />

---

## 📋 Output Example

Here’s an example of what the output looks like when you run the tool:

<img width="956" height="764" alt="Output example" src="https://github.com/user-attachments/assets/a36ec35a-11ec-43d6-be98-33eff5a5be92" />

## 🧾 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for more details.

---

## ❗ Disclaimer

> This tool is intended for educational, debugging, and interoperability purposes only. Usage of Widevine-protected materials must comply with relevant laws and terms of service. The authors of this project do not condone or support illegal or unethical use.

---

## 🤝 Contributions

Contributions, fixes, and improvements are welcome! Feel free to open an issue or submit a pull request (PR).

---