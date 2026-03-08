Good question 👍 The key idea is **risk reduction and control**.

Even though we still move **tokens**, they are **safer than sending passwords repeatedly**.

---

## 1️⃣ Password is permanent, token is temporary

A **password is permanent**.

If someone steals it:

* they can log in
* change account settings
* lock you out

But a **token** can be:

* expired
* revoked
* limited

Example:

```
Password → permanent key
Token → temporary access card
```

---

## 2️⃣ Tokens can have limited permissions

Tokens can restrict what someone can do.

Example in APIs:

* token A → read data only
* token B → read + write
* token C → admin

If stolen, **damage is limited**.

Password = **full control always**.

---

## 3️⃣ Password exposure risk

Without tokens you would do:

```
Request 1 → send password
Request 2 → send password
Request 3 → send password
Request 4 → send password
```

More transmissions = **higher chance of interception**.

With tokens:

```
Login → password once
Next 1000 requests → token only
```

---

## 4️⃣ Tokens can expire automatically

Modern systems like **OAuth 2.0** or **JSON Web Token** use:

* **short-lived access tokens** (5–15 minutes)
* **refresh tokens**

Even if stolen → attacker only gets **short time access**.

---

## 5️⃣ You can revoke tokens instantly

If a token leaks:

```
delete token → access gone
```

But if password leaks:

```
attacker may change password first
```

---

✅ **Simple summary**

| Password        | Token             |
| --------------- | ----------------- |
| Permanent       | Temporary         |
| Full access     | Limited access    |
| Hard to revoke  | Easy to revoke    |
| Sent many times | Sent once (login) |

So tokens **reduce risk**, even though they are also credentials.

---

💡 Small insight:
In modern large systems (Google, Netflix, AWS), **passwords are almost never used directly after login**. Everything runs on **tokens internally**.

---

If you want, I can also explain **the real reason big companies moved from sessions → tokens → JWT → OAuth** (it’s a very interesting architecture concept).
