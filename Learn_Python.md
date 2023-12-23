## TABLE OF CONTENTS
- [PYTHON CONCEPT](#python-concept)
    - [BASICS PYTHON](#basics-python)
        - [TYPE OF PROGRAMMING](#type-of-input)
        - [OPERATORS](#operators)
            - [ASSIGNMENT OPERATORS](#assignment-operators)
            - [ARITHMETIC OPERATORS](#arithmetic-operators)
            - [COMPARISON OPERATORS](#comparison-operators)
            - [LOGICAL OPERATORS](#logical-operators)
            - [IDENTITY OPERATORS](#identity-operators)
            - [MEMBERSHIP OPERATORS](#membership-operators)
            - [BITWISE OPERATORS](#bitwise-operators)
        - [DATA TYPES](#data-types)
            - [STRING](#string)
            - [TUPLE](#tuple)
            - [LIST](#list)
            - [DICTIONARY](#dictionary)
            - [SET](#set)
            - [ARRAY](#array)
            - [BOOLEAN](#boolean)
        - [DATA STRUCTURE](#data-structure)
            - [LINEAR DATA STRUCTURE](#linear-data-structure)
                - [STATIC DATA STRUCTURE](#static-data-structure)
                    - [ARRAY](#array)
                - [DYNAMIC DATA STRUCTURE](#dynamic-data-structure)
                    - [QUEUE](#queue)
                    - [STACK](#stack)
                    - [LINKED LIST](#linked-list)
            - [NON LINEAR DATA STRUCTURE](#non-linear-data-structure)
                - [TREE](#tree)
                - [GRAPH](#graph)
        - [FLOW OF CONTROL](#flow-of-control)
            - [CONDITION](#condition)
                - [IF](#if)
                - [ELSE](#else)
                - [ELIF](#elif)
            - [LOOPS](#loops)
                - [FOR](#for)
                - [WHILE](#while)
            - [BREAK](#break)
            - [PASS](#pass)
            - [CONTINUE](#continue)
        - [EXCEPTION](#exception)
            - [TRY](#try)
            - [EXCEPT](#except)
        - [FUNCTION](#function)
            - [BUILT IN](#built-in)
                - [GLOBAL FUNCTION](#global-function)
                - [LIBRARY BASED](#library-based)
            - [USER DEFINE](#user-define)
        - [RECURSION](#recursion)
        - [FILE HANDLING](#file-handling)
            - [TEXT FILE](#text-file)
            - [BINARY FILE](#binary-file)
            - [<abbr title="COMMA SEPRATED VALUE FILE">CSV FILE</abbr>](#csv-files)
        - [ABOUT PIP](#pip)
    - [ADVANCE PYTHON](#advance-python)
        - [<abbr title="OBJECT-ORENTED PROGRAMMING LANGUAGE">OOPS</abbr>](#oops-object-orented-programming-language)
            - [CLASS](#class)
            - [OBJECT](#object)
            - [ABSTRACTION](#abstraction)
            - [ENCAPSULATION](#encapsulation)
            - [INHERITANCE](#inheritance)
                - [OVERRIDDING](#overridding)
            - [POLYMORPHISM](#polymorphism)
                - [OVERLOADING](#overloading)
        - [NUMPY (LIBRARY)](#numpy)
        - [PANDAS (LIBRARY)](#pandas)
        - [MATPLOTLIB (LIBRARY)](#matplotlib)
        - [PYSDR (IT IS USED TO WORK WITH RADIO WAVES)](#pysdr)
- # PYTHON CONCEPT
    - ## BASICS PYTHON
        + built in:-pre define
            + type() is built in function to find type of th variable
            + len() is a built in function to find the length of data.
        + variable
        + literal
        - ### TYPE OF INPUT
            - We can tak input by two ways in python
                + 1.static
                    - in static we driect assign the value to variable
                    <br/><code>x=10</code>
                + 2.dynamic
                    - for dynamic input we can use python built in function "input"
                    <br/><code>x=input("enter your value")</code>
        - ### OPERATORS
            -![TYPES OF OPERATORS](<Screenshot 2023-11-11 100646.png>)
            - ### ASSIGNMENT OPERATORS
                 The operators including =, +=, -=, =, /=, %=, //=, *=, &=, |=, ^=, >>=, and <<= are employed to evaluate a value to a variable. 
                - #### (=)
                - #### (+=)
                - #### (-=)
                - #### (/=) 
                - #### (%=) 
                - #### (//=)
                - #### (*=)
                - #### (&=)
                - #### (|=)
                - #### (^=)
                - #### (>>=) 
                - #### (<<=)
            - ### ARITHMETIC OPERATORS
                + The operators including =, +=, -=, =, /=, %=, //=, *=, &=, |=, ^=, >>=, and <<= are employed to evaluate a value to a variable.
            - ### COMPARISON OPERATORS
                + Comparison operations compare some value or operand and based on a condition, produce a Boolean. Python has six comparson operators as below:
                    + Greater Than (>)
                    + Less Than (<)
                    + Greater Than Or Equal To(>=)
                    + Less Than Or Equal To(<=)
                    + Equal To(==)
                    + Not Equal To(!=)
                + The comparson operators are also employed to compare the letters/words/symbols accordng to the <abbr title="American Standard Code for Information Interchange"> ASCII </abbr> value of letters.
            - ### LOGICAL OPERATORS
                + Logcal operators are used to combine conditional statements.
                - #### AND
                    * Returns True if both statements are true.
                        <table border="3" style="border-color:purple;background-color:black">
                            <tr>
                                <th>A</th>
                                <th>B</th>
                                <th>A and B</th>
                            </tr>
                            <tr>
                                <th>True</th>
                                <th>True</th>
                                <th>True</th>
                            </tr>
                            <tr>
                                <th>True</th>
                                <th>False</th>
                                <th>False</th>
                            </tr>
                            <tr>
                                <th>False</th>
                                <th>True</th>
                                <th>False</th>
                            </tr>
                            <tr>
                                <th>False</th>
                                <th>False</th>
                                <th>False</th>
                            </tr>
                        </table>
                - #### OR
                    * Returns True if one of the statements is true.
                        <table border="3" style="border-color:purple;background-color:black">
                            <tr>
                                <th>A</th>
                                <th>B</th>
                                <th>A or B</th>
                            </tr>
                            <tr>
                                <th>True</th>
                                <th>True</th>
                                <th>True</th>
                            </tr>
                            <tr>
                                <th>True</th>
                                <th>False</th>
                                <th>True</th>
                            </tr>
                            <tr>
                                <th>False</th>
                                <th>True</th>
                                <th>True</th>
                            </tr>
                            <tr>
                                <th>False</th>
                                <th>False</th>
                                <th>False</th>
                            </tr>
                        </table>
                - #### NOT
                    * Reverse the result, returns False if the result is true.
                        <table border="3" style="border-color:purple;background-color:black">
                            <tr>
                                <th>A</th>
                                <th>A Not B</th>
                            </tr>
                            <tr>
                                <th>True</th>
                                <th>False</th>
                            </tr>
                            <tr>
                                <th>False</th>
                                <th>True</th>
                            </tr>
                        </table>
            - ### IDENTITY OPERATORS
                + The operators is or is not are employed to control if the operands or objects to the left and right of these operators are referring to a value stored in the same momory location and return True or False.
                - #### IS
                - #### IS NOT
            - ### MEMBERSHIP OPERATORS
                + These operators inclusing in and not in are employed to check if the certain value is available in the sequence of values and return True or False.
                - #### IN
                - #### NOT IN
            - ### BITWISE OPERATORS
        - ### DATA TYPES
            * In python we can use some data type as follow:-
                    
                ![TYPE OF DATA TYPES](<Screenshot 2023-11-10 204813.png>)
            - ### STRINGS
                <code><abbr title="VARIABLE">STR=<abbr title="DATA">"HELLO WORLD"</abbr></code>
                * + String are immutable in type and cannot be changed in any way once it is created.
                + String are defined in the two diffrent way.
                    + 1.static
                        + In static we can define by three ways:
                            + 1. In single quotation.
                                <br/><code>x='HELLO WORLD'<br/>print(type(x))<br/><br/>Output:<br/><class 'str'></code>
                            + 2. In double quotation.
                            <br/><code>x="HELLO WORLD"<br/>print(type(x))<br/><br/>Output:<br/><class 'str'></code>
                            + 3. In triple quotation.
                            <br/><code>x="""HELLO WORLD"""<br/>OR<br/>x='''HELLO WORLD'''<br/>print(type(x))<br/><br/>Output:<br/><class 'str'></code>
                    + 2.dynamic
                        + by type casting
                            In double quotation.
                            <br/><code>a=[HELLO,WORLD]<br/>x=str(a)<br/>print(type(x))<br/><br/>Output:<br/><class 'str'></code>
                + We can do indexing & slicing in the string.
                + We can also use membership operator in the string.
                    <code>x='HELLO'<br/>print('H' in x)<br/>print('O' not in x)<br><br/>Output:<br/>True<br/>False</code>
                + String allow you to store several data items including characters, integer, float etc.
                - #### INDEXING OF A STRING
                    <code>syntax of indexing:<br/>string[element_no]</code>
                    - TWO TYPE OF INDEXING
                        - FORWORD INDEXING
                            + Forword indexing are counted from the start of the string(starts from [0] and last element is length-1).
                            <br/><code>str="hello world"<br/>print(str[0])<br/>print(str[10])<br/><br/>OUTPUT:-<br/>h<br/>d</code>
                        - BACKWORD INDEXING
                            + Backword indexing are counted from the end of the string(starting element is [-1] and last element is -length).<br/><code>str="hello world"<br/>print(str[-1])<br/>print(str[-11])<br/><br/>OUTPUT:-<br/>d<br/>h</code>
                - #### SLICING OF A STRING
                    - Slicing is similar to indexing but in indexing we get only one element and in slicing we get one or more than one element.
                    <code><br/>syntax of slicing:<br/>string[start:stop:step]</code>
                    + By default step is 1.
                    - Similarly to indexing,we can do two type of slicing:-
                        + FORWORD SLICING
                            * Forword slicing are counted from the start of the string(starts from [0] and last element is length-1).
                            <br/><code>str="hello world"<br/>print(str[0:8])<br/>print(str[3:10:2])<br/><br/>OUTPUT:-<br/>hello wo<br/>l ol</code>
                        + BACKWORD SLICING
                            + Backword slicing are counted from the end of the string(starting element is [-1] and last element is -length).
                            <br/><code>str="hello world"<br/>print(str[-1:-8])<br/>print(str[-1:-8:-1])<br/>print(str[-3:-11:-2])<br/><br/>OUTPUT:-<br/><br/>dlrow o<br/>rwol</code>
                    - **NOTE:-For better understanding try more slicing program.**
                - #### CONCATENATION/REPETATION OF STRING
                    + ##### CONCATENATION
                        * for concatenation we can use "+" operator.
                        * with the help of concatenation we can add two string.<br/>
                            <code>str1="hello "<br/>str2='world'<br/>print(str1+str2)<br/><br/>Output:<br/>hello world</code>
                    + REPETATION
                        * For repetation we can use "*" operator.
                        * with the help of repetation we can write one string at multiple times.<br/>
                            <code>str="hello "<br/>print(str*5)<br/><br/>Output:<br/>hello hello hello hello hello</code>
                - #### ESCAPE SEQUENCES
                    + In the python string many of the escape sequences are available.Few are given below:
                    <table border="3" style="border-color:purple;background-color:black">
                        <tr>
                            <th>USES</th>
                            <th>SYNTAX</th>
                            <th>EXAMPLE</th>
                        </tr>
                        <tr>
                            <td></td>
                            <td>"\n"</td>
                            <td><code>"hello\nworld"<br/>Output:<br/>hello<br/>world</code></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>"\t"</td>
                            <td><code>"hello\tworld"<br/>Output:<br/>hello   world</code></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>"\\"</td>
                            <td><code>"hello python\\world"<br/>Output:<br/>hello python\world</code></td>
                        </tr>
                    </table>
                - #### STRING FUNCTION
                    [FMDKF](<../../../../../upload/pdf/STRING FUNCTION.pdf>)
            - ### TUPLE
                <code><abbr title="VARIABLE">tup=<abbr title="DATA">(1,4,7,9,'cat','rat')</abbr></code>
                + Tuples are immutable in type and cannot be changed in any way once it is created.
                + Tuples are defined in two different way. 
                    * 1.static
                        + In parenthesis().
                        <br/><code>tuple1=(1,2,3,4,5,"atr")<br/><br/>Output:<br/><class 'tuple'></code>
                    * 2.dynamic
                        + type casting
                            <br/><code>tup=[1,2,3,4,5,"atr"]<br/>tuple1=tuple(tup)<br/><br/>Output:<br/><class 'tuple'></code>
                + Tuples are ordered,indexed collections of data.
                + Similar to string indices, the first value in the tuple will have the index [0], the second value [1]
                + Backword indices are counted from the end of the tuple[-1], just like string.
                + In Tuple structure commas separate the values.
                + Tuples can store duplicate values.
                + Tuple can be nested.
                    <code><br/>tuple1=(1,2,3,(4,3,4),6,7)</code>
                + We can also use membership operator in the tuple.
                    <code>tuple1=(1,2,3,4,5,"atr")<br/>print('1' in tuple1)<br/>print('atr' not in tuple1)<br><br/>Output:<br/>True<br/>False</code>
                + Tuples allow you to store several data items including string, integer, float in one variable.
                    <code><br>tuple1=(1,2,3,4,5,"atr")</code>
                - #### INDEXING
                    <code>syntax of indexing:<br/>string[element_no]</code>
                    - TWO TYPE OF INDEXING
                        - FORWORD INDEXING
                            + Forword indexing are counted from the start of the tuple(starts from [0] and last element is length-1).
                            <br/><code>tuple1=(1,2,3,4,5,"atr")<br/>print(tuple1[0])<br/>print(tuple1[4])<br/><br/>OUTPUT:-<br/>1<br/>5</code>
                        - BACKWORD INDEXING
                            + Backword indexing are counted from the end of the tuple(starting element is [-1] and last element is -length).<br/><code>tuple1=(1,2,3,4,5,"atr")<br/>print(tuple1[-1])<br/>print(tuple1[-4])<br/><br/>OUTPUT:-<br/>atr<br/>3</code>
                - #### SLICING
                    - Slicing is similar to indexing but in indexing we get only one element and in slicing we get one or more than one element.
                    <code><br/>syntax of slicing:<br/>tuple_variable[start:stop:step]</code>
                    + By default step is 1.
                    - Similarly to indexing,we can do two type of slicing:-
                        + FORWORD SLICING
                            * Forword slicing are counted from the start of the tuple(starts from [0] and last element is length-1).
                            <br/><code>tuple1=(1,2,3,4,5,"atr")<br/>print(tuple1[0:5])<br/>print(tuple1[1:5:2])<br/><br/>OUTPUT:-<br/>(1, 2, 3, 4, 5)<br/>(2, 4)</code>
                        + BACKWORD SLICING
                            + Backword slicing are counted from the end of the string(starting element is [-1] and last element is -length).
                            <br/><code>tuple1=(1,2,3,4,5,"atr")<br/>print(tuple1[-5:-1])<br/>print(tuple1[-5:-1:-1])<br/>print(tuple1[-6:-1:2])<br/><br/>OUTPUT:-<br/>(1, 2, 3, 4, 5)<br/>()<br/>(1, 3, 5)</code>
                - #### CONCTENATION
                    * for concatenation we can use "+" operator.
                        * with the help of concatenation we can add two tuple.<br/>
                            <code>tuple1=(1,4,3,2,5)<br/>tuple2=(6,5,4,3,7,9)<br/>print(tuple1+tuple2)<br/><br/>Output:<br/>(1, 4, 3, 2, 5, 6, 5, 4, 3, 7, 9)</code>
                    + REPETATION
                        * For repetation we can use "*" operator.
                        * with the help of repetation we can write one tuple at multiple times.<br/>
                            <code>tuple1=(1,4,3,2,5)<br/>print(tuple1*3)<br/><br/>Output:<br/>(1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)</code>
                - #### TUPLE FUNCTION
                    <table border="3" style="border-color:purple;background-color:black">
                        <tr>
                            <th>USES</th>
                            <th>SYNTAX</th>
                            <th>EXAMPLE</th>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </table>
            - ### LIST
                <code><abbr title="VARIABLE">lst=<abbr title="DATA">[1,4,7,9,'cat','rat']</abbr></code>
                + list can be defined in two ways like tuple.
                    * 1.static
                        + In square bracket[].
                        <br/><code>list1=[1,2,3,4,5,"atr"]<br/><br/>Output:<br/><class 'list'></code>
                    * 2.dynamic
                        + type casting
                            <br/><code>lst=(1,2,3,4,5,"atr")<br/>list1=list(lst)<br/><br/>Output:<br/><class 'list'></code>
                + List are ordered.
                + List can contain any items or objects.
                + List elements can be accessed by index similar to string or tuple.
                + List can be nested.
                + We can also do slicing, indexing, concatnation and repetation in list like tuple.
                    <br/><code>list1=[1,2,3,4,5,"atr"]<br/>list2=[5,6,7,8,9]<br/>print(list1[0])<br/>print(list1[4])<br/>print(list1[0:5])<br/>print(list1[-5:-1])<br/>print(list1+list2)<br/>print(list1*3)<br/><br/>OUTPUT:-<br/>1<br/>5<br/>[1, 2, 3, 4, 5]<br/>[2, 3, 4, 5]<br/>[1, 2, 3, 4, 5, 'atr', 5, 6, 7, 8, 9]<br/>[1, 2, 3, 4, 5, 'atr', 1, 2, 3, 4, 5, 'atr', 1, 2, 3, 4, 5, 'atr']</code>
                + We can also use membership operator in the list.
                    <code>list1=[1,2,3,4,5,"atr"]<br/>print('1' in list1)<br/>print('atr' not in list)<br><br/>Output:<br/>True<br/>False</code>
                + List are mutable.
                + List are dynamic.
                <br/><code>list1=[1,2,3,4]<br/>list1[1]=9<br/>print(list1)<br/><br/>Output:<br/>[1, 9, 3, 4]</code>
                - #### LIST FUNCTION
                    <table border="3" style="border-color:purple;background-color:black">
                        <tr>
                            <th>USES</th>
                            <th>SYNTAX</th>
                            <th>EXAMPLE</th>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </table>
            - ### DICTIONARY
                <code><abbr title="VARIABLE">dict=<abbr title="DATA">{<abbr title="KEY">"name"</abbr>:<abbr title="VALUE">"shayam"</abbe>,<abbr title="KEY">"age"</abbr>:<abbr title="VALUE">32</abbr>}</abbr></code>
                + Data of dictionary written in curly brackets{}.
                + Dictionaries are used to store data values in key:value pairs.<br/>
                <code>x={<abbr title="key">"name"</abbr>:<abbr title="value">"ram"}</abbe></code>
                + A dictionary is a collection which is ordered, changeable or mutable and do not allow duplicates.
                + Dictionary can be referred to by using the key name.
                + Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
                + We can also use membership operator in the dictionary.
                + Dictionaries cannot have two items with the same key.
                + A dictionary can nested and can contain another dictionary.
                - #### DICTIONARY FUNCTION
                    <table border="3" style="border-color:purple;background-color:black">
                        <tr>
                            <th>USES</th>
                            <th>SYNTAX</th>
                            <th>EXAMPLE</th>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </table>
            - ### SET
                + Set are immutable
                - #### SET FUNCTION
                    <table border="3" style="border-color:purple;background-color:black">
                        <tr>
                            <th>USES</th>
                            <th>SYNTAX</th>
                            <th>EXAMPLE</th>
                        </tr>
                    </table>
            - ### BOOLEAN
        - ### DATA STRUCTURE
            ![TYPES OF DATA STRUCTURE](<Screenshot 2023-11-10 205940.png>)
            - #### LINEAR DATA STRUCTURE
                - ##### STATIC DATA STRUCTURE
                    - ##### ARRAY
                - ##### DYNAMIC DATA STRUCTURE
                    - ##### QUEUE
                    - ##### STACK
                    - ##### LINKED LIST
            - #### NON LINEAR DATA STRUCTURE
                - ##### TREE
                - ##### GRAPH
        - ### FLOW OF CONTROL
            - ### CONDITION
                + Decision making is required when we want to execute a code only if a certain condition is satisfied.
                + The if/elif/else statement is used in Python for decision making.
                + An else statement can be combined with an if statement.
                + An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a False value
                + The else statement is an optional statement and there could be at most only one else statement following if.
                + The elif statement allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
                + Similar to the else, the elif statement is optional.
                + However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.
                - #### IF
                - #### ELSE
                - #### ELIF
            - #### LOOPS
                - #### FOR
                - #### WHILE
            - #### BREAK
            - #### PASS
            - #### CONTINUE
        - ### EXCEPTION
            - #### TRY
            - #### EXCEPT
        - ### FUNCTION
            - #### BUILT IN
                - ##### GLOBAL FUNCTION
                - ##### LIBRARY BASED
            - #### USER DEFINE
        - ### RECURSION
        - ### FILE HANDLING
            - #### TEXT FILE
            - #### BINARY FILE
            - #### <abbr title="COMMA SEPRATED VALUE FILE">CSV FILE</abbr>
        - ### PIP
- ## ADVANCE PYTHON
    - ### <abbr title="OBJECT-ORENTED PROGRAMMING LANGUAGE">OOPS</abbr>
        - #### CLASS
        - #### OBJECT
        - #### ABSTRACTION
        - #### ENCAPSULATION
        - #### INHERITANCE
            - ##### OVERRIDDING
        - #### POLYMORPHISM
            - ##### OVERLOADING
    - ### NUMPY
    - ### PANDAS
    - ### OPENCV
        - We can use this library for working with normal image(like .jpg,.png and many more) and videos(like mp4).
        - For using opencv library you want to install first this library.By using
        
                pip install opencv-python
        - ### For collecting additional package of opencv library
        
                pip install opencv-contrib-python
        - After installing the you want to import this library in your program By using
        
                import cv2
                                      OR
                from cv2 import*
        <table border="3" style="border-color:purple;background-color:black">
            <tr>
                <th>Task/Uses</th>
                <th>Syntax</th>
                <th>Example</th>
            </tr>
            <tr>
                <td>To read an image</td>
                <td>varable=cv2.imread()</td>
                <td>object=cv2.imread("file_name")</td>
            </tr>
            <tr>
                <td>To save an image</td>
                <td>cv2.imwrite()</td>
                <td>cv2.imwrite("Image_Name",object)</td>
            </tr>
            <tr>
                <td>To display an image</td>
                <td>cv2.imshow()</td>
                <td>cv2.imshow("Image_name",object)</td>
            </tr>
            <tr>
                <td>To convert gray Image</td>
                <td>cv2.cvtColor()</td>
                <td></td>
            </tr>
            <tr>
                <td>To convert threshold image</td>
                <td>cv2.threshold()</td>
                <td></td>
            </tr>
            <tr>
                <td></td>
                <td>cv2.waitKey()</td>
                <td></td>
            </tr>
            <tr>
                <td></td>
                <td>cv2.destroyAllWindows()</td>
                <td></td>
            </tr>
        </table>
    - ### MATPLOTLIB
    - ### PYSDR
    