# Lesson 6

0. look at the file

1. create a holder for our data, which will be `dictionary` (dic, list, etc.)

2. read as one big string
3. split into records using `\n@`
	- we will get a list of strings
4. loop through all the records:
	NB: each records is a string that needs to be converted into something else.
	- we need to split each record using `,\n`
	- now we loop through the list of "key-value" pairs
	- type&citationkey element:
		- grab list element with index 0 (`citationkey = record[0]`)
		- split the element on `{`
			- recordType = element[0]
			- citationKey = element[1]
	- add a record into our `dictionary` using citationKey as a key value
	- add recordType into the newly created record
	- process the rest of the record:
		- loop through the record, starting with 1:
			- `for r in record[1:]:`
		- split every element on `=`
			- key = element[0].strip()
			- value = element[1].strip()
			- add our key-value pair into the `dictionary`

Next part: save `dictionary` into: CSV, JSON, YAML

	- Easy: *dump* your `dictionary` into JSON or YAML, using corresponding libraries
	- 


```
conversionDic = {
	'year' : 'date',
	'date' : 'date',
	...
}
```















