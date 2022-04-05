### Hi!
  * [Mark T. Holder](https://phylo.bio.ku.edu)
  * computational evolutionary biologist in EEB and the BI
  * https://orcid.org/0000-0001-5575-0536



### Overview
 * Reasons to use classes:
   * organization
   * bundling data together
   * encapsulation
   * modularity
 * Learning how to define and use classes in python.
   * Basic syntax
   * instance vs class
   * cascade of attribute lookup




### #1 Organization
    from dendropy import Tree

pulls in dozens of functions in a nice bundle.
  * Jeet Sukumaran's [DendroPy](https://dendropy.org/) has >2,000 functions
  * the vast majority are inside classes they pertain to: see [the Tree class docs](https://dendropy.org/library/treemodel.html#the-tree-class)
  * `tree.as_ascii_plot(...)` is less annoying having many `x_as_ascii_plot(...)` functions for every sort of data




### #2 Bundling data
Imagine writing a 3-D physics particle motion simulator. Each particle has:
  * mass
  * 3 position coordinates: `x_pos`, `y_pos`, `z_pos`
  * velocity in 3 directions: `x_vel`, `y_vel`, `z_vel`
If you have 100 particles...



#### Lots of lists - one for each attribute
    forces = calc_gravity(mass_l, x_pos_l, y_pos_l, z_pos_l)
    x_force_l, y_force_l, z_force_l = forces
    alter_velocity(mass_l, x_pos_l, y_pos_l, z_pos_l,
                   x_force_l, y_force_l, z_force_l,
                   x_vel_l, y_vel_l, z_vel_l)
It's annoying to have functions with 10 arguments.
If you add an attribute (`charge`, perhaps), you have to 
modify lots of function signatures.



#### Lists of lists - each inner list holds properties of one particle
    ###########   mass, xpos  ypos  zpos, xvel, yvel, zvel
    particles = [[10.5, 11.3, 12.3, -1.4,  0.3, 21.8, 1.5],
                 [20.1, 51.3, 27.3, 55.4, -1.8, 31.5, 3.5],
                 ...
                ]
    forces = calc_gravity(particles)
    alter_velocity(particles, forces)
  * Better, but is element 0 is mass, or xpos, ypos,...
  * wrong index = silent error
  * Hard to a new variable (unless it is at the end of each list)



#### Lists of dict - each dict holds properties of one particle
    particles = [{"mass": 10.5,
                  "x_pos": 11.3, "y_pos": 12.3, "z_pos": -1.4,
                  "x_vel": 0.3, "y_vel": 21.8, "z_vel": 1.5],
                ...
                ]
    forces = calc_gravity(particles)
    alter_velocity(particles, forces)
  * A lot better.
  * Initialization is a pain
  * Classes are a lot like this option, but with better error-checking and syntax...




#### Lists of instances of class Particle
    particles = [Particle(mass=10.5, pos=[11.3, 12.3,- 1.4],
                          vel=[0.3, 21.8, 1.5]),
                ...
                ]
    forces = calc_gravity(particles)
    alter_velocity(particles, forces)
  * Cleaner
  * You can add checks in the initialization of each particle to assure that `mass` is a number, `pos` and `vel` are lists of 3 numbers, _etc_
  * You can associate appropriate behavior (functions) with Particles



### #3 Encapsulation
    if person.current_age >= 21:
        print("You can buy alcohol (legally).")
    # person.current_age  might be the stored variable
    # OR person.birthdate might be the stored variable

  * When you write a class you can hide some of the ugly details from code that uses the class.
  * There are many ways to store data and keep it synchronized
  * A class's functions can assure data integrity without requiring the user to understand the implemenation details.



### #4 Modularity
    class WebServiceWrapper:
        ... # this class has a helper functions 
            #  for call web-services

    class OTWebServiceWrapper(WebServiceWrapper):
        ... # this class has helpers specific to the
            # OpenTreeOfLife web services

    class NCBIWebServiceWrapper(WebServiceWrapper):
        ... # This could hold helpers specific to 
            #  NCBI services

  * `WebServiceWrapper` becomes a module of behaviors that 
can be easily extended.
  * Helps us avoid code duplication




#### For further info on the basics of classes in Python
  * Corey Shafer has some nice youtube videos on classes at: https://youtu.be/ZDa-Z5JzLYM



### Everything in python has a type
    a = 34
    b = "34"
    c = [3, 4]
    type(a)
    type(b)
    type(c)
    a*10
    b*10
    c*10
The `class` statement lets you create a new type <small>(sort of - there is slight distinction between a type and a class, but beginners can ignore it)</small>



### Basic syntax
    class <i>SomeName</i>(<i>SomeParentClassName</i>):
        pass
  * defines a class called <i>SomeName</i>.
  * says that the new class will inherit behavior from the parent class <i>SomeParentClassName</i>

  * You need to indent the contained code following `:`
  * Like a function <code>def</code>, defining a <code>class</code> does not cause actions to be executed - it provides a recipe for later use



### Creating instances of your class
    class Person:
        pass

    me = Person()
    a = int("34")
    c = list("34")



### Even an empty class can be useful as organization
    me = Person()
    me.age = 49
    me.name = "Mark Holder"
is a bit cleaner than:

    myinfo = {}
    myinfo["age"] = 49
    myinfo["name"] "Mark Holder"
but it is very similar, see:

    print(me.__dict__)



### The "dot" notation is for "attribute" access
    me.age                  # preferred syntax
    getattr(me, "age")      # same, and occassionally useful
    me.__dict__["age"]      # same in _some_ cases 
    getattr(me, age)        # WRONG

    me.age = 50             # preferred syntax
    setattr(me, "age", 50)  # same, and occassionally useful
    me.__dict__["age"] = 50 # same in _some_ cases 
    setattr(me, age, 50)    # WRONG