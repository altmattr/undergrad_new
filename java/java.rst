Transition to Java
==================

Processing _is_ Java under the hood.  The processing IDE we have been using basically just makes Java look nicer for us and gives us easy access to all the primitive operations we've been using.  We can do everything we did in Processing directly in Java if we can get our head around the more complex IDE that Java uses [#].

.. [#] There are actually multiple IDEs for Java but the most populare one, and the one you will use in COMP1010, is Visual Studio Code.

You will need to download a cop  of the Java IDE _Visual Studio Code_ and install the Java Extensions.

Importing the library
---------------------

Java doesn't have all the processing graphics primitives unless we _import them_

.. code:: java

    import processing.core.*;
    import processing.data.*;
    import processing.event.*;
    import processing.opengl.*;


Objects (and Classes)
--------------------

Nothing happens in Java without a special compound data type called ``Main`` which also needs to be defined by the programmer!  When you get in to Java properly you will learn how to make your own compound datatypes and then build values of them, but we can simply memorise the formula at this stage.  ``public class Main {...} extends PApplet`` is how to make a datatype callse ``Main``.

This datatype needs a special function called ``main`` (lowercase this time) which is actually the very first function called in any Java program.  The recipie for this is ``public static void main(String[] args){ ... }``.

It is also up to _us_ to make sure ``setup`` and ``draw`` get called appropriately, which you do by making sure your ``main`` function looks like this

.. code:: java

    static public void main(String[] passedArgs) {
        String[] appletArgs = new String[] { "examples" };
        if (passedArgs != null) {
            PApplet.main(concat(appletArgs, passedArgs));
        } else {
            PApplet.main(appletArgs);
        }
    }

Don't worry about what any of that means, it can be considered "magic incantations" for now.  You will learn more in later courses.

At this point you can just copy-paste your Processing code into the ``Main`` class, with just _one other change_.  You know how ``size`` always had to be the first line of your ``setup`` function?  That's because it actually needs to be put into a special function that runs _before_ ``setup`` called ``settings``.  What we end up with is this (processing on the left, java on the right)

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

        import processing.core.*;
        import processing.data.*;
        import processing.event.*;
        import processing.opengl.*;

        import java.util.HashMap;
        import java.util.ArrayList;
        import java.io.File;
        import java.io.BufferedReader;
        import java.io.PrintWriter;
        import java.io.InputStream;
        import java.io.OutputStream;
        import java.io.IOException;

        public class examples extends PApplet {

        int x;
        int y;

        public void setup(){
            x = 0;
            y = 0;
        }

        public void draw(){
            background(0);
            basicGir(x,y);
            x = (x + 1) % width;
            y = (y + 1) % height;
        }

        public void basicGir(int x, int y){
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


        public void settings() { size(800, 800); }

        static public void main(String[] passedArgs) {
            String[] appletArgs = new String[] { "examples" };
            if (passedArgs != null) {
                PApplet.main(concat(appletArgs, passedArgs));
            } else {
                PApplet.main(appletArgs);
            }
        }
        }
