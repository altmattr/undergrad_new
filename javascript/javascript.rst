Transition to JavaScript
========================

Processing has a special mode for javascript called "p5.js".  You can choose p5.js mode in the top right.  If you do it on an empty document you will get a basic structure (Processing on the left, JavaScript on the right).

.. image:: /javascript/ide.jpg

We will now go through each of the differences between processing and javascript.

``function`` instead of ``void``
--------------------------------
We've been defining functions with ``void`` then a functions name.  The ``void`` keyword was also telling us what the function returned.  In javascript we don't bother giving the return type, instead we use the keyword ``function`` to indicate we are defining a function.

.. container:: left
    
    .. code:: java

        void setup(){
        }

        void draw(){
        }

.. container:: right

    .. code:: javascript

        function setup(){
        }

        function draw(){
        }
    
``createCanvas`` instead of ``size``
------------------------------------

In javascript, you don't get the canvas for free, you have to create it youself and you also set the size you want at that point.

.. container:: left
    
    .. code:: java

        void setup(){
          size(800,800);
        }

        void draw(){
        }

.. container:: right

    .. code:: javascript

        function setup(){
          createCanvas(800,800);
        }

        function draw(){
        }

Runs in a browser
-----------------

When you start your program it will open a web broswer and run it there - JavaScript is all about programming web pages instead of desktop applications.

``var`` instead of datatype
---------------------------

Javascript does not need you to tell it what type a variable is, instead you just use ``var`` to say "this is a variable declaration"

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
            circle(x,y,10);
            x = (x + 1) % width;
            y = (y + 1) % height;
        }
.. container:: right

    .. code:: javascript

        var x;
        var y;

        function setup() {
            createCanvas(800,800);
            x = 0;
            y = 0
        }

        function draw() {
            background(0);
            circle(x,y,10);
            x = (x + 1) % width;
            y = (y + 1) % height;
        }

You don't need to put a data type into your function signature
--------------------------------------------------------------

You might think it would need to be ``var`` instead but in fact you can leave it out entirely.

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

    .. code:: javascript

            var x;
            var y;

            function setup() {
            createCanvas(800,800);
            x = 0;
            y = 0
            }

            function draw() {
            background(0);
            basicGir(x,y,10);
            x = (x + 1) % width;
            y = (y + 1) % height;
            }

            function basicGir(x,  y){
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

