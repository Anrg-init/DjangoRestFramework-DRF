1 --- ## 1️⃣ HTTP Request (what client sends)


A request has **4 main parts**.

```
Request Line
Headers
Body
Query Parameters
```

### Example Request

```
POST /api/student/?page=2 HTTP/1.1
Host: example.com
Authorization: Basic YWRtaW46MTIzNA==
Content-Type: application/json
Cookie: sessionid=abc123

{
  "name": "Rahul",
  "age": 20
}
```

### Parts

| Part         | Example                         | Purpose      |
| ------------ | ------------------------------- | ------------ |
| Request Line | `POST /api/student/ HTTP/1.1`   | Method + URL |
| Headers      | `Authorization`, `Content-Type` | metadata     |
| Query Params | `?page=2`                       | filtering    |
| Body         | JSON data                       | actual data  |

---

# 2️⃣ Request Data Types

Different types of request body formats:

| Type      | Example              | Used in     |
| --------- | -------------------- | ----------- |
| JSON      | `{ "name":"Rahul" }` | APIs        |
| Form Data | `name=rahul`         | HTML forms  |
| Multipart | files/images         | file upload |
| XML       | `<name>rahul</name>` | old APIs    |

DRF usually uses:

```
application/json
```

---

# 3️⃣ HTTP Response (what server sends)

A response also has **3 main parts**.

```
Status Line
Headers
Body
```

### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Rahul",
  "age": 20
}
```

---

# 4️⃣ Response Status Codes

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 400  | Bad request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not found    |
| 500  | Server error |

Example:

```
HTTP/1.1 401 Unauthorized
```

---

# 5️⃣ Request Object in DRF

DRF converts request into Python object.

Example:

```python
request.method
request.headers
request.query_params
request.data
request.user
```

Example usage:

```python
name = request.data["name"]
page = request.query_params.get("page")
```

---

# 6️⃣ Response Object in DRF

Server returns response using:

```python
from rest_framework.response import Response
```

Example:

```python
return Response({"message": "success"})
```

DRF converts it to JSON automatically.

---

# 7️⃣ Full Flow

```
Client Request
   ↓
HTTP Request
   ↓
Django/DRF
   ↓
View logic
   ↓
Response object
   ↓
HTTP Response
```

---

# Very Short Summary

| Component | Contains                            |
| --------- | ----------------------------------- |
| Request   | method, headers, query params, body |
| Response  | status code, headers, body          |

```
Client → HTTP Request → Server → HTTP Response → Client
```




2 --- 