// {{Variable Naming conventions}}

// 1. Snakecase: Words are delimited by an underscore.
let full_name = 'Masud Rana' 

// 2. Camelcase: Words are delimited by capital letters, except the initial word.
let fullName = 'Masud Rana' 

// 3. Pascalcase: Words are delimited by capital letters.
let FullName = 'Masud Rana' 

// -> Should follow the one convention for all the coding in a task
// -> Should not follow the multiple conventions for all the coding in a task


// Variable name should be meaningful for the task
let x = 'Masud Rana' // should not follow this convention
let name = 'Masud Rana' // should follow this convention

// Indentation of Coding
// should give spacing between Word to Word and Line to Line

/*
Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
*/


// comments or documentation

/**
 * addNumbers will be added any two number
 * @param {number} x -first number
 * @param {number} y - second number
 */

function addNumbers(x,y) {
  console.log('Sum is : ',x+y)
}

addNumbers(10,'20'); // ai function ta call korlei comment er likha ta dekhabey. jeita help korbey ai function ta ki kaj korey and aita kivby use korbo seita bujty




// DRY = Don't Repeat Yourself
// don't repeat same code
// same kaj bar bar korty holey , akta function toiri korey sei function ta k bar bar use kora better



// Void Deep Nesting
// akta loop er vitor arekta loop, tar vitorey arekta loop. avabey onk gula loop use kora avoid korty hby
//



// Avoid Unnecessary comments
// jeita dekhei bujha jai, seita comment korer dorkar nai
for (let i = 0; i < array.length; i++) { // for loop start
  const element = array[i];
} // for loop end


// File folder should be structured and it should organized properly
// different types of file should be located in different folders