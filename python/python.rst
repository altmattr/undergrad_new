Transition to Python
====================

Processing also has a Python mode, but you have to install this yourself.

.. image:: /python/ide_install.jpg

Once you do this, you will see "Python" in the list of modes you can choose in the top-right of the IDE.

:``def`` instead of ``void``: 
    You use the ``def`` keyword instead of the ``void`` keyword to tell Python you have a new function definition.

:Don't delcare variables:
    They just magically are declared for you the first time you use them!  This means that you can't rely on them having a default value, so you must initialise every variable.

:colon and indent instead of curly braces:
    When you would have used curly braces to start and end an ``if``-statement of function etc, you instead put a colon where the ``{`` would have gone, and indent all the lines that would have gone before the ``}``.  You've been indenting like this in your processing code, but you didn't _have_ to, in Python it is not an option. 

:No types on parameters:
    In Python you just give the parameter a name and move on!

:No colons:
    In python you don't complete each statement with a colon.  The carriage return that causes the newline does the job just fine.

Here is an example of a full program in Processing (on the left) and Python (on the right) showing all these differences

.. container:: left
    
    .. code:: java

            int x;
            int y;

            void setup(){
                size(800,800);
                x = 0;
                y = 0;
            }

            void draw(){
                background(0);
                basicGir(x,y);
                x = (x + 1) % width;
                y = (y + 1) % height;
            }

            void basicGir(int x, int y){
                fill(214, 225, 160);
                stroke(0);
                strokeWeight(4);
                rect(x - 100, y - 100, 200, 200);
                fill(255);
                circle(x - 30, y + 20, 80);
                fill(0);
                circle(x-40, y + 18, 3);
                fill(255);
                circle(x + 90, y + 10, 80);
                fill(0);
                circle(x+98, y + 2, 3);
            }

.. container:: right

    .. code:: python

        def setup():
            size(800,800)
            x = 0
            y = 0

        def draw():
            background(0)
            basicGir(x,y,10)
            x = (x + 1) % width
            y = (y + 1) % height

        def basicGir(x, y):
            fill(214, 225, 160)
            stroke(0)
            strokeWeight(4)
            rect(x - 100, y - 100, 200, 200)
            fill(255)
            circle(x - 30, y + 20, 80)
            fill(0)
            circle(x-40, y + 18, 3)
            fill(255)
            circle(x + 90, y + 10, 80)
            fill(0)
            circle(x+98, y + 2, 3)

You don't need ``new`` for arrays
---------------------------------

You can just make an array variable equal to an empty array when you "declare it" and then Python will make up.

You need to use ``insert`` to put things into array (which are really list)
---------------------------------------------------------------------------

Python does't actually have arrays, it has "lists" instead but they work in the same way.

.. container:: left
    
    .. code:: java
        
        for(int i = 0; i < top; i++){
          array[i] = value;
        }

.. container:: right

    .. code:: python

        for i in range(0, top):
            array.insert(i,value)


You will also notice that ``for`` loops change a little.
