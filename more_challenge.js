String.prototype.insertInto = function (position, s) {
  return this.slice(0, position) + s + this.slice(position);
};
const permute = (str) => {
  console.log('permuting...', str);
  let permutations = [];
  if (typeof str !== "string") {
    return null;
  }

  // simpliest case "" -> []
  if (str.length === 0) {
    permutations.push("");
    return permutations;
  }
  // simple case "a" -> ['a']
  else if (str.length === 1) {
    permutations.push(str);
    return permutations;
  }
  // recursive case "abc" -> "a" inserted in all permutations of "b" and "c"
  else {
    let head = str.charAt(0);
    let tail = str.substring(1, str.length);

    // array with results
    let permutatedTail = permute(tail);

    // insert head into every posible combination of combinationList
    permutatedTail.forEach((chunk) => {
      for (let i = 0; i <= chunk.length; i++) {
        let insertd = chunk.insertInto(i, head);
        permutations.push(insertd);
      }
    });

    return permutations;
  }
}
console.log(permute('COO'))