## compare
```sh
# compare values
*** Variables ***
${num1} 0.0
${num2} 0 
*** Test Cases ***
IF ${num1} == ${num2}   # compare nums or string
IF '${num1}' == '${num2}'  # compare string
```