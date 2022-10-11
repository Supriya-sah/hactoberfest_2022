function isPalindrome(line) {
    let param = line;
    let arrayLine = Array.from(String(param), String);
    let reverseArrayParam = arrayLine.reverse();
    let reverseParam = reverseArrayParam.join('');

    if (param == reverseParam) {
        return true;
    }

    return false;
}

console.log(isPalindrome('.!!.'));