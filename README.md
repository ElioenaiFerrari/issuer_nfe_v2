# Issuer NFe V2

- [Issuer NFe V2](#issuer-nfe-v2)
  - [What's new](#whats-new)
  - [How to use?](#how-to-use)

## What's new

- Emit with http protocol
- Selenium and Webdriver for automation
- Email send on done issue

## How to use?

<span style="color: orange;">POST</span> {host}/api/v2/issue

body:

```json
{
  "user": {
    "username": "", // CNPJ
    "password": "",
    "service_code": "11972" // Service code
  },
  "company": {
    "cnpj": "",
    "name": "",
    "zip_code": "",
    "street": "",
    "district": "",
    "city": "",
    "state": "",
    "email": ""
  },
  "note": {
    "code": 1,
    "description": "COMISSIONAMENTO",
    "quantity": 1,
    "unit_value": 1800
  },
  "on_done": {
    "from": "",
    "to": "",
    "subject": "Hi, this is  my NFe"
  }
}
```
