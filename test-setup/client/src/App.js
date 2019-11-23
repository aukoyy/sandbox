import * as React from 'react';
import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [out, setOut] = useState('');

  const palindrome = (maybeAPalindrome) => {
    // for (let i = 0; i < maybeAPalindrome.length() ; i++) {
    //   console.log('tes')
    //   let firstDigit = maybeAPalindrome[i];
    //   let lastDigit = maybeAPalindrome[maybeAPalindrome.length() - 1];
    //   setOut(firstDigit)
    //   console.log(firstDigit, lastDigit)
    // }
  };

  const palindromeMachine = (variable) => {
    const invertedVariable = variable.toString().split('').reverse().join('')
    const maybePalindrome = variable + parseInt(invertedVariable);

    // -1
    palindrome(maybePalindrome)
    setOut(maybePalindrome)


  }


  useEffect(() => {
    palindromeMachine(28)
  }, [palindromeMachine]);

  return (
    <div >
      <h1>{out}</h1>
    </div>
  );
}

export default App;
