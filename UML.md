# Primitives and Objects

## Primitives

* int 4 bytes
* char 1 byte
* long 8 bytes
* float 4 bytes
* double 8 bytes
* Boolean 1 byte

## Objects

* String
* Integer

## Difference between primitives and objects (In Java)

* Objects automatically choose the length of storage.
* Objects have methods to be called.


# Relationship between classes and UML diagrams

## Relationships

* Association

A line.

* Generalization / inheritance

An solid line with triangular arrow.

* Implimentation (from a interface)

Dotted lined with triangular arrow.

* Dependence

Dotted line with acute arrow.


## Goals for UML diagram: Minimize dependencies

More dependence means more complexity; more complexity means more possible errors generated from other classes.
It also means more difficulty to maintain.

To reduce dependency:

* Encapsulation (Information hiding)

To decrease the dependency through classes.

* Modularity

Modularity is dividng each levels of design into separatable parts. It's a kind of abstraction.

To decrease the dependency through modules.

* Encapsulation and Modularity creates interfaces between programs that information can only be transmitted through.

## Notes:

* This is UML class diagram, so there is no instantiation in it.
