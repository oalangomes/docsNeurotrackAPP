### 📲 [GET] Buscar Cliente por CPF

**Endpoint:**
```bash
GET /sap/commerce/webservices/v1/assistedservicewebservices/customers/search?baseSite=vivoTelco&sort=byNameAsc&query=75987543061
```

**Headers:**
```http
Accept: application/json, text/plain, */*
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
Authorization: Bearer {access_token}
Customer-Emulated-Id: 75987543061
```

**Exemplo curl:**
```bash
curl 'https://api02.digital.vivo.com.br/sap/commerce/webservices/v1/assistedservicewebservices/customers/search?baseSite=vivoTelco&sort=byNameAsc&query=75987543061' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Customer-Emulated-Id: 75987543061' \
  -H 'Origin: https://preprd.lojaonline.vivo.com.br' \
  -H 'User-Agent: Mozilla/5.0' \
  -H 'Referer: https://preprd.lojaonline.vivo.com.br/'
```

**Resposta (200 OK):**
```json
{
  "entries": [{
    "name": "HYBRIS METALICA",
    "uid": "75987543061",
    "cpf": "75987543061"
  }],
  "pagination": {
    "currentPage": 0,
    "totalPages": 1
  }
}
```

---

### 📲 [GET] Buscar Informações do Cliente (ASM)

**Endpoint:**
```bash
GET /occ/v2/vivoTelco/asm/customer/information?cpf=75987543061&employeeId=A0096542&flow=SALESFORCE
```

**Headers:**
```http
Authorization: Bearer {access_token}
Accept: application/json
```

**Exemplo curl:**
```bash
curl 'https://api02.digital.vivo.com.br/sap/commerce/webservices/v1/occ/v2/vivoTelco/asm/customer/information?cpf=75987543061&employeeId=A0096542&flow=SALESFORCE' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Accept: application/json'
```

**Resposta (200 OK):**
```json
true
```

---

### 📲 [GET] Buscar Usuário

**Endpoint:**
```bash
GET /occ/v2/vivo/users/75987543061?lang=pt&curr=BRL
```

**Headers:**
```http
Authorization: Bearer {access_token}
Customer-Emulated-Id: 75987543061
Accept: application/json
```

**Exemplo curl:**
```bash
curl 'https://api02.digital.vivo.com.br/sap/commerce/webservices/v1/occ/v2/vivo/users/75987543061?lang=pt&curr=BRL' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Customer-Emulated-Id: 75987543061' \
  -H 'Accept: application/json'
```

**Resposta (200 OK):**
```json
{
  "name": "HYBRIS METALICA",
  "cpf": "75987543061",
  "currentPlan": "Vivo Fibra 300 Mbps Especial Netflix"
}
```

---
