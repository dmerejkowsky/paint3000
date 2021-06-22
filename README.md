# Paint3000 - a refactoring exercise

## Instructions

First, make sure you can run the tests. This will involve creating a virtualenv and installing `pytest` in it.

Second, try and understand what the `Paint` class does and how it works.

Then, try to use the Command/Query separation and the Single Responsibility principles to refactor the code.

Notes:

* You should limit the changes to the public API of the `Paint` class and to the `./test_paint.py` file
* You can introduce as many classes and as many modules you want.

Have fun :)

<details>
   <summary>Hints</summary>
Here's a list of steps you can take:

1. Extract a `Store` class which will deal with saving data into and reading from the JSON file
1. Extract a `Report` class to generete the text of the report
1. Implement Command/Query separation in the `Report` class : you should not have to mutate
   state inside the `Report` class
1. Implement Command/Query separation in the `Paint` class by introducing a `use_paint` command
   method.
</details>

## Credits

Code adapted from the "Clean Code In the Browser" series, by Chris Powers.

https://cleancoders.com/series/clean-code-in-the-browser
