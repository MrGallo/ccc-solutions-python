# ccc-solutions-python

## Testing Tips
To speed up running and testing your code, you should either *mock* the `input`
function or *comment out* your use of the `input` function and hard-code the 
variable values.

### Mock the `input` function
Place something similar at the top of your code. **You must not include this 
code in your contest submission.**
```python

def mock_input():
    value = mock_inputs.inputs[mock_input.i]
    mock_input.i += 1
    return value
mock_input.i = 0
mock_input.inputs = """100
3
33
66
1""".split("\n")
input = mock_input
```
Just copy and paste the lines of input into the 'inputs' string variable.

### Comment out the use of `input`
If this were my code to submit:
```python
start = int(input())
end = int(input())
```
I would comment out where I used the `input` function and hardcode variables.
```python
# start = int(input())
# end = int(input())

start = 10
end = 50
```
**Be sure to *uncomment* the use of the `input` function, and *comment* out the 
hard-coded values when you submit the problem.