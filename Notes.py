LControl - Lan Control (?)

Requirements

This module will handle requests from the http server
The GUI is only for any interface/settings that we may have
    Keep it clean/elegant
    Settings:
        Frequency for serving requests from http server
        Login information - Nothing fancy too fancy, I don't expect
                            this to be used in a public network
    Ex. Bottom right corner, doesn't take up much real estate on the monitor
        Resize window by size of display

HTTPS Server
    Requires login
        Authorization token(?) if user logs in
        I have no clue how to do this (STACKOVERFLOW AND LEARN)
    HTML - Main target is for mobile/smartphones
    Any requests should be somehow sent off to this main module

There should be one class for each main component:
    LControl
    GUI
    Https Server


Style guide:
    Spaces at the start and end of brackets IF there are parameters
        Ex. foo( bar )
    camelCase for local variables
    UPPER case for globals
    Classes should start with capitals and camelCase
        Ex. class LControlManager():



Example of a class
    class ClassName(object):
        """docstring for ClassName"""
        def __init__( self, arg ):
            super( ClassName, self ).__init__()
            self.arg = arg

        def foo(self):
            """docstring for foo"""
            arr = []            # Arrays are called "Lists" in python
            for i in Range( 10 ):
                arr.append( i )
            for i in arr:        # For-each loop
                print( i )         # Output: 1 2 3 4 5 ... on new lines of course
            return 0

        def bar( self ):
            """docstring for bar"""
            self.foo()            # Calls the foo function
                                # 'self' refers to the current object
                                # Similar to 'this' in C++

            t = type( self.arg )
            print( t )            # Prints out the type
                                # Python doesn't use the keywords
                                # Uses 'auto' for everything

            func = self.stub
            func()                # Calls the stub function

        def stub( self ):
            """docstring for stub"""
            pass                # does nothing, tells intepreter to not expect anything
                                # returns "None", null = None

        def outer( self ):
            def inner():
                print( "Helper function that only exists in outer()" )
                print( "You can also have outer functions outside of the class" )
            inner()             # Notice how it's inner() and not self.inner()
            return "You can return multiple items", True

        def test( self ):
            stringVal, boolVal = self.outer()
            return (stringVal, boolVal)

        def test2( self, val ):
            tuple = self.test()
            val = [ tuple[0], tuple[1] ]
            return False

        def test3( self, val="" ):
            """ val is initialized to "" if nothing passed in """"
            val += "Jacy"
            return None

        def test4( self ):
            """
            Explanation:
                There is no such thing as pass by reference in python
                The equivalent is passing in an immutable object and modifying that
                Immutable objects:
                    Lists        - []
                    Tuples       - ()
                    Dictionaries - {}
            """
            notRefVal = "Hello World"
            refVal = [ notRefVal, "Jacy" ]

            self.test2( refVal )
            self.test3( notRefVal )

            print( notRefVal )       # Output: "Hello World"
            print( refVal )          # Output: [ "You can return multiple items", True ]


        Dictionaries - Map/Set
            exampleDict = {
                            "Key1"        : "Val1",
                            "Key2"        : "Val2",
                            "SomeRandKey" : "SomeRandVal"
                          }



    """docstrings... """ - Description of the class
    This creates a class that inherits from 'object' - Most likely will not use
    super().__init__() - calls the inherited constructor
    __init__ is the "constructor" for the class
    self.x is a member instance to the class


    Extra notes:

        Operators:  C++     Python (lowercase is fine)
                    &&      AND
                    ||      OR
                            IN      - Left object IN right object  Ex. '1' in ['1', '0', '2']
                            IS      - IS object the same
                    true    True    - Capital T only
                    false   False   - Capital F only

                    ==      ==
                    !=      !=
                    >=      >=
                    <=      <=
                    >       >
                    <       <

            '=='' DOES NOT EQUAL TO 'IS'
                == - checks that objects are equivalent
                IS - checks that the two objects are the same
                When in doubt, stick with ==

        Indent using 4 SPACES, not tabs
        Python does not like mixing the two together

        Recommended sublime settings: (Copy and paste into settings)
        // Settings in here override those in "Default/Preferences.sublime-settings",
        // and are overridden in turn by syntax-specific settings.
        {
            // Set to true to removing trailing white space on save
            "trim_trailing_white_space_on_save": true,

            // By default, shift+tab will only unindent if the selection spans
            // multiple lines. When pressing shift+tab at other times, it'll insert a
            // tab character - this allows tabs to be inserted when tab_completion is
            // enabled. Set this to true to make shift+tab always unindent, instead of
            // inserting tabs.
            "shift_tab_unindent": true,

            // Set to true to insert spaces when tab is pressed
            "translate_tabs_to_spaces": true
        }
