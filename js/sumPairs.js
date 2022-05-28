exports.sumPairs = function (intArr, desiredNumber) {
    let pairs = []
    for (let i = 0; i < intArr.length; i++) {
        for (let j = i + 1; j < intArr.length; j++) {
            if (intArr[i] + intArr[j] === desiredNumber) {
                pairs.push([intArr[i], intArr[j]])
            }
        }
    }
    return pairs.length === 0 ? 'unable to find pairs' : pairs
}







