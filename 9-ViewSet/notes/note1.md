### What is a ViewSet (DRF)?

A **ViewSet** is a class that **handles multiple CRUD actions in one single class**.

Instead of writing **separate views for list, create, retrieve, update, delete**, ViewSet groups them together.

---

### Example (without ViewSet)

You might write many views:

```
ListAPIView
CreateAPIView
RetrieveAPIView
UpdateAPIView
DestroyAPIView
```

Each usually needs its **own URL**.

---

### Example (with ViewSet)

```python
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

This **one class handles all operations**:

* list
* create
* retrieve
* update
* delete

---

### Why DRF created ViewSets

Main reason: **reduce repetition and simplify routing**.

With routers:

```
router.register('students', StudentViewSet)
```

DRF automatically creates URLs like:

```
GET     /students/       → list
POST    /students/       → create
GET     /students/1/     → retrieve
PUT     /students/1/     → update
DELETE  /students/1/     → delete
```

---

### Simple Difference

| Feature             | Generic/Concrete Views | ViewSet               |
| ------------------- | ---------------------- | --------------------- |
| Views per operation | Multiple classes       | One class             |
| URLs                | Manually defined       | Router auto-generates |
| Code size           | More                   | Less                  |

---

✅ **Super simple idea**

```
APIView / Generic Views → one class = one action
ViewSet → one class = many actions
```
