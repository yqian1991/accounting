# Accounting
Accounting script

# How to use
## Record the expense in expense.json
If an amount is shared by all the people, then you can leave "shared_by" empty
```
{
  "qian_yu": {
    "1": {
      "amount": 84.84, // 84.84 is shared by all
      "shared_by": []
    }
  }
}

```
If an amount is shared by some people, you should list their names in "shared_by",
the name must be exactly the same in the file
```
{
  "liu_yang": {
    "1": {
      "amount": 710.77, // 710.77 is shared by all
      "shared_by": []
    },
    "2": {
      "amount": 149.19, // only liu_yang and liu_xinyu should pay for this amount
      "shared_by": ["liu_yang", "liu_xinyu"]
    }
  }
}
```
As you see, you can also set multiple records for the same person.

## Run
```python
python finance.py expense.json
```
If you are sure the result is right, run the following again to record the result to a txt file
```python
python finance.py expense.json true
```