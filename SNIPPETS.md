# All Snippets 

## Ada

```
with Ada.Text_IO; use Ada.Text_IO;

procedure jello is begin
    Put_Line("jello!");
end jello;

```


## AppleScript

```
display dialog “jello!”
```


## Assembly

```
section .text
   global _start

_start:
   mov  edx,len
   mov  ecx,msg
   mov  ebx,1
   mov  eax,4
   int  0x80

   mov  eax,1
   int  0x80

section .data
msg db 'jello!', 0xa
len equ $ - msg

```


## AutoHotkey

```
MsgBox, jello!

```


## Bash

```
echo jello!
```


## Basic

```
10 PRINT "jello!"
20 END
```


## Batch

```
@echo off
echo jello!

```


## Brainfuck

```
+[----->+++<]>+++.-----.+++++++..+++.[--->+<]>----.
```


## C

```
#include <stdio.h>

int main()
{
    printf("jello!");
}

```


## C#

```
class jello
{
    static void Main()
    {
        System.Console.WriteLine("jello!");
    }
}

```


## C++

```
#include <string>

int main()
{
    printf("jello!");
}

```


## Clojure

```
(ns jello.core
  (:gen-class))

(defn -main 
  [& args]
  (println "jello!"))

```


## CoffeeScript

```
console.log "jello!"

```


## Dart

```
void main() {
  print('jello!');
}
```


## Delphi

```
program Jello;
{$APPTYPE CONSOLE}

begin
	WriteLn('jello!');
end.

```


## E

```
println("jello!")

```


## Elixir

```
IO.puts "Hello world!"

```


## F#

```
printfn "jello!"

```


## Go

```
package main
import "fmt"
func main() {
    fmt.Println("jello!")
}
```


## Groovy

```
println "jello!"

```


## Haskell

```
main = putStrLn "jello!"

```


## Haxe

```
class jello {
    static public function main():Void {
        trace("jello!");
    }
}

```


## Java

```
public class Main {
    public static void main(String[] args) {
        System.out.println("jello!");
    }
}
```


## JavaScript

```
console.log("jello!")

```


## Julia

```
println("jello!")

```


## Kotlin

```
fun main() {
    println("jello!")
}
```


## Lua

```
print("jello!")
```


## Luan

```
local Io = require "luan:Io.luan"
local print = Io.print

print("jello!")

```


## Moliere

```
imprime "jello!"

```


## Pascal

```
program Jello;
begin
	writeln("jello!");
end.

```


## Perl

```
use warnings;
print("jello!");

```


## PHP

```
<?php
	echo 'jello!';
?>
```


## PowerShell

```
Write-Output jello!

```


## Python

```
print("jello!")
```


## QBasic

```
PRINT "jello!"

```


## R

```
print("jello!")

```


## Racket

```
(displayln "jello!")
```


## Ruby

```
puts "jello!"
```


## Rust

```
fn main() {
    println!("jello!");
}
```


## Scala

```
object jello {
    def main(args: Array[String]) = {
        println("jello!")
    }
}
```


## Scheme

```
(display "jello")
(newline)

```


## Swift

```
print("jello!")

```


## TI83-BASIC

```
"jello!

```


## TypeScript

```
console.log("jello!")

```


## VBScript

```
document.write("jello!")

```


## Whitespace

```
   		 	 	 
	
     		  	 	
	
     		 		  
	
     		 		  
	
     		 				
	
      	    	
	
  


```

```
S S S T	T	S T	S T	S L
T	L
S S S S S T	T	S S T	S T	L
T	L
S S S S S T	T	S T	T	S S L
T	L
S S S S S T	T	S T	T	S S L
T	L
S S S S S T	T	S T	T	T	T	L
T	L
S S S S S S T	S S S S T	L
T	L
S S L
L
L

```

