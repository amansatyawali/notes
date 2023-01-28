Generator is a function that uses yield instead of return.
We can have more than one yiled statements in a generator, but we can only have one return statement in a function. That is because when a function encounters return statement, it returns the value that is supposed to, and then clears the state of the function.
But in a generator, when a yield statement is encountered, it returns the value, stops the further execution of the generator, and preserves the state (values of variables etc) of the generator.

We assign a generator to a variable like :
```
    gen_obj = generator_fun()
```

now gen_obj is a generator object. Also, this statement will not execute anything.

Then when we call the next() function with the generator of the argument, the generator function will be executed till the first yield statement is encountered.
```
    res_1 = next(gen_obj)
```

Now the gen_obj will pause the execution of the gnerator and preserve the state.

Then, when the next(gen_obj) will be called again, the execution will start from the last yield statement encountered. And it will run until another yield statement is not encountered.

If we call next() and there is no yield function that is encountered and the generator function ends, a StopIteration error will be raised.