title: How to use Python decorators to write a command line execution tool
date: 2019-02-28 02:54
category: Python
tags: Python
slug: command-line-tool-with-python-decorators
summary: Decorator pattern is one of those well-known design patterns. It wraps your functions or classes and adds behaviors on top of them. To make a 6-inch screen a mobile phone, you just need to decorate it with a circuit board, antenna, battery etc. But what the screen does is still displaying content.

## Hmm, decorators?

Decorator pattern is one of those well-known design patterns that I learned from University. It magically wraps your functions or classes and adds behaviors on top of them. Think about how much you can do with a LCD screen. Decorating it with a CPU and remote, it becomes a TV. Topping up with an antenna, and battery, it becomes a mobile phone. But what the screen essentially does is still displaying content. Decorators don't change the behaviors of their components but extend their capabilities and add extra functionalities.

Today, I'm going to demonstrate some examples of how I've used decorators to build a simplified command line processor. 

## Basic usage of decorator 

Firstly, we are going to start with writing a decorator "after_execution" that simply prints any output from it decoratees (I know it's not a word, but you get the idea) .

```python
import functools

def after_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        print(f"Executed a command!\n... {output}")
        return output
    
    return wrapper

@after_execution
def execute_command(command_name):
    if command_name == "gun":
        return "puh"
    elif command_name == "grenade":
        return "boom"
    elif command_name == "exit":
        return exit()

output = execute_command("grenade")
print(output)
```

Let us break up the code above line by line,

Line 1: import functools built-in module in Python that helps us to create decorators.

Line 3 & 10:  We defined a function decorator called "after_execution". It takes a function as an argument, wraps it and returns the wrapped function.

Line 4 - 5: By using functools.wraps, we defined the wrapper which is the actual part that decorates functions. The wrapper can takes unlimited positional arguments and named arguments as we (pretend that) don't know what arguments the decoratee function – which is func, takes.

Line 6 - 8: The wrapper invokes the func and prints its outputs. It also returns whatever the func has returned so that we don't alter its behavior in terms of output values.

Line 10: After decorator finishes decorating the function, we return the wrapper,  so that other decorators can further decorate on top of them.

Line 12 - 13: Defines function execute_command and decorates it with after_execution decorator.

Line 14 - 19: Obviously, it's the logic of execute_command that decorator doesn't need to care about.

The output of the above script would then be,

```python
>>> Executed a command!
>>> ... boom
>>> boom
```

Hooray, we have decorated the command executor! We also have separated the concerns of different functions. The command executor doesn't need to know what would happen after executing the command. Also, the decorator doesn't have to worry about how commands are being executed. 
Decorators with arguments

For now, the command executor needs to catalog commands and processes them differently. However, ideally, the job should be done by the decorator. What a executor only needs to know is executing one command. We then could have as many as executors we want, and let command decorator handle the rest.

To achieve that, we need to add arguments on our decorator and decorate executors accordingly.

```python
import functools

COMMANDS = dict()

def command(command_name):
    def _command(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            print(f"Executed a command!\n... {output}")
            return output
        
        COMMANDS[command_name] = wrapper
        return wrapper
    
    return _command

@command("gun")
def execute_gun():
    return "puh"
    
@command("grenade")
def execute_grenade():
    return "boom"

@command("exit")
def execute_exit():
    return exit()

def operation_center():
    while True:
        command_name = input("Please enter the command: ")
        COMMANDS[command_name]()
        
if __name__ == "__main__":
    operation_center()
```

The code is very similar to the old code, except there is an extra layer being added in command decorator. 

Line 5 - 11: Decorator command takes one positional argument command_name, and it wraps the previous after_execution decorator.

Line 13: Registers command within the global variable COMMANDS. Command name as key and the wrapper function as value.

Line 14 & 16: Returns decorator functions for each layer.

Now, we have separated our monolith executor to two "micro" executors. COMMANDS global variables acts as an operator in operation center to dispatch commands according to input values. 

Now, when we run the script with input grenade, gun and exit the output will be,

```python
Please enter the command: gun
>>> Executed a command!
>>> ... puh
Please enter the command: grenade
>>> Executed a command!
>>> ... boom
Please enter the command: exit
```

## Summary

With decorators, it saves us from repeating ourself and separate the concerns of different functions. The decorator pattern has also been applied everywhere even though you might not be aware of. 

Of course, if you do need a command-line like task execution tool, you don't have to rebuild the wheels. Try Python Invoke which is an amazing tool that I have been using a lot. Actually, it has inspired me to write my own command execution engine and this blog as well.

I'm a fan of all kinds of ChatOps. I have written a GitBot at work, which use exactly the same pattern above to consume commands and arguments to process pull requests comments. But I have to admit that sometimes it's really brain hurting to read the implementation of decorators as there are so many layers going on. Make sure you have documented your code properly! Happy hacking!