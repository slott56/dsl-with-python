Domain Specific Language (DSL) design can decompose a large problem into two smaller problems: a language to describe alternative solutions, and applications built around that language.
The idea is to replace code written in a general-purpose programming language with statements using a more specialized language.

A DSL can allow more people to help craft solutions to problems.
It can also improve productivity by pushing common data representation issues into the DSL.

An example of a widely-used DSL is the Regular Expression language to describe the structure of strings. Another example is the SQL language to describe database creation, retrieval, update, and delete operations.

Creating a DSL forces a developer to face a number of implementation choices.
Design a language from the ground up.
Use JSON or TOML or some other existing language.
Or, use Python and avoid the complexities of parsing.

This talk takes a light-hearted view of DSL design issues by looking at two case studies taken from the Table Top Role-Playing Games (TTRPG) domain.
This unique view-point can help to disentangle language design from the problem domain.

(There's no deep consideration of any specific TTRPG. Just two very general features.)

