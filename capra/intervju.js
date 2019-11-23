const palindrome = (maybeAPalindrome) => {
  // for (let i = 0; i < maybeAPalindrome.length() ; i++) {
  //   console.log('tes')
  //   let firstDigit = maybeAPalindrome[i];
  //   let lastDigit = maybeAPalindrome[maybeAPalindrome.length() - 1];
  //   setOut(firstDigit)
  //   console.log(firstDigit, lastDigit)
  // }
}

const palindromeMachine = (variable) => {
  const invertedVariable = variable.toString().split('').reverse().join('')
  const maybePalindrome = variable + parseInt(invertedVariable);

  // -1
  return maybePalindrome

}

const result = palindromeMachine(28);

console.log(result);